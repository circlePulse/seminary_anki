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
