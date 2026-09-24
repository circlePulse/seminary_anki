# Card Design

What cards exist and what shape they take. Section numbers are kept from the source document for cross-referencing.

---

## 1. The generative method: what is the load-bearing point?

This is the primary card-generation method. Everything in §2 validates cards that already exist; this is what determines which cards exist at all.

**Don't read a sentence and ask "what card should I make?" Ask "what claims is this sentence actually making?"** Enumerate the propositions. Each proposition is a candidate card. Atomicity then stops being a rule you enforce after the fact and becomes a property of the method — you can't accidentally bundle two facts if you enumerated them separately to begin with.

### Worked example

Raw note:

> Any sound humans make is lafḍh. If it has meaning, it is called mawḍūʿun (meaningful) or muhmalun (meaningless).

**Decomposition — five propositions, not three:**

1. لَفْظ is the term for any sound produced by a human
2. لَفْظ divides into مَوْضُوع and مُهْمَل
3. **The criterion of division is whether a meaning has been assigned to the utterance**
4. مَوْضُوع = an utterance to which a meaning has been assigned
5. مُهْمَل = an utterance to which no meaning has been assigned

Proposition 3 is the one a card-first reading loses every time. The labels are memorable; the criterion is what lets you place a new term correctly when you meet one, and it is the thing you'll actually be asked to state.

### Decomposition audits the notes

A proposition you cannot state cleanly is a gap to resolve, not a card to write. This example has two:

- **The conditional is incoherent as transcribed.** "If it has meaning, it is called mawḍūʿ *or* muhmal" — a single conditional can't govern both branches. Real-time notes compress; forcing yourself to write the criterion as a standalone proposition exposes the compression.
- **مُهْمَل, not *mahmal*.** The root is ه‑م‑ل, "to neglect" — مُهْمَل is "neglected," i.e. left without an assigned meaning, paired against مَوْضُوع, "placed/assigned." The transliteration drift would have propagated into every downstream card.

Catching this at decomposition costs a minute. Catching it in month seven costs a rewrite of a whole cluster.

### Two passes

**Pass 1 — sentence level.** Decompose each sentence as above. This gets you most of the deck.

**Pass 2 — section level.** Ask the same question of the *relationships between* sentences. This pass is where distinction cards, structural notes (§7), and interference anchors (§9) come from, and it is the one most likely to be skipped.

Pass 1 is sentence-local by construction. It will never surface:

- That this division contrasts with a differently-grounded division taught later
- That a term introduced here gets subdivided three lectures on
- That two criteria taught weeks apart sound alike and will collide

None of those are in any single sentence, and all of them are examinable.

### Where the method stops

Decomposition tells you which propositions exist. It does **not** tell you which card type to use, and it will happily generate near-duplicate fronts if you card each proposition mechanically — see §6, §7 and §8 for the shape they should take.

---

## 2. The three tests

Validators. Every card must pass all three before it goes in the deck.

**1. Atomic.** The answer is one fact. If the back contains two things that could each be a question, it is two cards. (If §1 was done properly this is nearly automatic.)

**2. Standalone.** The card is answerable when it surfaces at random, three months from now, with no memory of the lecture, the notes, or the surrounding cards. No "the second condition," no "as mentioned above," no dangling pronouns, no "(3 of 8)."

**Enforcement:** `generate_deck.py` flags fronts containing a demonstrative that points
at something the front never names — "this ḥadīth", "that ruling", "these sciences".
Every ḥadīth card in a deck fits the front "why is *this* ḥadīth half of knowledge",
which is why it must say *which*. A quotation or a "Complete: …" prompt carries its own
referent and is exempt.

**3. Diagnostic failure.** When you press *Again*, you should know exactly what you didn't know. If a failure could mean four different things, the card is testing four things.

**4. The back carries information the front does not.** If you can produce the answer by re-wording the question, no retrieval happens. "Which ḥadīth commands holding to the Sunnah and the rightly-guided successors?" → "Hold on firmly to my Sunnah and the Sunnah of the rightly-guided Khulafāʾ" is a paraphrase wearing a question mark.

