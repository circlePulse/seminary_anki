# Handoff

Read this before touching anything. Then read `skill/SKILL.md` in full, then
`registry/courses.json`.

## Start from this zip, not from GitHub

The remote at `github.com/circlePulse/seminary_anki` is **18 commits and roughly
five weeks behind**. It holds the state of 2026-09-10 — about 330 notes, no Python
deck, no World Religions deck, no delta machinery. The push step was manual and
never happened.

**Cloning it and working from there would silently discard five weeks of work.**
This zip is the current state. Push it first, or work from it directly, but do not
treat the remote as the source of truth until it has been updated.

## What this is

A system for turning class notes into Anki decks. Two institutions: IOK Seminary
(Arabic, ḥadīth, fiqh) and UCI (Python, religious studies). Notes live in Notion;
`registry/courses.json` maps each course to its deck file, id prefix, Notion
location, and which domain packs to read.

Current state: **1,081 notes across 10 decks.**

| deck | notes | course |
|---|---|---|
| quduri | 206 | HDT-201 |
| vocab | 192 | VOCAB |
| sarf | 169 | ARB-201 |
| nahw | 145 | ARB-201 |
| arbaeen_ahadith | 110 | HDT-201 |
| pyth | 106 | ICS-H32 |
| wrel | 76 | RELSTD-5B |
| arbaeen | 69 | HDT-201 |
| riyad | 4 | HDT-202 |
| arbaeen2 | 4 | HDT-201 |

## Three files you cannot afford to lose

Everything else is recoverable. These are not.

- **`ids.lock.json`** — every card id ever assigned, with a content fingerprint.
  A note's Anki GUID derives from `(course, id)`. Change an id and the note stops
  being an update and becomes a **duplicate**, orphaning that note's review history
  with no way to recover it. Ids are append-only. `skill/scripts/check_ids.py`
  fails the build when a large fraction of a deck's ids start pointing at different
  cards, which is the signature of a positional renumber.
- **`delivered.json`** — the content hash of every note as last handed to the user.
  This is what makes delta delivery possible.
- **`decks/*.json`** — the source. Never rebuild a deck from Notion, from the
  conversation, or from an `.apkg`.

## The rule that generated the most friction

**Deliver only what changed.** `generate_deck.py decks/X.json --delta` builds a
package containing only notes that are new or whose content differs from
`delivered.json`. Unchanged notes are left out entirely, so Anki never touches them.

Handing over a full deck for a routine update rewrites every note on import. The
user noticed — an import reported 138 notes updated when 8 had actually changed —
and was right to object. Full builds (`--full`) are for a fresh collection or
recovery only.

Present only the packages that are non-empty, and only for decks that gained cards.

## Hard-won rules, each from a real failure

1. **Every card must be self-contained.** "Why is *this* ḥadīth half of knowledge?"
   fits every ḥadīth in the deck. 18 cards shipped with this defect before it was
   caught. Now linted.
2. **The back must contain information the front doesn't.** "Which ḥadīth commands
   holding to the Sunnah?" → "Hold on firmly to my Sunnah…" is a paraphrase wearing
   a question mark. Feels easy, gets graded Good, teaches nothing. Now linted.
3. **No binary-choice fronts.** "Explicitly or implicitly typed?" is a coin flip and
   makes self-grading meaningless.
4. **Isolate inline Arabic in `<bdi>`.** Arabic bare inside an English sentence makes
   the neutral characters around it — punctuation, parentheses, cloze delimiters —
   resolve RTL and render on the wrong side. Roughly 530 older fields still have this
   defect and are being fixed separately; see `skill/references/arabic.md`. Do not
   force `direction: rtl` on `<bdi>`; it defaults to `dir=auto` and that is the point.
5. **Flag, don't guess.** The user's notes contain transcription slips —
   *prompt injection* for code injection, *kebob_case* for snake_case, a verb form
   that does not exist. Correct mechanical slips and say so; never silently resolve a
   substantive ambiguity.
6. **Filenames carry a timestamp to the minute.** Two deliveries for the same deck on
   the same day once overwrote each other.

## Pending

- **~530 fields need `<bdi>` wrapping.** Cards from before the rule was recorded.
  A brief for this exists; the verification rule is that stripping the tags back out
  must leave text byte-identical.
- **Notetypes are still named `Seminary Basic` / `Bidirectional` / `Cloze`** and now
  hold Python and religious-studies cards. Renaming is one line under the pinned ids.
- **`qud-051`–`qud-104`** carry session tag `sep09`, which is wrong; the real class
  date was never recorded.
- **Arbaʿīn Ḥadīth 2's body is uncarded** — only its vocabulary went in. The section
  covers Umm al-Ḥadīth, Ḥadīth Jibrīl, and the definitions of Islām, Īmān and Iḥsān.
- **Ḥadīth 3's matn was supplied from memory**, not from the notes, and is flagged on
  its own card for verification against the user's copy.

## Working style the user expects

Terse requests — "now python", "check sarf notes" — mean: fetch that Notion page,
work out what is new since the last pass, and card it. They will say when something
is wrong, directly. They do not want the whole deck re-sent, options laid out, or
work they did not ask for. They do want to be told when their notes contain an error.
