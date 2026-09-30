# Handoff

Read this first, then `skill/SKILL.md` in full, then `registry/courses.json`.

## Where this now lives

This project has moved out of a chat sandbox and onto the user's own machine, run
through **Claude Code** in the Claude Desktop app. That changes the most important
thing about it: **the folder you are working in is permanent.** It is not rebuilt
each session and it does not disappear when the conversation ends.

Everything below assumes that. If you find yourself about to reconstruct state from
an `.apkg`, from Notion, or from the conversation — stop. The files are on disk.

Two constraints that come with the setup:

- Reaching local files needs the Claude Desktop app open and connected.
- **Run sessions locally, not in the cloud.** In a cloud session only files that are
  explicitly delivered are kept; working files are discarded when the session ends.
  That is precisely the failure mode this move is meant to end.

Connectors — Notion in particular — stay linked across sessions, so fetching the
class notes works the same way it always has.

## First run, once

1. Confirm the folder is a git repo with history: `git log --oneline | head`.
   You should see about 19 commits, most recent first.
2. `git remote -v` — the remote is `github.com/circlePulse/seminary_anki`.
   **It is roughly five weeks and 18 commits behind this folder.** It holds the state
   of 2026-09-10: ~330 notes, no Python deck, no World Religions deck, none of the
   delta machinery.
3. **Push, and do not pull first.** A merge or rebase against that stale remote is a
   good way to lose five weeks. `git push origin main` — force it if the remote has
   diverged, after checking nothing on it is newer than this folder.
4. `pip install genanki` if it isn't present, then `./build.sh`. It should report
   1,081 ids, none lost, and no pending deliveries.

From then on: **commit and push at the end of every session.** Git is right there
now; the reason this drifted before was that pushing was a manual step outside the
tool doing the work. It no longer is.

## What this is

Turning class notes into Anki decks. Two institutions — IOK Seminary (Arabic,
ḥadīth, fiqh) and UCI (Python, religious studies). Notes live in Notion;
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

## The session loop

1. The user says something terse — "now python", "check sarf notes", "Arbaeen
   Hadith 3". That means: fetch that Notion page, work out what is new since the last
   pass, and card it.
2. Read the domain packs for that course before drafting.
3. Edit `decks/X.json`. Ids are append-only — see below.
4. `python3 skill/scripts/generate_deck.py decks/X.json --delta`
5. Tell the user the `.apkg` is in `build/` and what is in it — how many new, how many
   changed. They import it from there; no download step any more.
6. `./build.sh` to regenerate the registry, then commit and push.

## Three files you cannot afford to lose

- **`ids.lock.json`** — every card id ever assigned, with a content fingerprint. A
  note's Anki GUID derives from `(course, id)`. Change an id and the note stops being
  an update and becomes a **duplicate**, orphaning that note's review history with no
  way to recover it. Ids are append-only; a deleted card burns its id forever.
  `check_ids.py` fails the build when a large fraction of a deck's ids start pointing
  at different cards, which is the signature of a positional renumber.
- **`delivered.json`** — the content hash of every note as last handed over. This is
  what makes delta delivery possible.
- **`decks/*.json`** — the source. Never rebuild a deck from Notion, from an `.apkg`,
  or from the conversation.

Now that these sit on a real disk, back them up like any other work. They are the
only thing here that cannot be regenerated.

## Deliver only what changed

`--delta` builds a package containing only notes that are new or whose content
differs from `delivered.json`. Unchanged notes are left out entirely, so Anki never
touches them.

Handing over a full deck for a routine update rewrites every note on import. The user
noticed — an import reported 138 notes updated when 8 had actually changed — and was
right to object. `--full` is for a fresh collection or recovery only.

Mention only the decks that actually gained cards.

## Hard rules, each from a real failure

1. **Every card must be self-contained.** "Why is *this* ḥadīth half of knowledge?"
   fits every ḥadīth in the deck. 18 cards shipped with this defect before it was
   caught. Now linted at build time.
2. **The back must contain information the front doesn't.** "Which ḥadīth commands
   holding to the Sunnah?" → "Hold on firmly to my Sunnah…" is a paraphrase wearing a
   question mark. Feels easy, gets graded Good, teaches nothing. Now linted.
3. **No binary-choice fronts.** "Explicitly or implicitly typed?" is a coin flip and
   makes self-grading meaningless.
4. **Isolate inline Arabic in `<bdi>`.** Bare Arabic in an English sentence makes the
   neutral characters around it — punctuation, parentheses, cloze delimiters — resolve
   RTL and render on the wrong side. See `skill/references/arabic.md`. Do not force
   `direction: rtl` on `<bdi>`; it defaults to `dir=auto` and that is the point.
5. **Flag, don't guess.** The user's notes contain transcription slips — *prompt
   injection* for code injection, *kebob_case* for snake_case, a verb form that does
   not exist. Correct mechanical slips and say so; never silently resolve a
   substantive ambiguity.
6. **Filenames carry a timestamp to the minute.** Two deliveries for the same deck on
   the same day once overwrote each other before the user had imported the first.

## Pending

- **~530 fields need `<bdi>` wrapping** — cards written before rule 4 was recorded.
  The user is having this done separately. The verification rule: stripping the tags
  back out must leave the text byte-identical. Afterwards those decks will show a
  large delta, which is correct.
- **Notetypes are still named `Seminary Basic` / `Bidirectional` / `Cloze`** and now
  hold Python and religious-studies cards. Renaming is one line under the pinned ids.
- **`qud-051`–`qud-104`** carry session tag `sep09`, which is wrong; the real class
  date was never recorded.
- **Arbaʿīn Ḥadīth 2's body is uncarded** — only its vocabulary went in. The section
  covers Umm al-Ḥadīth, Ḥadīth Jibrīl, and the definitions of Islām, Īmān and Iḥsān.
- **Ḥadīth 3's matn was supplied from memory**, not from the notes, and is flagged on
  its own card for checking against the user's copy.

## Working style the user expects

Terse requests, answered by doing the work. They will say directly when something is
wrong, and they are usually right. They do not want the whole deck re-sent, options
laid out, or work they did not ask for. They do want to be told when their own notes
contain an error, and they want judgement calls surfaced rather than made silently.
