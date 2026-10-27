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

Current state: **2,157 notes across 10 decks.**

| deck | notes | course |
|---|---|---|
| vocab | 463 | VOCAB |
| quduri | 305 | HDT-201 |
| arbaeen_ahadith | 302 | HDT-201 |
| wrel | 303 | RELSTD-5B |
| sarf | 246 | ARB-201 |
| nahw | 238 | ARB-201 |
| pyth | 217 | ICS-H32 |
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
   `direction: rtl` on `<bdi>`; it defaults to `dir=auto` and that is the point. The templates
   wrap every side in `<div dir="ltr">`, because some Anki clients auto-detect the card's direction
   from its first letter. On 2026-10-13 that flipped 450 notes that open with Arabic. Never remove
   the wrapper. A template change reaches the user only in a package holding one note of each
   notetype (`--resend`; see `skill/references/notetypes.md`).
5. **Flag, don't guess.** The user's notes contain transcription slips — *prompt
   injection* for code injection, *kebob_case* for snake_case, a verb form that does
   not exist. Correct mechanical slips and say so; never silently resolve a
   substantive ambiguity.
6. **Every card is active.** The user said so on 2026-10-06. Draft nothing as Tier 2,
   and never tell them to suspend anything. The 22 older `tier2` notes keep the tag as a
   label only.
7. **Filenames carry a timestamp to the minute.** Two deliveries for the same deck on
   the same day once overwrote each other before the user had imported the first.