This failure is more dangerous than a leech. A leech announces itself; a giveaway card feels *easy*, gets graded *Good*, earns a long interval, and quietly consumes review time for years while teaching nothing.

It comes from one specific move: taking a bullet and converting it into "what does X say about *[the bullet's own content]*?" Scriptural evidence is the usual victim, because the natural question names the content.

**The fix for a text is a completion prompt, not a description.** Give the opening of the text and ask for the rest:

| Instead of | Write |
|---|---|
| Which ḥadīth names the best speech and the best guidance? | Complete: "The best speech is …, and the best guidance is …" |
| What is the Qurʾānic instruction about what the Prophet ﷺ gives and forbids? | Complete: "Whatever he gives you, …; whatever he forbids you from, …" |
| How does the Qurʾān describe the Prophet's ﷺ character? | Complete: "Indeed, you are upon …" |

`generate_deck.py` flags likely giveaways at build time by lexical overlap. It is a prompt to look, not a verdict — "Which century was the golden age of ḥadīth studies?" → "The 200s, the 3rd century AH" scores high and is fine, because *which* century is exactly the information the front withholds.

---

## 3. Triage: everything is accounted for, nothing vanishes

Every proposition from §1 lands in exactly one of three buckets. All three are **visible in the draft file** before generation.

### Tier 1 — Core

Will need to be produced cold. Generated active.

- Definitions of technical terms (`ḥadīth ḥasan`, `tadlīs`, `ʿillah`, `مَوْضُوع`)
- Criteria of division — the basis on which a category splits
- Matn of aḥādīth you're accountable for, and their narrator
- Classification criteria and the categories they produce
- Rules, conditions, and their exceptions
- Key dates and identities for figures who recur
- Root-word analyses where the root does real explanatory work
- Distinctions between easily confused things (see §9)

### Tier 2 — Secondary

Plausibly asked, plausibly examinable, lower yield. **Generated as real cards**, tagged `tier2`, and delivered suspended — so they exist in the collection, are findable by search, and can be unsuspended in a batch before an exam or when a topic turns out to matter.

- Scholar opinions mentioned once in passing
- Secondary dates and minor biographical detail
- Illustrative examples the teacher used
- Detail that is currently context but could become examinable

This tier is the mechanism that makes the whole approach safe. It costs nothing in daily review load and eliminates the "Claude decided this didn't matter" failure entirely. **When in doubt, tier 2 — never drop.**

### Tier 3 — Not a card, but logged

The only things that don't become cards, and each one is listed by name in an **Omissions** section at the bottom of the draft file with a one-line reason, so you can overrule it in ten seconds.

- Lecture-flow artifacts: "we'll come back to this," "as I said last week," transcription noise
- Exact restatements of a fact already carded
- Material you don't yet understand — **flagged for clarification, not discarded.** Cards are a retention tool, not a comprehension tool; memorizing a definition you can't explain produces a permanent leech and unusable knowledge. This goes back to you as a question, and becomes a card once the meaning is settled.

Nothing else is auto-dropped. "It seemed minor" is not a Tier 3 reason — that's Tier 2.

> **Note:** "we'll come back to this" is Tier 3 as a *card*, but it goes into the forward-reference log (§13) rather than the bin.

### Where economy actually belongs

The way a 40-fact lecture becomes 240 cards is not coverage. It's **multiplication** — generating basic, reverse, application, distinction, context, and enumeration variants of the same fact by default. Six cards testing one fact means six failures to diagnose, six chances at interference, and six slots in the queue for one piece of knowledge.

So: **cover every proposition; write the fewest cards that test it.** Add a second angle when the second angle is itself something you must know — a distinction you'll be asked to draw, an application you'll be asked to make — not as a matter of routine.

That is the whole economy argument. It never justifies leaving a concept out.

### Managing load without cutting coverage

- **Throttle new cards per day per course** rather than shrinking the deck. A complete deck introduced at 15 new cards/day is sustainable; the same deck dumped in at once is not.
- **Ship Tier 2 suspended.** Zero cost until you want it.
- **Tag by session date** so you can unsuspend or cram a specific week before a quiz.
- If the queue is genuinely outrunning what you can sustain, the first thing to cut is redundant angles and leeches — not facts.

