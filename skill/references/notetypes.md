# Notetypes, IDs, and Styling

---

## 14. Notetypes and IDs

### The "Basic++++++++" problem

Anki identifies notetypes by **ID**, not by name. Import a notetype whose ID isn't in the collection but whose name is, and Anki keeps both and appends a `+`. Do that weekly for a year and you get `Basic++++++++`, with your notes scattered across nine notetypes that can't be styled, searched, or repaired as a group.

Two causes, both in the generation script:

1. **`random.randrange()` at runtime.** A fresh model ID on every run means every single import mints a new notetype. This is the main culprit — and it's in the current skill's code sample.
2. **Naming a custom notetype `Basic`.** Anki ships a stock `Basic` with a fixed ID that will never match yours, so the collision is guaranteed on the very first import.

### The rules

- **Three notetypes for the entire collection, not per course.** `Seminary Basic`, `Seminary Bidirectional`, `Seminary Cloze` — plus Anki's built-in Image Occlusion where a diagram is involved. That is the whole inventory, across every course, for all of seminary. Vocabulary needs no notetype of its own: §8 builds it from Cloze (paradigm) plus Bidirectional (gloss).
- **Pin every model ID as a constant in a registry file** committed alongside the skill. Nothing is generated at runtime, ever.

  ```python
  # ids.py — never regenerate these
  MODEL_BASIC = 1607392319
  MODEL_BIDIR = 1607392320
  MODEL_CLOZE = 1607392321

  STAGING_DECK_ID   = 1607392330
  STAGING_DECK_NAME = "Seminary::_Inbox"
  ```

  **Deck IDs are deliberately not a registry.** Everything generates into one staging deck and gets moved by hand in Anki desktop (§16). One pinned staging ID is all that's needed.

- **Prefix names so they can never collide with stock notetypes.** `Seminary Basic`, not `Basic`.
- **CSS and template changes are safe to re-ship** under the same ID — that's how you push a styling fix to every existing card at once.
- **Field additions or removals are not.** Changing the field list of an ID that already exists in the collection risks remapping existing notes. Make field changes in the Anki UI first, then mirror them into the script, keeping the ID.
- **Verify after the first import of each session.** Tools → Manage Note Types; if anything is suffixed, an ID drifted and it should be fixed before more notes land on the wrong type.
- **Repairing existing damage:** Change Notetype to consolidate `Basic+`, `Basic++`, … back onto the canonical one, then delete the emptied types. Do it once, then pin the IDs so it can't recur.

### One-time migration, before any deck is generated

Moving cards between decks by hand does not move them between **notetypes**. If year-one notes sit on some `Basic+++` and the new registry invents fresh IDs, year one is stranded there permanently — it will never receive a styling fix and can never be searched or repaired as one group.

So the registry does not get invented. It gets **adopted**:

1. Tools → Manage Note Types. List what a year of runtime-generated IDs actually produced.
2. Consolidate the duplicates onto one notetype per role with Change Notetype, checking the field mapping each time.
3. Delete the emptied notetypes.
4. Read the surviving IDs out of the collection (Manage Note Types, or the database) and write **those** into `ids.py`.

Step 4 is the one that matters. Adopting the surviving IDs means every note ever made — year one and year two — lives on the same three notetypes from then on.

---

---

## 15. Styling and dark mode

### Minimal by default

**A card is a memory test, not a design artifact.** Every style rule is a thing that can break on one of the four clients you review on, and none of it improves recall. Styling that exists to look nice is a liability.

**Style only what changes legibility or meaning:**

- Arabic font stack, size, and line-height — Arabic at English body size with English line-height is genuinely hard to read, and tashkīl gets clipped
- `direction` — `ltr` on `.card`, `rtl` on Arabic spans and table cells
- Separation between question and answer (Anki's `<hr id="answer">` already does this)
- List alignment — left-aligned lists inside a centered card
- Table borders and cell padding, where tables are actually used

**Don't style:** colored headings, boxed callouts, background tints, border-radius, shadows, gradients, custom web fonts, animations, per-field color coding. If a card needs visual hierarchy to be readable, it's carrying too much content — fix the card, not the CSS.

### Dark mode is mandatory — and the cheapest way to get it is fewer colors

The reason dark mode breaks is hardcoded colors. So the first move is not "write dark overrides," it's **set fewer colors in the first place.**

**Don't set `color` or `background-color` on `.card` at all.** Anki supplies both, correctly, in whichever theme the user is in. Overriding them creates the exact problem the overrides then have to fix. AnkiDroid also inverts colors in night mode when the CSS doesn't specify them, so hardcoding a light-mode color is worse than setting none.

Where a color is genuinely load-bearing (transliteration greyed out, table header shading), define it **once as a custom property** and override only the variables — not the whole ruleset.

```css
.card {
  /* the only colours declared anywhere */
  --muted: #666;
  --rule: #ccc;
  --header-bg: #e8e8e8;

  direction: ltr;              /* required: prevents BiDi scrambling */
  font-family: 'Scheherazade New', 'Amiri', 'Traditional Arabic',
               'Geeza Pro', Arial, sans-serif;
  font-size: 20px;
  line-height: 1.6;
  text-align: center;
  /* no color / background-color — Anki handles these */
}

/* Arabic needs its own size and leading; tashkīl clips at English line-height */
.arabic {
  direction: rtl;
  font-size: 28px;
  line-height: 1.9;
}

.transliteration { color: var(--muted); font-style: italic; font-size: 0.85em; }

ul, ol { text-align: left; display: inline-block; }

table { border-collapse: collapse; margin: 10px auto; }
th, td { border: 1px solid var(--rule); padding: 8px 12px; text-align: center; }
th { background-color: var(--header-bg); }
td.arabic, th.arabic { direction: rtl; font-size: 22px; line-height: 1.9; }

/* Desktop + AnkiMobile use .nightMode; AnkiDroid uses .card.night_mode (no space) */
.nightMode, .card.night_mode {
  --muted: #aaa;
  --rule: #555;
  --header-bg: #333;
}
```

**Font stack, in priority order:** Scheherazade New and Amiri are the two worth installing — both are proper Naskh with reliable tashkīl positioning. Traditional Arabic (Windows) and Geeza Pro (macOS/iOS) are the built-in fallbacks. Arial is last resort and renders vowel marks poorly.

**Markup:** wrap Arabic in `<span class="arabic">` inside mixed sentences, `<div class="arabic">` for full-Arabic content. The LTR base direction on `.card` plus RTL on those spans is what keeps punctuation from jumping.

Three variables, one override block. Compare to declaring the full palette twice or three times, where every future color change means editing three places and one of them silently drifts.

**On `@media (prefers-color-scheme: dark)`:** it follows the *operating system*, not Anki's theme setting. If the OS is dark and Anki is set to light, the media query fires and you get dark cards inside a light reviewer. The class hooks above cover every client, so the media query is redundant at best. Leave it out unless you've confirmed a specific client needs it.

**Never rely on colour to carry meaning.** Anything that must be distinguishable needs a non-colour cue too — italics, a label, position.

---
