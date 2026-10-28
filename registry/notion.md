# Notion map

Where the class notes live and how they are laid out. The page ids are stable,
so fetch a course page by its id (in `courses.json` as `notion_id`) instead of
searching by title. Mapped 2026-09-30.

## Dashboards

Both are top-level private pages, and both are in favourites.

| Page | Id |
|---|---|
| 🕋 IOK Seminary Dashboard | `262737ec4b8a80979e4afc3d10fb1239` |
| UCI Dashboard | `3a5737ec4b8a8043ad9ccaf948179443` |

The course pages sit inside column and toggle blocks on each dashboard, so the
ancestor path shows several untitled parents. Ignore them.

## IOK Seminary — Year 2 Classes

| Page | Id | Deck |
|---|---|---|
| IOK Arabic | `3cd737ec4b8a80e8b1f0e33ad63d1837` | ARB-201 → `nahw`, `sarf` |
| Arba’in/Quduri | `3cd737ec4b8a80b7839fe066e0ed33c9` | HDT-201 → `arbaeen*`, `quduri` |
| Riyadh | `3cd737ec4b8a80f5896fd2e0daaead1f` | HDT-202 → `riyad` |
| Tazkiyah | `3df737ec4b8a8043893cd7bb8daf6bc1` | none |
| Durus/Safwah/Qasas | `3cd737ec4b8a80c89cd4e026c60b838c` | none: the page holds only reading etiquette, no notes |

**IOK Arabic** has two top-level toggles. *Tasheel Al-Nahw* goes chapter → section
(`Section 1.2 — ‘alkalimatu`), and *Sarf* is a flat run of topics (verbs, person,
tenses, wazn, abwāb, passive, iʿrāb, negation). The conjugation tables are
embedded HEIC photos, not text.

**Arba’in/Quduri** is one long page (~60k characters, too large for a single
fetch response; save it and read it in slices). It has these top-level toggles:
*Texts*, *Hadith, Sunnah, intro to Arba’in*, *Imam Al-Nawawi*,
*Arba’in* (Introduction, then `Hadith #1`, `#2`, `#3` …), and *Qudoori* (intro,
bio, a legal-values tangent, then `Kitaabu Al-Tahaaratu` → wuḍūʾ, ghusl, water).
Each ḥadīth section opens with its narrator's biography, and Ḥadīth 2 opens with
a vocab list.

**Riyadh** points to Arbaʿīn for al-Nawawī's biography. It has an intro, then one
toggle per chapter. As of 2026-10-14 the only chapter is repentance; the empty Kitāb al-Jihād toggle is gone.
The vocabulary lists the user pastes into chat come from this class's reading (Bāb al-Ṣabr, Bāb al-Ṣidq).

**Tazkiyah** covers *Bidāyah* → *Tongue* (lying, breaking promises, backbiting).
It uses bullets, not toggles.

**Year 1 is out of scope.** The archive under *Archive* on the dashboard (QRN-101,
ARB 101/102, JRP 101, SPR 101, HDT 101, CRD 101, SRH-101) is not to be scanned or
carded. The user said so on 2026-09-30.

## UCI — Y1 Q1 Courses

| Page | Id | Deck |
|---|---|---|
| World Religions II | `3a5737ec4b8a80b4a050ff5e3082d024` | RELSTD-5B → `wrel` |
| Python Programming and Libraries (Accelerated) | `3a5737ec4b8a80568691d464ac953688` | ICS-H32 → `pyth` |
| Calculus II (info block says Math 1B, Pre-Calculus II) | `3a5737ec4b8a80508bc1d5409415cb2a` | none: a *Review* section of formulas since 10-08, on hold at the user's word (2026-10-14) |
| UCI General | `3a5737ec4b8a807580c5faf8babade0c` | not course notes |

Every UCI course page opens with *Info* (section codes, times, links) and *Todos*
before the notes.

**World Religions II** is organised by **date**. It has one heading per class
(`# 09/24/26`), each holding `## Class Lecture` and `## Readings`, with one
`###` per reading. New material is a new date heading, and the date gives the
session tag.