---

## 4. Writing the front

- **Ask for one thing, and make the expected form obvious.** "What is X?" is fine for a definition. "Tell me about X" is not a card.
- **Front-load the distinguishing content.** The front must contain whatever makes *this* item different from its siblings.
- **Never encode list position.** "(2 of 6)", "the third sign", "Reward #4" — the deck is shuffled; position is meaningless. If an item has no distinguishing feature other than its position, it doesn't deserve its own card.
  - *Exception:* genuinely ordered sequences where the order is the thing being memorized (steps of wuḍūʾ, stages of a chain).
- **Add a scope cue when the same question could be asked of many things.** `[HDT] Ḥadīth classification —` prefixes are cheap and kill a lot of ambiguity.
- **Rewrite in your own words.** Real-time lecture notes are fragments. Copying a fragment onto a card front preserves its ambiguity forever.

---

## 5. Writing the back

- **One fact.** Repeat of test 1, because it's the rule most often broken.
- **Short enough to verify at a glance.** If you have to read a paragraph to decide whether you got it right, you'll grade yourself inconsistently and the scheduler's data becomes noise.
- **No supporting explanation on the back of the answer.** If context matters, put it in a separate `Extra`/`Notes` field that renders below the answer — it's there when you want it and it doesn't inflate the thing you're grading.
- **Answers you must produce verbatim get a verbatim card. Everything else gets the gist.** Decide this per card and make the front say which.

---

## 6. Card type selection

| Content | Use | Why |
|---|---|---|
| Term ↔ meaning, standing alone | **Bidirectional** | Genuine two-way association; needs no surrounding context |
| Fact about a person/event | **Basic, one direction only** | Reversing a fact ("who died in 256 AH?") is ambiguous and useless |
| Division trees, criteria, placement | **Cloze** (see §7) | The context *is* the content |
| Matn, formulas, fixed phrasing | **Cloze** | Tests the load-bearing words in context instead of demanding whole-passage recitation |
| Ordered sequences | **Cloze, one deletion per step** | Preserves the sequence as context |
| Paradigms, conjugation tables | **Table card**, or cloze on individual cells | |
| Isnād structure, maps, diagrams | **Image occlusion** | Far better than describing a diagram in words |

### The dividing line: cloze vs. bidirectional

**Cloze when the context is load-bearing. Bidirectional when the pair stands alone.**

Context-free vocabulary doesn't need a sentence wrapped around it. لَفْظ ↔ any sound a human produces works as a bidirectional note, and the reverse card has a cleaner front than a mutilated sentence would. But a term's *position in a division* is meaningless without the division, so it gets clozed.

Applying that to the §1 example — three bidirectional notes plus one structural note, not five basic cards:

| Note | Type |
|---|---|
| Any sound produced by a human ↔ لَفْظ | Bidirectional |
| لَفْظٌ مَوْضُوع ↔ an utterance to which a meaning has been assigned | Bidirectional |
| لَفْظٌ مُهْمَل ↔ an utterance to which no meaning has been assigned | Bidirectional |
| On what basis is لَفْظ divided into مَوْضُوع and مُهْمَل? → whether a meaning has been assigned to it | Basic (or clozed into the spine, §7) |

**Why not the two extra cards** ("What is a meaningful lafẓ called?" *and* "What is a meaningful human utterance called?"): those fronts differ only in whether لَفْظ is supplied or expected. Two near-identical fronts is textbook interference (§9) — you will swap them for a year. The bidirectional note gets both directions with one front each, and Anki buries the siblings automatically.

### Other positions

- **Bidirectional is for terminology only.** Not for facts, not for dates, not for "definition → term" where the definition could describe five different terms. Every bidirectional note is two cards; charge yourself accordingly.
- **Enumeration cards ("name all 8 rewards of taqwā") are usually leeches.** Whole-set recall is the highest-failure card type there is. Keep one *only* when reciting the complete set is genuinely examinable — and then give it a first-letter hint, or build it as overlapping clozes rather than a naked list.
  - *Real exception:* when the division **is** the taught object. In manṭiq, the لَفْظ tree is not incidental structure — everything downstream hangs off it. When the structure is what's being taught, the structure gets a card.
