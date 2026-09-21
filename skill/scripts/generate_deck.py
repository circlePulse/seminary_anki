#!/usr/bin/env python3
"""
Build a .apkg from an approved draft.

Usage:
    pip install genanki --break-system-packages
    python3 generate_deck.py cards.json [-o /mnt/user-data/outputs]

Input JSON:
{
  "course": "MNT-101",
  "topic": "lafz-division",
  "session": "sep03",
  "source": "lecture notes 2026-09-03",
  "expected_count": 12,
  "cards": [
    {"type": "bidir", "tier": 1, "term": "لَفْظ",
     "meaning": "any sound produced by a human", "tags": ["terminology"]},

    {"type": "cloze", "tier": 1,
     "text": "اللَّفْظ is either {{c1::مَوْضُوع::the assigned one}} or {{c2::مُهْمَل}}",
     "extra": "", "tags": ["spine"]},

    {"type": "basic", "tier": 2,
     "front": "On what basis is لَفْظ divided?",
     "back": "whether a meaning has been assigned to it", "tags": ["criterion"]}
  ]
}

Optional per-card keys:
  "id"       stable, never-reused (e.g. "nahw-023"). Makes the note GUID stable so
             a corrected deck re-imports as an UPDATE rather than a duplicate.
  "session"  e.g. "sep17". Overrides the file-level session for a card added in a
             later class. The session tag is what "cram last week" filters on, so a
             deck that grows across classes needs it per card.
  "science"  e.g. "نَحْو". Renders as a small label above the field. Required on any
             card whose subject term is shared across sciences — see
             references/shared-terms.md.

course / topic / session / source are applied to every card automatically;
per-card "source" overrides the file-level one. "expected_count" is checked
against the approved draft and is a hard failure if it disagrees.

genanki cannot ship suspended cards. Tier 2 notes are tagged `tier2`; after
import, Browse -> `tag:tier2 -is:suspended` -> Ctrl+J.
"""

import argparse
import json
import os
import re
import sys

import genanki

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ids import (  # noqa: E402
    MODEL_BASIC, MODEL_BIDIR, MODEL_CLOZE,
    NAME_BASIC, NAME_BIDIR, NAME_CLOZE,
    STAGING_DECK_ID, STAGING_DECK_NAME,
)

# --------------------------------------------------------------------------
# Styling. Colours are declared once as custom properties and overridden in a
# single night-mode block. `.card` sets no color/background-color at all —
# Anki supplies both correctly per theme, and AnkiDroid inverts unspecified
# colours in night mode. No `prefers-color-scheme` query: it follows the OS,
# not Anki's theme, and mis-fires when they disagree.
# --------------------------------------------------------------------------
CSS = """
.card {
  --muted: #666;
  --rule: #ccc;
  --header-bg: #e8e8e8;

  direction: ltr;
  font-family: 'Scheherazade New', 'Amiri', 'Traditional Arabic',
               'Geeza Pro', Arial, sans-serif;
  font-size: 20px;
  line-height: 1.6;
  text-align: center;
}

.nightMode, .card.night_mode {
  --muted: #aaa;
  --rule: #555;
  --header-bg: #333;
}

.arabic { direction: rtl; font-size: 28px; line-height: 1.9; }
.transliteration { color: var(--muted); font-style: italic; font-size: .85em; }
.science { display: block; color: var(--muted); font-size: .62em; margin-bottom: 6px; }
.source { color: var(--muted); font-size: .7em; margin-top: 1.2em; }

ul, ol { text-align: left; display: inline-block; }

table { border-collapse: collapse; margin: 10px auto; }
th, td { border: 1px solid var(--rule); padding: 8px 12px; text-align: center; }
th { background-color: var(--header-bg); }
td.arabic, th.arabic { direction: rtl; font-size: 22px; line-height: 1.9; }
"""

SRC = '<div class="source">{{Source}}</div>'

