---
name: seminary-anki
description: Turn class notes into Anki decks — IOK Seminary and UCI university courses alike (.apkg) — decomposing lecture notes into propositions, drafting cards for review, and generating decks with genanki. Use whenever the user wants flashcards, Anki cards, study cards, or a deck made from class notes, lecture transcriptions, textbook material, or vocabulary lists, in any subject — seminary (ḥadīth, fiqh, manṭiq, naḥw, ṣarf, ʿaqīdah, tafsīr, uṣūl) or university (programming/CS, religious studies, humanities, social science). Handles Arabic/RTL content, dark mode, and pinned notetype IDs. Also use when editing, auditing, or adding to an existing deck.
---

# Study Anki

Generate Anki decks from class notes — IOK Seminary and UCI alike. One system:
shared scripts, one id ledger, one `delivered.json`, one Anki collection. What
changes between courses is which **domain pack** gets read. Read this file fully, then read the reference files listed under **Reference map** that apply — they are not optional background, they contain the rules that make the output usable.

## Non-negotiables

1. **Never omit silently.** Every proposition in the source becomes a Tier 1 card, a Tier 2 card, or a line in the Omissions log with a reason. "It seemed minor" is Tier 2, not omission. A missing card is invisible until the moment it was needed; a surplus card is fixed with one keypress.
2. **Decompose before drafting.** Ask what claims the sentence makes, not what card to write. See `references/card-design.md` §1.
3. **The back must contain information the front does not.** If the answer is a re-wording of the question, there is no retrieval. Card a text as a completion prompt ("Complete: 'Hold on firmly to …'"), never as a description of its own content. The generator flags likely giveaways at build time.
4. **One fact per card.** If the back holds two things that could each be a question, it is two cards.
5. **Arabic everywhere, fully vowelized.** Never bare transliteration. See `references/arabic.md`.
6. **Draft to a file and get approval before generating.** Never generate from an unreviewed draft.
7. **Never call `random.randrange()` for a model ID.** IDs come from `scripts/ids.py`. This is what produced `Basic++++++++`.
8. **Label shared terms with their science.** A term that means something else in another science (مُفْرَد, فِعْل) gets a `"science"` label on every card where it is the subject. When a new collision appears, fix the *older* card too — it stopped being unambiguous the moment the second sense arrived. Registry: `references/shared-terms.md`.
9. **Deliver deltas, never full decks.** `delivered.json` records the content hash of every note as last handed over. A note is re-sent only when its hash changes. Full builds (`--full`) are for a fresh collection or recovery, never routine delivery.
10. **Give every card a stable `id`.** Without one, correcting a card and re-importing creates a duplicate instead of an update.
11. **Ask rather than invent.** Fill mechanical gaps in the notes; flag substantive ones. Never reconstruct a criterion of division — a wrong criterion is invisible and every downstream card inherits it.

## Workflow

0. **Identify the course** in `registry/courses.json` — it gives the deck file, the id prefix, the Notion page, and which domain packs to read. Read those packs before drafting.
1. **Ingest.** Read the source. Find inline `{{ CLAUDE: ... }}` notes first — they are instructions, never content, and they override defaults here.
2. **Decompose.** Pass 1 sentence-level, pass 2 section-level. `references/card-design.md` §1.
3. **Check the working files.** Gloss index for collisions; forward-reference log for anything this session resolves. `references/working-files.md`.
4. **Draft to `/home/claude/draft_{COURSE}_{topic}.md`** — always, before showing anything in chat. Format in `references/working-files.md`.
5. **Present for review.** Lead with blocking questions. Paste the table or use `present_files`.
6. **Revise in place** with `str_replace`. The file is authoritative; never regenerate the whole draft in chat.
7. **Generate on explicit approval — and deliver only what changed.** Run `generate_deck.py decks/X.json --delta` for each deck that gained or changed cards. The package contains **only** notes that are new or whose content differs from what was last delivered; unchanged notes are left out entirely, so Anki never touches them. Never hand over a full deck for a routine update — every card in it gets rewritten on import. Present only the delta packages that are non-empty.
8. **Give the post-import steps** (below) with the file.

## Post-import steps for the user

Every deck lands in the staging deck `Seminary::_Inbox` for manual sorting. Two actions after import:

1. Browse → `tag:tier2 -is:suspended` → **Ctrl+J** to suspend. (genanki cannot ship suspended cards; this is the one manual step that replaces it.)
2. Tools → Manage Note Types → confirm no suffixed types (`Basic+`) appeared.

## Reference map

| Read this | When |
|---|---|
| `references/card-design.md` | **Always.** Decomposition, the three tests, triage, card types, structural/spine notes, vocabulary, interference. |
| `references/arabic.md` | Seminary courses — any Arabic content. |
| `references/working-files.md` | Reading class notes; draft file, gloss index, forward-reference log formats. |
| `references/notetypes.md` | Generating a deck, or touching CSS/templates. |
| `registry/courses.json` | **First, every time.** Which course this is, where its notes live, its id prefix, and which packs to read. |
| `references/domain-cs.md` | Programming courses (ICS-H32). |
| `references/domain-humanities.md` | Humanities / social science (RELSTD-5B). |
| `references/shared-terms.md` | Seminary courses. Registry of terms that mean different things in different sciences, and the labelling rule. |

## Deck and tag policy

Decks are sorted **by hand** in Anki desktop, so deck membership encodes nothing and **tags carry all organisation**. Every note gets, without exception:

- course code (`MNT-101`)
- topic (`terminology`, `asanid`)
- session date (`sep03`)
- `tier2` if secondary
- `spine` / `criterion` / `placement` on structural notes
- a `Source` field value (lecture date, page, or ḥadīth number)

An untagged card is unfindable, and manual sorting never recovers what the tag would have told you.
