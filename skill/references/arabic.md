# Arabic Content Rules

CSS, font stack, and RTL markup live in `notetypes.md`. This file is about content.

---

## 10. Arabic-specific

### Arabic is the card, transliteration is a gloss

**Every Arabic term appears in Arabic, fully vowelized, everywhere it appears.** Not "where reasonable" — everywhere. Transliteration follows in parentheses; it never stands alone and never substitutes.

This is not only a rule about card fronts. It applies to:

- Card fronts and backs, both directions
- Cloze text, including spine, contrast, and placement notes (§7)
- Vocabulary paradigms — every principal part vowelized, not just the citation form
- Disambiguating glosses (§8) — `root ق‑د‑ر`, not `root q-d-r`
- Terms appearing inside an English sentence — `the ḥadīth is مُرْسَل (mursal) because…`

Bare transliteration in any of these is the failure mode that lets you recognise a word you cannot actually read. Full tashkīl in particular is what makes the difference between recognising a shape and knowing the word: عِلْم and عَلَم are the same skeleton.
### Other rules

- **Decide recognition vs. production per card.** Recognizing وَاجِب is a different skill from writing it from memory, fully vowelized. Only demand production where you're actually accountable for producing it — otherwise you've made a handwriting card and don't know it.
- **For matn memorization, cloze the Arabic.** "Recite the ḥadīth about intentions" is one enormous all-or-nothing card. Progressive clozes over the same text give partial credit and diagnose which clause is weak.
- **Never make transliteration → Arabic a card.** Transliteration isn't a thing you need to produce; the association runs Arabic → meaning and meaning → Arabic.
- **Verify transliteration against the root at decomposition time.** *muhmal* vs. *mahmal* is the kind of drift that propagates silently through a whole cluster (§1).
### Isolate every inline Arabic run — this is not optional

Arabic dropped bare into an English sentence renders wrong. The characters around
it — punctuation, parentheses, em-dashes, digits, the `::` and `}}` of a cloze — are
**neutral** under the Unicode bidirectional algorithm: they take their direction from
whatever strong characters sit next to them. Next to an Arabic run inside an English
line, they resolve RTL and jump to the wrong side. The usual symptom is a question
mark, period, or closing bracket appearing at the left edge of the Arabic instead of
after it, or a comma-separated list of terms reordering itself.

**Every Arabic run inside a line that also contains Latin text gets wrapped:**

```html
What is a <bdi>مُفْرَد</bdi>?
<bdi>لَفْظٌ مَوْضُوعٌ مُفْرَدٌ</bdi> — an utterance with an assigned meaning
```

`<bdi>` exists for this. `<span class="ar">` is equivalent; both carry
`unicode-bidi: isolate`.

**`direction: rtl` on its own is not enough on an inline element.** Without
`unicode-bidi: isolate` (or `embed`), the `direction` property has no effect on how
an inline run orders against its surroundings. A `.arabic` span with only
`direction: rtl` does nothing. This was wrong in the templates for the first month of
this project and produced roughly 530 broken fields.

**Cloze: wrap the Arabic run itself, never the braces.**

```html
اللَّفْظ is either {{c1::<bdi>مَوْضُوع</bdi>}} or {{c2::<bdi>مُهْمَل</bdi>}}
```

Wrapping the braces — `<bdi>{{c1::مَوْضُوع}}</bdi>` — looks tidier and is wrong. Anki
replaces the deletion with `[...]`, leaving `<bdi>[...]</bdi>`. Square brackets are
**mirrored** characters: rendered in an RTL run they come out as `]...[`. Wrapping the
run itself leaves the placeholder in the surrounding LTR context where it belongs.

For the same reason, never force `direction: rtl` on `<bdi>` in CSS. The element
defaults to `dir="auto"`, which resolves from the first strong character in its
content — that is the entire point of it. Set `direction` explicitly only on a class
like `.ar` used on known-Arabic content.

**A line that is entirely Arabic goes in one `<div class="arabic">` — never per-run
`<bdi>`.** This covers a whole matn, a vocabulary paradigm, a singular/plural pair, an
Arabic definition with blanks, and a full-Arabic table cell. The card's base direction
is LTR, and isolates inside an LTR line are laid out **left to right**, so
`<bdi>تَحَمَّلَ</bdi> — {{c1::<bdi>يَتَحَمَّلُ</bdi>}} — …` puts the مَاضِي on the
*left*: backwards to a reader of Arabic. 63 vocab cards shipped like this and were
fixed on 2026-10-01. A bare all-Arabic line without any wrapper reads in the right
order until a blank sits at either end. That blank then drifts to the wrong side,
because a trailing or leading `[...]` resolves against the LTR card, not the Arabic.

```html
<div class="arabic">نَصَرَ — {{c1::يَنْصُرُ}} — {{c2::اُنْصُرْ}} — {{c3::نَصْر}}</div>
<div class="arabic">{{c2::كِتَاب}} (مُفْرَد) — {{c1::كُتُب}} (جَمْع)</div>
```

The مَاضِي (or the مُفْرَد) is written first and renders rightmost. `<bdi>` is only
for an Arabic run inside a line that also has Latin text. `generate_deck.py` warns
(`RTL — …`) when an all-Arabic field sits outside the block.

- Rendering (BiDi, `direction: ltr`, dark mode, fonts) is a template concern — keep it out of card content and solve it once in the CSS. See §15.

### Transliteration convention

Academic transliteration with macrons and dots, always in parentheses after the Arabic, never alone.

| Arabic | Translit. | Arabic | Translit. | Arabic | Translit. |
|---|---|---|---|---|---|
| ا | ā | ذ | dh | ط | ṭ |
| ء | ʾ | ص | ṣ | ظ | ẓ |
| ع | ʿ | ض | ḍ | غ | gh |
| ح | ḥ | ش | sh | ث | th |
| خ | kh | | | | |

Long vowels: ā, ī, ū. Tāʾ marbūṭa: `-ah` in pause form.

---
