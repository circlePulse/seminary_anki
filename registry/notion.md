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
toggle per chapter (repentance, then Kitāb al-Jihād, which is still empty).

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
| Calculus II (info block says Math 1B, Pre-Calculus II) | `3a5737ec4b8a80508bc1d5409415cb2a` | none: the page has no notes yet |
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
  notes still carry the originals.
- **Notes are sometimes mid-edit.** A trailing toggle can stop mid-word (the
  Qudūrī water section once ended at `Ri`, and an hour later it ran to a full
  classification). Re-fetch right before drafting, card up to the last complete
  proposition, and flag the rest.
- **Images** (HEIC photos of tables, screenshots) carry content the text does
  not. Say when a section's substance is only in an image.

## Uncarded as of 2026-09-30 (after the evening batch)

- Tazkiyah: all of it. There is no course entry or deck yet.
- Buddhism "spread along …" (World Religions 09/29) breaks off in the notes. It gets
  carded once the user supplies the rest.

Carded on 2026-09-30: the Ḥadīth 2 body, the World Religions lecture of 09/29, the
Qudūrī water section, and Riyāḍ's chapter of repentance. For the next pass on any
of these pages, compare against the deck rather than trusting a `START HERE` marker.
