# Handoff

Read this first, then `skill/SKILL.md` in full, then `registry/courses.json`.

## GitHub is the source of truth

This project runs in a **Claude Code cloud session**. The workspace you are in is
**ephemeral** — it is discarded when the session ends, and only files explicitly
delivered to the user survive it.

So the remote at `github.com/circlePulse/seminary_anki` is the source of truth, and
this is the whole discipline:

> **Pull at the start of every session. Push at the end of every session.**
> Work that is not pushed is lost when the session ends, silently.

That is not a best practice here, it is the only persistence there is. If a push
fails — auth, conflict, anything — **say so loudly and do not end the session
quietly.** The user needs to know the work did not survive. This project has already
lost five weeks once to an unpushed workspace; the difference now is that you have
git and credentials and can actually close the loop.

The three files that matter most — `ids.lock.json`, `delivered.json`, `decks/*.json`
— are plain text and are committed. Everything in `build/` is regenerable and stays
gitignored.

## Seeding the remote: done

Done on 2026-09-30. The zip's history is on `main`. **Never force-push again.** Every
session starts with `git pull` and ends with a normal push.

## What this is

Turning class notes into Anki decks. Two institutions — IOK Seminary (Arabic,
ḥadīth, fiqh) and UCI (Python, religious studies). Notes live in Notion;
`registry/courses.json` maps each course to its deck file, id prefix, Notion
location, and which domain packs to read. `registry/notion.md` maps the Notion pages
themselves: page ids, how each page is laid out, and what is still uncarded.

Current state: **1,191 notes across 10 decks.**

| deck | notes | course |
|---|---|---|
| quduri | 228 | HDT-201 |
| vocab | 192 | VOCAB |
| sarf | 169 | ARB-201 |
| arbaeen_ahadith | 158 | HDT-201 |
| nahw | 145 | ARB-201 |
| wrel | 110 | RELSTD-5B |
| pyth | 106 | ICS-H32 |
| arbaeen | 69 | HDT-201 |
| riyad | 10 | HDT-202 |
| arbaeen2 | 4 | HDT-201 |

## The session loop

1. The user says something terse — "now python", "check sarf notes", "Arbaeen
   Hadith 3". That means: fetch that Notion page, work out what is new since the last
   pass, and card it.
2. Read the domain packs for that course before drafting.
3. Edit `decks/X.json`. Ids are append-only — see below.
4. `python3 skill/scripts/generate_deck.py decks/X.json --delta`
5. **Deliver the delta `.apkg`, and only that.** In a cloud session anything left in
   `build/` is discarded, so it must be handed over explicitly or it does not exist.
   One file per changed deck, with its counts. See the delivery rules below.
6. `./build.sh` to regenerate the registry.
7. **Commit and push.** Confirm the push succeeded before ending the session.

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

These are the only things here that cannot be regenerated, and in a cloud session
they exist only in the commit you push. An unpushed change to `ids.lock.json` is the
worst possible thing to lose: the next session would reassign ids, and every note
would import as a duplicate with its review history orphaned.

## What to hand the user: delta packages, nothing else

`--delta` builds a package containing only notes that are **new or whose content
changed** since `delivered.json`. Unchanged notes are left out of the file entirely,
so Anki cannot touch them.

The rules, all of which came from getting it wrong:

- **One `.apkg` per deck that actually changed. Nothing else.** Not the deck JSON,
  not `ids.lock.json`, not `delivered.json`, not the repo zip. Those belong in the
  commit, not in the user's downloads.
- **A deck reporting `0 new, 0 changed` is not delivered and not mentioned.** Say
  nothing about decks that did not move.
- **Never hand over a full deck for a routine update.** `--full` exists for a fresh
  collection or a recovery, and nothing else. A full deck rewrites every note on
  import: one such import reported 138 notes updated when 8 had actually changed, and
  the user was right to object.
- **State the counts with each file** — how many new, how many changed — so the
  number Anki reports on import is never a surprise.
- **A package that was built but never imported** is recovered with
  `generate_deck.py decks/X.json --delta --resend id1,id2,…`. That puts the named cards
  back into a delta even though `delivered.json` records them as delivered.
- **If an earlier delta for the same deck has not been imported yet, say so.**
  Deltas are cumulative only against `delivered.json`, not against each other: a
  package built today does not contain what yesterday's package held.

A session that produces five decks' worth of work hands over five files. A session
that changes one deck hands over one. The user has pushed back on volume more than
once, and both times was objecting to files that had no reason to exist.

## Hard rules, each from a real failure

1. **Every card must be self-contained.** "Why is *this* ḥadīth half of knowledge?"
   fits every ḥadīth in the deck. 18 cards shipped with this defect before it was
   caught. Now linted at build time.
2. **The back must contain information the front doesn't.** "Which ḥadīth commands
   holding to the Sunnah?" → "Hold on firmly to my Sunnah…" is a paraphrase wearing a
   question mark. Feels easy, gets graded Good, teaches nothing. Now linted.
3. **No binary-choice fronts.** "Explicitly or implicitly typed?" is a coin flip and
   makes self-grading meaningless.
4. **Isolate inline Arabic in `<bdi>`; put all-Arabic lines in `<div class="arabic">`.** Bare Arabic in an English sentence makes the
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
  **Mixed lines only.** A line that is entirely Arabic (a paradigm, a singular/plural
  pair, an Arabic definition with blanks) goes in one `<div class="arabic">`, never
  per-run `<bdi>`. Per-run isolates in the LTR card put the مَاضِي on the left; 101
  cards were fixed for exactly this on 2026-10-01. The build now warns (`RTL — …`).
- **Notetypes are still named `Seminary Basic` / `Bidirectional` / `Cloze`** and now
  hold Python and religious-studies cards. Renaming is one line under the pinned ids.
- **`qud-051`–`qud-104`** carry session tag `sep09`, which is wrong; the real class
  date was never recorded.
- **The 2026-09-30 batch carries placeholder session tags.** The Ḥadīth 2 body
  (arbh-111–158) and the repentance cards (riyad-005–010) are tagged `sep30`, but their
  class dates are unknown. The user said this can be fixed later.
- **Ḥadīth 3's cards (arbh-052–110) show Ḥadīth 1's source line.** The deck-level
  `source` was never updated when Ḥadīth 3 was added. Fixing it re-sends all 59 as
  changed, so it waits for the user's go-ahead.
- **Gloss collision: "to write"** — صَنَّفَ (voc-007) and كَتَبَ (voc-186). Suggested
  fix: voc-007 becomes "to author, to compose (a book)". Awaiting the user.
- **Ḥadīth 2's matn is deliberately uncarded.** The user doesn't need to memorise it.
- **The Sep 24 "front names nothing" fix may never have reached the user's Anki.** On
  2026-09-30 they still saw "this ḥadīth" on Ḥadīth 1 cards. The 9 Ḥadīth 1 cards were
  re-sent with `--resend`. The other 9 from that fix (arb-038, qud-087, qud-109,
  qud-179, qud-185, tah-030, nahw-012/013/014, wrel-044) are unconfirmed. Re-send
  them the same way if the user sees the old wording.
- **Ḥadīth 3's matn was supplied from memory**, not from the notes, and is flagged on
  its own card for checking against the user's copy.

## Working style the user expects

Terse requests, answered by doing the work. They will say directly when something is
wrong, and they are usually right. They do not want the whole deck re-sent, options
laid out, or work they did not ask for. They do want to be told when their own notes
contain an error, and they want judgement calls surfaced rather than made silently.
