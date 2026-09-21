# Reading Notes and Working Files

---

## 11. Reading class notes

### What the source actually is

The notes are typed in real time while the teacher is speaking. That produces predictable artifacts, and reading them as if they were written prose produces bad cards:

- Fragments and incomplete sentences
- Bullets that assume context from the sentence spoken before them
- Compression that makes a claim incoherent as written (see the conditional in §1)
- Transliteration and spelling drift
- One-off lines that belong to no surrounding thought — transcription noise

### Interpretation rules

1. **Read for what was meant, not what was typed.** Reconstruct the proposition, then check that the reconstruction is coherent.
2. **Fill mechanical gaps; flag substantive ones.** A mechanical gap is one where the missing content is uncontested — a truncated term, a dropped article, a definition every text gives identically. A substantive gap is one where filling it means choosing among positions that scholars actually differ on, or where more than one reconstruction fits the words. **Mechanical gaps get filled silently. Substantive gaps become questions.**
3. **Never invent a criterion.** Reconstructing labels is safe; reconstructing the basis of a division is not, because a wrong criterion is invisible and generative — every downstream placement inherits the error.
4. **Outliers go to the Omissions log, not the bin.** A line that fits nothing around it is probably an artifact. It's still logged with the reason "doesn't fit surrounding context — likely transcription noise," so it can be overruled in ten seconds (§3).
5. **Cross-check terminology against standard usage** — especially roots and transliterations (§1, §10).

### Inline agent notes

Source material may carry meta-instructions addressed to the model:

```
{{ CLAUDE: context only, no cards from this paragraph }}
{{ CLAUDE: bidirectional for every term in this list }}
{{ CLAUDE: this contradicts last week — flag it, don't reconcile it }}
```

These are **instructions, never content.** They are obeyed as guidance and never become cards. They also override defaults in this document — if a note says context only, that paragraph is Tier 3 with the note itself as the logged reason.

### Recurring note patterns

| Pattern in notes | Usually yields |
|---|---|
| `Term: definition` | Bidirectional note (§6) |
| `X is divided into A and B` | Spine note + criterion card (§7) — **the criterion is usually missing** |
| `Word — root — derived forms` | Vocabulary paradigm + gloss (§8) |
| `[Scholar]: [opinion]` | Tier 2 unless the opinion is the taught position |
| `we'll come back to this` | Forward-reference log (§13), not a card |
| A list with no distinguishing features per item | One enumeration card, or nothing (§6) |

---

---

## 13. Working files

Three files persist across sessions. They are the state of the system; a session that doesn't update them has lost work.

### The draft file — `draft_{COURSE}_{topic}.md`

```markdown
# Draft — HDT-201, lecture of 2026-09-03
Source: lecture-notes-sep03.pdf
Status: awaiting review

## Questions — blocking
1. Line 14: "meaning is assigned" — assigned by whom, the language or the speaker?
   Two reconstructions fit; the answer changes the criterion card.

## Cards
| # | Tier | Type | Front / Text | Back | Tags |
|---|------|------|--------------|------|------|
| 1 | 1 | Bidir | لَفْظ | any sound produced by a human | mantiq, terminology |
| 2 | 1 | Cloze | اللَّفْظ is either {{c1::مَوْضُوع}} or {{c2::مُهْمَل}} | — | mantiq, spine |
| 3 | 2 | Basic | Who first framed this division? | — | mantiq, tier2 |

## Omissions
- "as we discussed last term" — lecture-flow artifact
- Restatement of card 1 at line 22 — duplicate

## Notes on decisions
- Card 2 kept as one note per spine convention; will be edited when مُفْرَد is subdivided.
```

The Tier column is not decoration — it drives whether the note ships suspended.

### The gloss index — `gloss-index.md`

**Collection-wide, not per course.** Collisions cross course boundaries: a term from ḥadīth terminology and a term from manṭiq can share "knowledge" just as easily as two terms in the same lecture.

```markdown
| English gloss | Term | Course | Disambiguator on the card |
|---|---|---|---|
| knowledge | عِلْم | MNT-101 | established body of what is known |
| knowledge | مَعْرِفَة | MNT-101 | acquaintance with a particular thing |
| ability | قُدْرَة | AQD-101 | — (unique so far) |
```

Checked before every vocabulary note is written. When a row collides, **both** cards get edited and both disambiguators recorded (§8).

### The forward-reference log — `forward-refs.md`

```markdown
| Date promised | What was deferred | Belongs to | Status |
|---|---|---|---|
| 2026-09-03 | subdivisions of مُفْرَد | spine: لَفْظ tree | open |
| 2026-08-27 | conditions of tawātur | spine: ḥadīth by transmission | resolved 09-03 |
```

Its one job: when the deferred material finally arrives, tell you **which existing note to edit** rather than creating a parallel one.

---

---

## The generation input — `cards.json`

Written only after approval, transcribed from the approved draft file. `expected_count` must match the draft's card count; the script hard-fails if it doesn't, which is what catches transcription drift between the reviewed table and the generated deck.

```json
{
  "course": "MNT-101",
  "topic": "lafz-division",
  "session": "sep03",
  "source": "lecture notes 2026-09-03",
  "expected_count": 6,
  "cards": [
    {"type": "bidir", "tier": 1,
     "term": "لَفْظ",
     "meaning": "any sound produced by a human",
     "tags": ["mantiq", "terminology"]},

    {"type": "cloze", "tier": 1,
     "text": "اللَّفْظ is either {{c1::مَوْضُوع::the assigned one}} or {{c2::مُهْمَل::the neglected one}}.",
     "extra": "",
     "tags": ["mantiq", "spine"]},

    {"type": "basic", "tier": 2,
     "front": "On what basis is لَفْظ divided?",
     "back": "Whether a meaning has been assigned to it",
     "tags": ["mantiq", "criterion"]}
  ]
}
```

Fields by type: `basic` needs `front` + `back`; `bidir` needs `term` + `meaning`; `cloze` needs `text` (+ optional `extra`). Course and session tags and the `Source` value are applied to every note automatically; a per-card `"source"` overrides the file-level one.

Then:

```bash
pip install genanki --break-system-packages
python3 scripts/generate_deck.py cards.json -o /mnt/user-data/outputs
```