**Python** has a single `# Notes` toggle with one toggle per topic (Expressions,
Variables, Strings, … Loops) and no dates. New material is appended as new topic
toggles at the bottom, so "what's new" means comparing topics against the deck.

## Conventions across all pages

- **One proposition per toggle.** Nesting is subordination: a child toggle
  qualifies, exemplifies or subdivides its parent. That structure is the first
  decomposition pass, done for you.
- **`{{ CLAUDE NOTE: … }}` markers** are the user's instructions. `START HERE`
  marks where the previous carding pass stopped. Old markers are not always
  removed, so a page can hold more than one. Take the latest one that the deck
  does not already cover, and check against the deck before trusting any marker.
- **Transcription slips are common** (*prompt injection* for code injection,
  *kebob_case* for snake_case). Corrections go on the cards, not in Notion; the
  notes still carry the originals. Edit Notion only when the user asks, as they did
  for the swapped abortion stages on 2026-10-07. Make the smallest exact edit, then
  re-fetch to check it.
- **Notes are sometimes mid-edit.** A trailing toggle can stop mid-word (the
  Qudūrī water section once ended at `Ri`, and an hour later it ran to a full
  classification). Re-fetch right before drafting, card up to the last complete
  proposition, and flag the rest.
- **Images** (HEIC photos of tables, screenshots) carry content the text does
  not. Say when a section's substance is only in an image. Screenshots can be read: see
  "How Notion images open now" in HANDOFF (signed URL, then the web-fetch agent).

## Uncarded as of 2026-09-30 (after the evening batch)

- Tazkiyah: all of it. There is no course entry or deck yet. The user put it on hold on 2026-10-14
  ("don't do … tazkiya yet"), along with Calculus II.
- Buddhism "spread along …" (World Religions 09/29) breaks off in the notes. It gets
  carded once the user supplies the rest.

Carded on 2026-10-28, later: the rest of Arbaʿīn Ḥadīth 8 (arbh-319–326), which the user said is finished.

Carded on 2026-10-28: the vocabulary list supplied that day (voc-472–500), tagged `riyad-istiqamah` by inference
(the user approved the tag). تغشاني was read as تَغَشَّانِي.

Carded on 2026-10-28: Qudūrī ḥayḍ, istiḥāḍah, nifās and the maʿdhūr (qud-306–331), from the 10-27 notes. On the
cards only: less than a verse is given as al-Ṭaḥāwī's view against the relied-upon one; the blank ruling of
istiḥāḍah is filled from Qudūrī (a constant nosebleed); the gap of purity is within the days of ḥayḍ.

Carded on 2026-10-28: Arbaʿīn Ḥadīth 8 (arbh-303–318) and its vocab list (voc-464–471), up to the notes'
"(to be continued)". One softening, on the cards only: "every time" Allah mentions īmān with action became
"again and again".

Carded on 2026-10-28: Ṣarf, the rest of the mazīd abwāb and the rubāʿī (sarf-248–323), from the 10-27 notes. Two
corrections are on the cards only: the dropped tāʾ (tataqabbalu, not yataqabbalu) and the reason for izzammala's
hamzat al-waṣl. The ṣarf ṣaghīr examples are Claude's, the traditional set.

Carded on 2026-10-27, later: the memorisation cards (riyad-011–030 and sarf-247), for both Riyāḍ to-dos and the
ism al-ālah chart. The audit of every memorisation note is in `drafts/draft_2026-10-27_memorisation.md`.

Carded on 2026-10-27: World Religions 10/27, Buddhism (wrel-285–303). Corrections on the cards only: the
Eightfold Path has its standard eight (the notes had right thought and right intent as two, and no right
mindfulness); nirvana is not glossed "self-annihilation". "Heaven = Sutras" was left uncarded as unclear.
Riyāḍ's memorisation to-do now adds ḥadīth 82's duʿāʾ. Nothing else had changed.

Carded on 2026-10-24: IOK Arabic, the new toggles at the end of Tasheel ch. 2 (nahw-228–238). They cover
nūn al-wiqāyah, ḍamīr al-shaʾn and al-qiṣṣah, ḍamīr al-faṣl, and the relative pronouns. The CLAUDE note "memorize
the chart for asmaa’ al-mawsoolah" got a chart table built by Claude (nahw-235), since the page has none.
Corrections on the cards only: nūn al-wiqāyah carries a kasrah, not a sukūn; "Dameer al-Qasli" is ḍamīr al-faṣl.