- **Don't generate six angles on one concept as a matter of course.** Application and distinction cards are excellent — when the application or distinction is itself something you need to know. Generating them mechanically is how a 40-fact lecture becomes 240 cards (§3).

---

## 7. Structural notes: the cross-sentence layer

Pass 2 of §1 produces relations that span sentences. These have no natural bare Q/A front — you end up inventing a stilted question — but they cloze beautifully, because a cloze carries the relation and its context in the same note. Three note shapes plus one log.

### The spine note

**One canonical statement per topic, stating the division tree as far as it has been taught, with each node label clozed.** This is the main artifact to add and the single highest-value note in a manṭiq or uṣūl deck.

```
اللَّفْظ is either {{c1::مَوْضُوع::the assigned one}} or {{c2::مُهْمَل::the neglected one}};
مَوْضُوع is either {{c3::مُفْرَد}} or {{c4::مُرَكَّب}}.
```

The critical property: **it is not a per-lecture artifact.** When مُفْرَد gets subdivided three weeks later, you *edit this note* rather than creating a new one. Anki keeps the review history on the existing deletions and only the new cloze enters as new material. A lecture-by-lecture pipeline structurally cannot produce this — it has to be maintained as a standing note per topic.

### Criterion contrast notes

Where two divisions have similar-sounding criteria — the main interference source in manṭiq — cloze the criterion and leave the contrasting case visible:

```
لَفْظ divides by {{c1::whether a meaning has been assigned to it}};
مَوْضُوع divides by {{c2::whether a part of the word signifies a part of the meaning}}.
```

Each card shows the other criterion while asking for one. The disambiguation happens at authoring time instead of in your head at 11pm.

### Placement notes

```
مُرَكَّب is a subdivision of {{c1::مَوْضُوع}}, not of لَفْظ directly.
```

Catches the specific error of knowing a term perfectly but hanging it off the wrong node — the error you'd actually make under pressure, and one that none of the term↔meaning cards test.

### The forward-reference log

Not a card. A running list in the course file for every "we'll come back to this," with the lecture date and the topic it was promised against. When the later lecture lands, the log tells you **which spine note to go edit.** Without it, the promised material arrives and nothing connects it to the structure it belongs to.

### Cloze rules, corrected

- **There is no fixed deletion count.** The real rule: **every deletion must be independently answerable from what remains visible.** In prose that caps out around three, because prose deletions lean on each other. In a skeletal structural statement where each deletion is a single node label and everything else is scaffolding, six is fine. The spine note above has four and is correct.
- **Delete the word that carries the meaning** — not the particle, not the article, not half a clause. A deleted clause is a paragraph you're trying to recite, and it will become a leech.
- **Parallel deletions need hints.** In a tree, two `[...]` in structurally identical positions are genuinely ambiguous: "either [...] or مُهْمَل" is answerable, but "مُفْرَد or [...]" in a deeper branch may not tell you which branch you're in. `{{c1::مَوْضُوع::the assigned one}}` fixes it at no cost.
- **Sibling burying is on by default in modern Anki** and is what makes multi-deletion notes safe — the deletions from one note spread across days rather than all landing together.

---

## 8. Vocabulary notes

Vocabulary is the highest-volume category in the deck and the one most prone to both under-specification and interference. Two hard requirements and one collision rule.

### Every vocabulary note carries its full principal parts

A word learned in one form is a word you can't read in any other. The requirement is by part of speech:

| Part of speech | Required forms |
|---|---|
| **اِسْم (noun)** | singular + plural |
| **فِعْل (verb)** | مَاضِي (past), مُضَارِع (present), أَمْر (command), مَصْدَر (verbal noun) |

These are **not** one card. "Give all four principal parts of نَصَرَ" is a compound card that fails as a unit and tells you nothing about which form you missed. Use a cloze paradigm — one deletion per form, siblings buried, each independently answerable from the base form (§7):