MODEL_BASIC_DEF = genanki.Model(
    MODEL_BASIC, NAME_BASIC,
    fields=[{"name": "Front"}, {"name": "Back"}, {"name": "Source"}],
    templates=[{
        "name": "Card 1",
        "qfmt": "{{Front}}",
        "afmt": '{{FrontSide}}<hr id="answer">{{Back}}' + SRC,
    }],
    css=CSS,
)

MODEL_BIDIR_DEF = genanki.Model(
    MODEL_BIDIR, NAME_BIDIR,
    fields=[{"name": "Term"}, {"name": "Meaning"}, {"name": "Source"}],
    templates=[
        {"name": "Term to Meaning",
         "qfmt": "{{Term}}",
         "afmt": '{{FrontSide}}<hr id="answer">{{Meaning}}' + SRC},
        {"name": "Meaning to Term",
         "qfmt": "{{Meaning}}",
         "afmt": '{{FrontSide}}<hr id="answer">{{Term}}' + SRC},
    ],
    css=CSS,
)

MODEL_CLOZE_DEF = genanki.Model(
    MODEL_CLOZE, NAME_CLOZE,
    model_type=genanki.Model.CLOZE,
    fields=[{"name": "Text"}, {"name": "Extra"}, {"name": "Source"}],
    templates=[{
        "name": "Cloze",
        "qfmt": "{{cloze:Text}}",
        "afmt": "{{cloze:Text}}<br>{{Extra}}" + SRC,
    }],
    css=CSS,
)

TAG_RE = re.compile(r"\s+")

_STOP = set("a an the of to in on for and or is are was were be been that this these "
            "those it its his her their with from as at by not no what which who whom "
            "how when where does do did there s t".split())


def _content_words(text):
    text = re.sub(r"<[^>]+>", " ", text).lower()
    text = re.sub(r"[^a-z\u0600-\u06ff ]", " ", text)
    return {w for w in text.split() if w not in _STOP and len(w) > 2}


def giveaway_ratio(front, back):
    """
    How much of the answer is already sitting on the question.

    A card must require retrieval: the back has to carry information the front
    does not. "Which hadith commands holding to the Sunnah?" -> "Hold on firmly
    to my Sunnah..." is a paraphrase, not a memory test, and it will always feel
    easy while teaching nothing.

    Lexical overlap is a proxy, not a verdict — "Which century was the golden
    age?" -> "The 200s, the 3rd century AH" scores high and is a perfectly good
    card. Flagged cards get looked at, not auto-rejected.
    """
    b = _content_words(back)
    if not b:
        return 0.0
    return len(_content_words(front) & b) / len(b)


def clean_tags(tags):
    """Anki tags are space-separated; spaces inside a tag silently split it."""
    return [TAG_RE.sub("-", t.strip()) for t in tags if t and t.strip()]


def label(text, science):
    """Prefix a field with its science, so shared terms can never be ambiguous."""
    if not science:
        return text
    return f'<div class="science">{science}</div>{text}'


def note_guid(course, card, i):
    """
    Stable GUID so a re-import UPDATES a note instead of duplicating it.
    Requires an explicit, never-reused `id` per card; without one the guid is
    derived from field content, and any edit to the text creates a second note.
    """
    cid = card.get("id")
    if cid:
        return genanki.guid_for(course, cid)
    return None


def validate(card, i):
    errs = []
    t = card.get("type")
    if t not in ("basic", "bidir", "cloze"):
        errs.append(f"card {i}: unknown type {t!r}")
        return errs
    if card.get("tier") not in (1, 2):
        errs.append(f"card {i}: tier must be 1 or 2")
    required = {"basic": ("front", "back"),
                "bidir": ("term", "meaning"),
                "cloze": ("text",)}[t]
    for f in required:
        if not str(card.get(f, "")).strip():
            errs.append(f"card {i}: missing {f!r}")
    if t == "cloze" and "{{c1::" not in card.get("text", ""):
        errs.append(f"card {i}: cloze text has no {{{{c1::...}}}} deletion")
    return errs