Carded on 2026-10-23, from a scan of every page:
- **Arbaʿīn:** the rest of Ḥadīth 6's lessons (arbh-267–270), and Ḥadīth 7 in full (arbh-271–302): Tamīm al-Dārī,
  naṣīḥah, and the five relationships. Its matn and Claude's translation are in `texts/arbaeen_h07.md`.
- **Qudūrī:** wiping over footgear (qud-286–305).
- **IOK Arabic, Ṣarf:** the new *thulathiy mazeed feeh* toggle (sarf-220–246). Its CLAUDE note asked for two-way
  pattern cards for each bāb, with the maṣdar named and one question per card, and for ṣarf ṣaghīr cloze tables
  "based on the image I gave". Bāb al-tafʿīl and bāb al-mufāʿalah each got both. Mufāʿalah has both maṣdars, and
  its model verb is قَاتَلَ. sarf-105 now says mujarrad means "stripped".
- **Python:** the *Example project notes* toggle (pyth-214–217).

Unchanged: World Religions (last edited 10-22), Riyāḍ, Durūs, Tazkiyah and Calculus II.

Carded on 2026-10-22, from a scan of every page:
- **Arbaʿīn Ḥadīth 6** (arbh-247–266), and the particle أَلَا (voc-446, `h06`). The "DON'T START YET" note over it
  had been left by mistake, the user said. Claude removed it from the page at their request.
- **Qudūrī tayammum additions** (qud-280–285). qud-269 was edited: the materials rule excludes plants and wood, and
  is Abū Ḥanīfah's and Muḥammad's view.
- **World Religions** 10/15 (in class, and the Daodejing reading) and 10/20 (wrel-192–284). wrel-190 now says Zhu Xi
  "arguably" founded Neo-Confucianism, per the 10/15 notes.
- **Python** namedtuple (under Tuple), then Recursion, Set and Dictionaries (pyth-193–213).

Corrections on the cards only:
- **Arbaʿīn:** al-Nuʿmān ibn Bashīr's death, "56" in the notes, is 64 or 65 AH.
- **World Religions:** Zhu Xi did take a view on human nature, Mengzi's; Daodejing 42 has a step the notes skip;
  the Enigmatic Female's gate is the root of Heaven and earth.
- **Python:** "an array of strings" is a list, `del` is a statement, and dictionaries are indexed by key, not only
  by strings.

The other pages had nothing new to card: IOK Arabic and Durūs. Riyāḍ has only a to-do, to memorise ḥadīth 37, 54,
61 and 71 and the second narration of 62; progressive cloze cards were offered. Calculus II and Tazkiyah are on
hold.

Revised in Notion on 2026-10-22, at the user's request ("I was very confused when writing my notes"): IOK Arabic,
Tasheel ch. 2, the iʿrāb toggles. LafDhi had been defined as "state explicitly shown", which is ẓāhir. Now
dhaahir and almuqaddar sit inside LafDhi as its two kinds, and Mahalli is tied to mabniy. A toggle on telling
muqaddar from mahalli was added. The CLAUDE note "add the categories" was replaced by the muqaddar categories. The
old wording is quoted in `drafts/draft_2026-10-22_irab.md`. Carded on 2026-10-23: nahw-226 (how the four kinds fit
together) and nahw-227 (muqaddar or mahalli), with nahw-215 edited to say "whether you can hear it or not".

Carded on 2026-10-14, from a scan of every page the user asked for:
- **IOK Arabic, Tasheel ch. 2, al-muʿrab wa-l-mabnī** (nahw-209–225). The CLAUDE note "add the categories" was
  read as the words whose iʿrāb is مُقَدَّر. The deck's topic is now `tasheel`, so its files are named that way.
- **sarf-135**, corrected: some أَسْمَاء are مَبْنِيّ.
- **World Religions** 10/01, 10/08 (in class, and the Mencius and Xunzi readings) and 10/13 (wrel-111–191). The
  CLAUDE note asked for a definition of Mozi's universal consequentialism.
