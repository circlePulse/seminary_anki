# Domain Pack — Programming / CS

Read alongside `card-design.md`. Everything there still holds — decomposition, the
four tests, tiering, interference, delta delivery. This covers what is different
about a programming course.

## The thing that wrecks CS decks: carding lookups

**Do not card what an editor, autocomplete, or one search gives you in two seconds.**
Exact argument order, method signatures, import paths, flag names, stdlib minutiae.
Carding them is the standard way a programming deck reaches 800 cards and gets
abandoned, and none of it is knowledge you are ever tested on without a machine in
front of you.

The test is the same as everywhere else: **would you need to produce this cold?**
In a programming course that usually means in an exam, on a whiteboard, or while
reasoning about code that is already broken.

| Card it | Don't |
|---|---|
| What a construct *does*, including its edge cases | Its exact signature |
| Why two similar things differ | That both exist |
| Complexity, and what drives it | Memorised complexity tables with no reasoning |
| The invariant a structure maintains | The method names that maintain it |
| What a given snippet outputs, and why | Reproducing library source |
| Cause → symptom for common errors | Error message text verbatim |
| Vocabulary of the field — the words lectures assume | Words you only ever read, never say |

## The highest-value card type: predict the output

A short snippet on the front, the output *and the reason* on the back. It tests a
mental model rather than a lookup, and a wrong answer tells you precisely which part
of the model is broken.

```
What does this print?

    def f(x, acc=[]):
        acc.append(x)
        return acc
    print(f(1)); print(f(2))
```
→ `[1]` then `[1, 2]` — the default list is created once at definition and
shared across every call that doesn't pass one.

**Keep snippets under about eight lines.** Longer and it becomes a reading exercise
with recall attached, and failure stops being diagnostic — you won't know whether you
misread it or misunderstood it.

## Formatting

Wrap code in `<pre class="code">`. The shared notetypes provide `.code` with a
monospace stack, preserved whitespace, left alignment, and horizontal scrolling. The
cards are centre-aligned by default, and centred code with collapsed indentation is
unreadable — Python especially, where the indentation *is* the syntax.

Inline identifiers in a sentence use `<code>`.

## Cloze on code

Good for fixed idioms with one moving part — a comprehension shape, a context-manager
line, a decorator form. Bad for whole functions: too many deletions, none of them
independently answerable, and it becomes transcription rather than recall.

Delete the part that carries the decision, not the boilerplate.

## Interference: near-identical operations

The CS equivalent of the narrator problem. Pairs that differ in one respect and will
collapse into each other unless carded against one another:

- `append` vs `extend` · `sort` vs `sorted` · `remove` vs `pop` vs `del`
- `is` vs `==` · shallow vs deep copy · mutable vs immutable defaults
- iterator vs iterable · generator vs list comprehension
- pass-by-object-reference confusions of every kind

Each pair gets a contrast note holding both sides in one view, not two separate
definition cards.

## Tiering in a programming course

- **Tier 1** — semantics that bite, complexity, invariants, vocabulary, anything the
  lecturer said would be examined
- **Tier 2** — library specifics you'd normally look up but might be asked to
  recognise; historical or version trivia
- **Tier 3** — anything an editor completes for you