def build(data, outdir):
    for key in ("course", "topic", "session", "cards"):
        if key not in data:
            sys.exit(f"cards.json is missing required key {key!r}")

    cards = data["cards"]
    expected = data.get("expected_count")
    if expected is not None and expected != len(cards):
        sys.exit(f"expected_count {expected} != {len(cards)} cards in file. "
                 "The draft and the transcription disagree — fix before generating.")

    errors = []
    for i, c in enumerate(cards, 1):
        errors += validate(c, i)
    if errors:
        sys.exit("\n".join(errors))

    deck = genanki.Deck(STAGING_DECK_ID, STAGING_DECK_NAME)
    base_tags = [data["course"], data["session"]]
    giveaways = []
    counts = {"basic": 0, "bidir": 0, "cloze": 0, "tier2": 0, "stable": 0}

    for c in cards:
        # session is when the material was TAUGHT; decks grow across many classes,
        # so a card may override the file-level session
        tags = clean_tags([data["course"], c.get("session") or data["session"]]
                          + list(c.get("tags", [])))
        if c["tier"] == 2:
            tags.append("tier2")
            counts["tier2"] += 1
        src = c.get("source") or data.get("source", "")

        sci = c.get("science")
        guid = note_guid(data["course"], c, None)
        if guid:
            counts["stable"] += 1

        if c["type"] == "basic":
            note = genanki.Note(MODEL_BASIC_DEF,
                                [label(c["front"], sci), c["back"], src],
                                tags=tags, guid=guid)
        elif c["type"] == "bidir":
            # label both fields: either one can be the front
            note = genanki.Note(MODEL_BIDIR_DEF,
                                [label(c["term"], sci), label(c["meaning"], sci), src],
                                tags=tags, guid=guid)
        else:
            note = genanki.Note(MODEL_CLOZE_DEF,
                                [label(c["text"], sci), c.get("extra", ""), src],
                                tags=tags, guid=guid)
        if c["type"] == "basic" and giveaway_ratio(c["front"], c["back"]) >= 0.45:
            giveaways.append(c.get("id") or c["front"][:50])

        counts[c["type"]] += 1
        deck.add_note(note)

    os.makedirs(outdir, exist_ok=True)
    fname = f"{data['course']}_{data['topic']}_{data['session']}.apkg"
    path = os.path.join(outdir, fname)
    genanki.Package(deck).write_to_file(path)

    cloze_cards = sum(
        len(set(re.findall(r"\{\{c(\d+)::", c["text"])))
        for c in cards if c["type"] == "cloze")
    est = counts["basic"] + counts["bidir"] * 2 + cloze_cards

    print(f"wrote {path}")
    print(f"  notes: {len(cards)}  "
          f"(basic {counts['basic']}, bidir {counts['bidir']}, cloze {counts['cloze']})")
    print(f"  expected cards in Anki: ~{est}")
    print(f"  tier2 notes tagged for suspension: {counts['tier2']}")
    if counts["stable"] == len(cards):
        print("  stable GUIDs: all notes — re-import will update in place")
    elif counts["stable"]:
        print(f"  WARNING: only {counts['stable']}/{len(cards)} notes have stable ids; "
              "the rest will duplicate on re-import")
    else:
        print("  WARNING: no card ids — any future edit will duplicate on re-import")
    if giveaways:
        print()
        print("  REVIEW — the front may be giving away the answer on these:")
        for g in giveaways:
            print(f"    {g}")
        print("  (lexical overlap only; check each one rather than assuming)")
    print()
    print("After importing:")
    print("  1. Browse -> `tag:tier2 -is:suspended` -> Ctrl+J to suspend")
    print("  2. Tools -> Manage Note Types -> confirm no `Basic+` types appeared")
    print(f"  3. Sort out of {STAGING_DECK_NAME} into your course decks")
    return path


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("cards_json")
    ap.add_argument("-o", "--outdir", default="build")
    a = ap.parse_args()
    with open(a.cards_json, encoding="utf-8") as fh:
        build(json.load(fh), a.outdir)
