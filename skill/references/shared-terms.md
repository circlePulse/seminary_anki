# Shared Terms Across Sciences

A term that appears in two sciences with different senses is the worst kind of collision, because both cards look correct in isolation. `مُفْرَد` means *a single word* in نَحْو and *singular* in صَرْف — the same front, two right answers, and no way to tell which is being asked.

## The rule

**Any card whose subject term appears in this registry carries a science label.** The generator renders it from a `"science"` key on the card:

```json
{"type": "basic", "id": "nahw-023", "science": "نَحْو",
 "front": "What is a مُفْرَد?", "back": "A single word (= كَلِمَة)"}
```

Label the card when the shared term is **what the card is about** — the thing defined, asked for, or produced. Do not label cards that merely mention it in passing; if every card carries a label, the label stops signalling anything.

For bidirectional notes the label goes on both fields, since either can be the front.

## Both sides get fixed

When a collision is discovered, the card that was written first is *also* wrong now — it was unambiguous only while it was alone. Edit both, add the term to the registry, and regenerate both decks. This is the same rule as the gloss index (`card-design.md` §8), applied to Arabic terms rather than English glosses.

## Registry

| Term | Science | Sense | Status |
|---|---|---|---|
| مُفْرَد | نَحْو | a single word (= كَلِمَة) | labelled |
| مُفْرَد | صَرْف | singular (number) | labelled |
| فِعْل | نَحْو | one of the three kinds of كَلِمَة — a word with tense | labelled |
| فِعْل | صَرْف | the verbal element of a conjugated form, as against the ضَمِير | labelled |
| صَرْف | نَحْو | defined in §1.1 as one of the three sciences | intentional duplicate, both decks |
| مَاضِي | نَحْو / صَرْف | same sense in both — no conflict | watch |
| مَصْدَر | نَحْو / فِقْه | the grammar sense, used inside a fiqh lesson (مَذْهَب is a ظَرْف مَكَانِي or a مَصْدَر) — same meaning, no conflict yet | watch |

## Watch list — collisions that have not landed yet

These will collide as the courses progress. Add the label at the moment the second sense is taught, and go back and label the first.

- **حَرْف** — نَحْو: a particle (word class). صَرْف: a letter of the alphabet. This one is certain to come up.
- **مَصْدَر** — نَحْو: the "root ism" from which words derive. صَرْف: the verbal noun, fourth principal part.
- **تَامّ / نَاقِص** — نَحْو: complete vs. incomplete compound. صَرْف: complete vs. defective verb.
- **اِسْم** — نَحْو: word class. صَرْف: اسم فاعل, اسم مفعول and the other derived nouns.
- **جَمْع** — صَرْف: plural. Also appears in ḥadīth terminology in other senses.
- **عِلْم** — فِقْه: "knowledge" in the technical definition. Will collide with the English gloss of مَعْرِفَة if that is ever carded (see the gloss index in `card-design.md` §8).
- **جَامِع** — فِقْه/method: a sound definition is *comprehensive*. Also the name of a ḥadīth-collection genre (الجامع الصحيح).
