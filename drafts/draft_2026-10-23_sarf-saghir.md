# Draft — ṣarf ṣaghīr cloze: the sample (1 note, 8 cards)

Status: **sample, awaiting approval.** Nothing is in the deck yet; the id sarf-220 is provisional.

Source: the pattern the user sent on 2026-10-23, on صَرَّفَ (ṣarrafa). The generator is
`drafts/sarf_saghir_template.py`: `saghir()` takes the eleven forms and builds the table.

## Design

- **Table:** three rows, as in the pattern: the active line, the passive line, then amr, nahy and ẓarf. It reads
  right to left (`<table dir="rtl">`, cells `td.arabic`).
- **Greyed words:** فَهُوَ (fa-huwa), the وَ (wa) before the passive māḍī, الأَمْرُ مِنْهُ (al-amru minhu),
  وَالنَّهْيُ عَنْهُ (wa-l-nahyu ʿanhu) and وَالظَّرْفُ مِنْهُ (wa-l-ẓarfu minhu). They use the deck's `--muted` grey,
  the same as transliterations, so they follow light and dark mode.
- **The māḍī stays visible** as the cue. Every other form is its own blank.
- **Shared blanks:** the maṣdar appears twice, so both copies are c2. For a mazīd verb the ẓarf is the ism mafʿūl
  (here مُصَرَّفٌ), so both are c6. A mujarrad verb gets a separate ẓarf blank, c9.
- **Colour fix:** the table carries `style="color: inherit"`. A client that renders without a doctype would
  otherwise draw table text black on the dark theme.
- **Highlight (proposed, not built):** blue on the blank and on the revealed answer. The cloze notetype has no
  `.cloze` style now, so answers aren't highlighted on any cloze card. Adding one changes the notetype CSS.

## Blanks

| Cloze | Form |
|---|---|
| c1 | muḍāriʿ |
| c2 | maṣdar, both copies |
| c3 | ism fāʿil |
| c4 | māḍī majhūl |
| c5 | muḍāriʿ majhūl |
| c6 | ism mafʿūl, and the ẓarf when it's the same word |
| c7 | amr |
| c8 | nahy |
| c9 | ẓarf, for a mujarrad verb |

## The note's text field

```html
<table dir="rtl" style="color: inherit"><tr><td class="arabic">صَرَّفَ</td><td class="arabic">{{c1::يُصَرِّفُ}}</td><td class="arabic">{{c2::تَصْرِيفًا}}</td><td class="arabic"><span style="color: var(--muted)">فَهُوَ</span> {{c3::مُصَرِّفٌ}}</td></tr>
<tr><td class="arabic"><span style="color: var(--muted)">وَ</span>{{c4::صُرِّفَ}}</td><td class="arabic">{{c5::يُصَرَّفُ}}</td><td class="arabic">{{c2::تَصْرِيفًا}}</td><td class="arabic"><span style="color: var(--muted)">فَهُوَ</span> {{c6::مُصَرَّفٌ}}</td></tr>
<tr><td class="arabic"><span style="color: var(--muted)">الأَمْرُ مِنْهُ</span> {{c7::صَرِّفْ}}</td><td class="arabic"><span style="color: var(--muted)">وَالنَّهْيُ عَنْهُ</span> {{c8::لَا تُصَرِّفْ}}</td><td class="arabic" colspan=2><span style="color: var(--muted)">وَالظَّرْفُ مِنْهُ</span> {{c6::مُصَرَّفٌ}}</td></tr>
</table>
```