- **Python** topics after Loops: Functions through Tests (pyth-107–192).

Corrections on the cards only:
- **Naḥw:** "faa'il" for fiʿl; جَزْم "marfoo'".
- **World Religions:** Mengzi "3th" century, and the missing fourth sprout.
- **Python:** a slice's stop defaulting to -1; `.write()` overwriting the file.

The other pages had nothing new: Riyāḍ, Durūs, and Arbaʿīn/Qudūrī apart from Ḥadīth 6's narrator. The old
`START HERE` marker in Qudūrī's nullifiers of wuḍūʾ has been removed by the user.

Carded on 2026-10-14 (last): Arbaʿīn Ḥadīth 5 (arbh-223–246), and its vocab أَحْدَثَ (voc-338–339, `h05`), per the
CLAUDE note in the notes. Ḥadīth 6 carries "CLAUDE NOTE: DON'T START YET".

Carded on 2026-10-14 (later): Qudūrī tayammum (qud-258–271), and the new top-level *Ikhtilaaf* toggle (qud-272–279).
The user put Ikhtilāf in the Qudūrī deck. From al-Qudūrī's text: "about a mile", and Jumuʿah having a
replacement (ẓuhr).

Revised on 2026-10-07 (evening): the Ḥadīth 4 *Lessons* block (arbh-200–221), and eight
clarifications to the Qudūrī water section (qud-224/225/227/228 edited, qud-229–235 new). The user's
abortion notes have the two stages swapped. The user confirmed it, so the cards follow Mufti Muhammad
ibn Adam's fatwa. At the user's request, the two stage headings were then swapped in Notion as well
(2026-10-07), so the page now matches the cards.

Carded on 2026-10-07: Arbaʿīn Ḥadīth 4 in full (arbh-159–199), with the narrator, the stages,
the soul, what is written and the example. The translation Claude supplied is carded alongside
the notes. Its matn is saved in `texts/arbaeen_h04.md`.

Carded on 2026-10-09: IOK Arabic. The 10-08 additions to ism mubālagha, tafḍīl, ẓarf and ālah, and the new
topic nūn al-tawkīd (sarf-193–219). The derived-noun singular/dual/plural chart is only a screenshot and
the S3 host is blocked, so it is uncarded; see the HANDOFF pending list. Two corrections are on the cards
only, not in Notion: the alif is added to the feminine *plural*, and the nūn takes a kasrah after an alif.

Carded on 2026-10-08 (later): Qudūrī's three sections after the water diagram — *Assorted points*,
*Rulings of wells*, *ʿassuʾur* — as qud-236–257, and one new Ḥadīth 4 lesson line ("actions are
judged by their end", arbh-222). The notes had no errors this time. Examples and the Abū Ḥanīfah
attribution come from the matn.

Carded on 2026-10-08: IOK Arabic. Kāna and her sisters (nahw-191–208) had been in the notes since
before 2026-10-02 and was missed then. The six new ṣarf topics are the amr and nahy, ism fāʿil and
mafʿūl, ism mubālagha, tafḍīl, ẓarf and ālah (sarf-170–192). Three mistakes in the notes were corrected
in Notion at the user's request:
- after وَ or فَـ, لَام الأَمْر takes a sukūn, not a kasrah;
- اِسْم الظَّرْف's own patterns are only thulāthī; from other verbs it takes the ism mafʿūl's form;
- "harf majzoom laam" became "harf jaazim laam", and kāna's "{name of particle}" became "{name of verb}".

Carded on 2026-10-02: IOK Arabic, the حُرُوف الجَرّ (meanings only, per the user's note),
إِنَّ and her sisters (full list), and §1.6 pronouns with the chart (nahw-146–190). The
chart's `ADD TESTS` note is done. In Notion both ḥarf lists sit under غَيْر عَامِل, but
they are عَامِل, and the cards file them there. The user hasn't asked for the Notion
nesting to be moved.

Carded on 2026-09-30: the Ḥadīth 2 body, the World Religions lecture of 09/29, the
Qudūrī water section, and Riyāḍ's chapter of repentance. For the next pass on any
of these pages, compare against the deck rather than trusting a `START HERE` marker.