```
نَصَرَ — {{c1::يَنْصُرُ}} — {{c2::اُنْصُرْ}} — {{c3::نَصْرٌ}}
```

For isms, cloze both directions in one note — producing a broken plural and recognising one are different skills, and both are needed:

```
{{c2::كِتَاب}} (مُفْرَد) — {{c1::كُتُب}} (جَمْع)
```

The meaning is a **separate bidirectional note**, not a field on the paradigm. Paradigm and gloss are different retrievals and belong on different cards.

**Minimum per vocabulary item:**

| Note | Type | Tests |
|---|---|---|
| Paradigm (forms) | Cloze, one deletion per form | Morphology |
| Term ↔ meaning | Bidirectional | Semantics |

Two notes, four to five cards, complete coverage of the word. That is the floor, not a target to trim.

### Shared translations must be disambiguated — on both cards

The moment two Arabic words share an English gloss, the meaning → term direction becomes unanswerable and **both** words become leeches. عِلْم and مَعْرِفَة both glossed "knowledge" means the front "knowledge" has two correct answers and you will fail it forever without ever learning anything.

The rule: **no bare gloss may serve as a front if any other term in the collection shares it.**

Fixes, in order of preference:

1. **Sharpen the gloss so it's unique.** The best disambiguator is a better translation. عِلْم → "knowledge as an established body of what is known"; مَعْرِفَة → "knowledge as acquaintance with a particular thing." Now neither front is ambiguous and you've learned the actual distinction.
2. **Add a distinguishing tag to the front** when the gloss can't be sharpened: register, root, pattern, or a collocation the word actually appears in. `ability (the intrinsic capacity — root ق‑د‑ر)`.
3. **Add an explicit contrast note** (§7) when the distinction is itself examinable:
   ```
   عِلْم is knowledge {{c1::as an established body of what is known}};
   مَعْرِفَة is knowledge {{c2::as acquaintance with a specific thing}}.
   ```

**When a collision is found, fix both cards, not just the new one.** The older card's gloss was unambiguous when it was written and stopped being so the moment the second word arrived. Leaving it alone means the interference is only half-treated — and the old card, being mature, is the one you'll trust and the one that will now start failing.

### The same problem in the other direction: one term, two sciences

The gloss index catches two Arabic words sharing one English gloss. The mirror case — **one Arabic word carrying different senses in different sciences** — is worse, because both cards are individually correct and neither looks wrong. مُفْرَد is *a single word* in نَحْو and *singular* in صَرْف.

Every card whose subject is such a term carries a science label, and the registry of these terms lives in `shared-terms.md`. As with glosses: when the second sense arrives, the first card must be edited too.

**Maintain a gloss index.** A running list in the course file of every English gloss already used. Before adding a vocabulary note, search the collection for the gloss (Anki: search the meaning field). This is a five-second check that prevents the single most common source of vocabulary leeches, and it only works if it's done at authoring time — retrofitting it across 800 notes is a project.

---

## 9. Interference — the failure mode specific to this material

Islamic-sciences decks fail on *interference* more than on difficulty. Dozens of narrators with similar names, dozens of death dates in the same century, clusters of technical terms with overlapping definitions, and division criteria that all sound like "whether it has X." Cards that are individually fine collide in memory and become leeches together.

Fix it at authoring time:

- **Never create sibling cards that differ only in one proper noun.** If "When did Imām al-Bukhārī die?" and "When did Imām Muslim die?" are the only distinguishing content, you'll swap them forever. Add an anchor to each front — a relationship, a place, a work, a teacher-student link.
- **Never create fronts that differ only in whether a term is supplied or expected.** See the two rejected cards in §6.
- **Never let two terms share an English gloss.** The highest-frequency instance of interference in this material, and the one with a systematic fix — see §8.
- **Card the distinction explicitly** when two things are confusable: "What distinguishes *mursal* from *munqaṭiʿ*?" is often a better card than two separate definitions. For criteria, use a contrast note (§7).
- **Attach dates to something.** A bare year is an orphan. "Died 256 AH, two years after his student X" is retrievable.
- **When a cluster becomes leeches, the fix is a rewrite, not more repetitions.** See §18.

---