8. **In chat replies and draft prose, open every paragraph and list item with an English word.** The Claude
   app sets a block's direction from its first strong letter, and a whole list from its first item's. On
   2026-10-14 a reply whose bullets opened with Arabic rendered right to left throughout ("it's all
   backwards"). Inside a line, keep Arabic words apart with English, such as a gloss in parentheses:
   `مُرُوءَة (decorum) or سُمْعَة (reputation)`. Never join them with only a comma or an arrow, because
   Arabic–punctuation–Arabic becomes one right-to-left run and reverses the order. Write "your مروؤ is now
   مُرُوءَة", not "مروؤ → مُرُوءَة".

## Pending

- **~400 fields still need `<bdi>` wrapping** — cards written before rule 4 was recorded.
  `skill/scripts/wrap_arabic.py decks/X.json` does it (report only; add `--write`), and
  refuses to write unless stripping the tags back out leaves the text byte-identical.
  **Sarf is done** (139 fields, 2026-10-02, after the user hit a scrambled sarf-080). Still
  to do, as of 2026-10-08: nahw 170, quduri 118, arbaeen 34, vocab 13 (voc-177 was wrapped on 2026-10-14 when a retag re-sent it), arbaeen_ahadith 10,
  arbaeen2 6, riyad 4. These are lower than first counted because a field whose only Arabic
  is ﷺ no longer counts. Each deck shows a large delta afterwards, which is correct.
  Offered to the user; do these only on their go-ahead.
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
  class dates are unknown. The user said this can be fixed later. Two more are best guesses: kāna
  (nahw-191–208) is tagged `oct01`, and the 2026-10-08 ṣarf batch (sarf-170–192) is tagged `oct08`.
- **Ḥadīth 3's cards (arbh-052–110) show Ḥadīth 1's source line.** The deck-level
  `source` was never updated when Ḥadīth 3 was added. Fixing it re-sends all 59 as
  changed, so it waits for the user's go-ahead.
- **Gloss collision: "to write"** — صَنَّفَ (voc-007) and كَتَبَ (voc-186). Suggested
  fix: voc-007 becomes "to author, to compose (a book)". Awaiting the user.
- **sarf-073's hints give its answers away.** "regularly" points to *present habitual* and
  "right now" to *present continuous*, and each example sentence gives it away a second time.
  arbh-041 had the same defect and was rewritten on 2026-10-02 to blank the content
  instead of the labels. sarf-073 was flagged to the user and is awaiting their go-ahead.
- **The vocabulary lists now follow the Riyāḍ class through the book.** The user confirmed on 2026-10-14
  that the 10-06 list (voc-193–230) is Bāb al-Ṣabr, tagged `riyad-sabr`. The 10-13 and 10-14 lists
  (voc-231–323) are Bāb al-Ṣidq, tagged `riyad-sidq`. The 10-21 lists are Bāb al-Murāqabah (`riyad-muraqabah`) and
  Bāb al-Taqwā (`riyad-taqwa`). The 10-27 list is Bāb al-Yaqīn wa-l-Tawakkul (`riyad-tawakkul`, voc-447–463). Words from the Qaṣaṣ class are tagged `qasas` (voc-396–406); the user now heads
  them separately. The older `riyad-qasas` tag (voc-064–133) mixes the two classes. Tag the next list by its
  chapter, and ask if it isn't obvious from the words.
- **Calculus II and Tazkiyah are on hold.** The user said "don't do calculus or tazkiya yet" on 2026-10-14.
  Calculus II now has a *Review* section of formulas, and Tazkiyah has never been carded. Neither has a deck.
  Don't card or draft either until the user asks.
- **Ḥadīth 5 (arbh-223–246) has two points the user was asked to check with the teacher.** First, the notes say
  ʿĀʾishah RA moved in during year 2 AH, while most sources say Shawwāl of year 1. Second, the notes say she lived
  "40 years" after the Prophet ﷺ, but 57 − 11 AH is 46, so the card says "more than forty". Its matn, in
  `texts/arbaeen_h05.md`, was supplied by Claude from the standard text, not from the user's copy.
- **Ḥadīth 6 (arbh-247–266) has two points for the user to check.** First, the notes say al-Nuʿmān ibn Bashīr RA
  was killed in 56 AH, but the sources say 64 or 65 AH, so the card says that. Second, the translation in
  `texts/arbaeen_h06.md` is Claude's and unchecked, and arbh-263 rests on it. Its matn was supplied by Claude from
  the standard text. The page's "DON'T START YET" note had been left by mistake; Claude removed it on 2026-10-22,
  at the user's request.
- **World Religions 10/15–10/20 (wrel-192–284) departs from the notes in four places, by design.** The user
  approved the draft with each one flagged. wrel-202 gives Zhu Xi's actual view of human nature (with Mengzi),
  where the notes say he took none. wrel-223 says the Enigmatic Female's gate is the root of Heaven and earth,
  where the notes say a thread. wrel-248 adds Daodejing 42's step from the two to the three. wrel-266 finishes
  a sentence that breaks off ("lead people astray"). The Daodejing chapter numbers on the backs are Claude's;
  the notes give only chapter 4.
- **Ṣarf ṣaghīr cloze tables (approved 2026-10-23, "Looks perfect").** Each is a table of the class pattern
  (صَرَّفَ يُصَرِّفُ تَصْرِيفًا …), with the fixed words greyed and one blank per form. sarf-245 is tafʿīl on
  صَرَّفَ, and sarf-246 is mufāʿalah on قَاتَلَ, with both maṣdars at the user's word (its fiʿāl maṣdar is c10). The
  design is in `drafts/draft_2026-10-23_sarf-saghir.md`, and `saghir()` in `drafts/sarf_saghir_template.py` and
  the 10-23 author script builds one from the forms. Family one's six abwāb were offered the same tables, with
  no answer yet.
- **Cloze answers are now highlighted (2026-10-23).** The CSS has a `.cloze` rule, bold and blue, so a table card
  shows which cell was asked. It reached the user in the 10-23 ṣarf package, which holds all three notetypes.
- **Ḥadīth 7 (arbh-271–302) rests partly on Claude's translation.** The translation is in `texts/arbaeen_h07.md`
  and the user hasn't checked it; arbh-281 rests on it. Its matn was supplied by Claude from the standard text.
- **Riyāḍ memorisation cards are drafted, awaiting approval (2026-10-27):** `drafts/draft_2026-10-27_memorisation.md`,
  riyad-011–030 plus sarf-247. They cover both Riyāḍ to-dos: the open one (37, 54, 61, the second narration of 62, 71,
  and 82's duʿāʾ) and the checked one (7, 16, 25, and the phrase in 29). Each ḥadīth has a phrase-by-phrase cloze and a
  recitation card. The texts are Claude's, from the standard edition (sunnah.com numbering, which matches the
  user's), in `texts/riyad_memorisation.md`. Five points await the user: 7's وَأَعْمَالِكُمْ, 82's أَزِلَّ (the online
  text has أَذِلَّ), where 82's duʿāʾ starts, and 62's first narration. The user asked on 2026-10-27 for every required
  memorisation item to have cards; the audit is in the draft.
- **voc-218 حَسَبَ is carded as "according to"**, which is unconfirmed: the verb حَسَبَ يَحْسُبُ, "to count",
  fits the same vowels and would collide with أَحْصَى (voc-009).
- **The 2026-10-13 vocabulary list (voc-231–291) carries four readings the user hasn't confirmed.** الها was
  read as أَلْهَى, بوصل as يُوصِلُ, يقلق as قَلِقَ يَقْلَقُ, and قوط as قُوت (it could be القُوط, the Goths, or قَطُّ).
  The user answered "looks good" without addressing them.
- **The derived-noun chart is the ism al-ālah chart, drafted as sarf-247 (2026-10-27).** It's mifʿal, mifʿalah and
  mifʿāl with their duals and plurals. It sits in the memorisation draft above. **How Notion images open now:** the
  container can't reach `prod-files-secure.s3.us-west-2.amazonaws.com`. Instead, get a signed URL with
  `notion-get-file-download-urls` and pass it straight to the `web-fetch` agent; the URL lasts five minutes. The
  harness saves the raw bytes under the session's `tool-results/`, and Read shows the PNG. HEIC photos are untested.
- **The relative-pronoun chart (nahw-235) was built by Claude** (2026-10-24). The notes say "memorize the chart
  for asmaa’ al-mawsoolah" but the chart isn't on the page. It's flagged for checking against the class's, above
  all the feminine plural: the card gives اللَّاتِي and اللَّوَاتِي, and some charts add اللَّائِي.
- **The nūn al-tawkīd chart (sarf-219) was built by Claude** from the rules in the notes, on فَتَحَ. The
  notes say "memorize chart" but contain none. It's flagged for checking against the teacher's chart.
- **Ḥadīth 2's matn is deliberately uncarded.** The user doesn't need to memorise it.
- **Ḥadīth 4's matn is saved in `texts/arbaeen_h04.md`** for reference (2026-10-07). The
  user doesn't need to memorise it, so don't card it. They are writing the class notes in
  Notion and will say when to scan. Card the notes then, not the matn. Cards may quote
  the matn where a note needs it.
  **Carded 2026-10-07 (arbh-159–199)**, from the notes plus the English translation, which
  the user asked to have carded as if it were notes. The notes had no translation, so Claude
  wrote one; it is in the same file and the user hasn't checked it. The 9 cards sourced "the
  text in translation" rest on it. Do the same for later ḥadīth unless told otherwise.
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
