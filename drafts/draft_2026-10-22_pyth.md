# Draft — ICS H32: namedtuple, Recursion, Set, Dictionaries (21 new notes)

Status: **awaiting approval.**

Source: the Python page as fetched on 2026-10-22: the new *namedtuple* toggle under Tuple, and the new topics
Recursion, Set and Dictionaries. The page has no dates, so the session tag `oct22` is the carding date, as before.

## Decisions you should know about

- **Spelling:** your notes have “namedtumple”; the cards say namedtuple.
- **Terms:** your notes call namedtuple's second argument “an array of strings”, and `del` an operator. In Python
  they're a list and a statement. The cards say list, and don't call `del` an operator.
- **Keys:** your notes say you index a dictionary “using strings”. The cards say “by key”, since keys needn't be
  strings, though your example's are.
- **Added from what I know:** one card on the empty set. It's written `set()`, because `{}` on its own is an empty
  dictionary. Your notes give both literals curly braces, so this is the trap. Drop it if you'd rather keep to
  the notes.
- **Code examples are mine:** your notes have none for these topics, apart from the dict literal. So the four
  “What does this print?” cards use my examples: `._replace()`, `._fields`, a set union, and a loop over your dict.
- **All Tier 1.**

## Cards

| id | Type | Front | Back |
|---|---|---|---|
| pyth-193 | basic | What is a <code>namedtuple</code>? | A tuple in which each element is explicitly given a name |
| pyth-194 | basic | How do you get <code>namedtuple</code> objects? | First make a blueprint — a new type — with namedtuple; then create objects from that type |
| pyth-195 | basic | Where does <code>namedtuple</code> come from? | The collections module: <code>from collections import namedtuple</code> |
| pyth-196 | basic | What two arguments does <code>namedtuple</code> take? | A string naming the new type, and a list of strings naming its fields |
| pyth-197 | basic | What does this print?<pre class="code">from collections import namedtuple<br>Point = namedtuple('Point', ['x', 'y'])<br>p = Point(1, 2)<br>print(p._replace(y=5))</pre> | <code>Point(x=1, y=5)</code> — <code>._replace()</code> returns a new object of the same type with the named fields replaced; <code>p</code> itself is unchanged |
| pyth-198 | basic | What does this print?<pre class="code">from collections import namedtuple<br>Point = namedtuple('Point', ['x', 'y'])<br>print(Point._fields)</pre> | <code>('x', 'y')</code> — <code>._fields</code> gives the names of the fields |
| pyth-199 | basic | What is recursion? | A function calling itself in its own definition — something you can't do when defining a word |
| pyth-200 | basic | What should you try before reaching for recursion? | A loop |
| pyth-201 | basic | What is a set's defining characteristic? | Order makes no difference — the only thing that matters is membership |
| pyth-202 | basic | How do you write a set literal? | Expressions in curly braces, separated by commas: <code>{1, 2, 3}</code> |
| pyth-203 | basic | How do you write an empty set, and why not <code>{}</code>? | <code>set()</code> — <code>{}</code> on its own is an empty dictionary |
| pyth-204 | basic | How do you test whether something is in a set, and why use a set for it? | With <code>in</code>. It works on lists too, but sets are optimised for exactly this. |
| pyth-205 | cloze | Set operators: {{c1::<code>&#124;</code>}} gives the union; {{c2::<code>&amp;</code>}} the intersection; {{c3::<code>-</code>}} the difference; {{c4::<code>^</code>}} the symmetric difference |  |
| pyth-206 | basic | What does this print?<pre class="code">print({1, 2} &#124; {2, 3})</pre> | <code>{1, 2, 3}</code> — the union; 2 appears once, since a set holds each value only once |
| pyth-207 | basic | Why can't you index into a set, and what can you do instead? | It has no fixed order — but you can iterate over it |
| pyth-208 | basic | How do you change a set's contents? | With <code>.add()</code> and <code>.remove()</code> — sets are mutable |
| pyth-209 | basic | What does a dictionary do? | Maps keys to values — essentially a keyed set, and also written with curly braces |
| pyth-210 | basic | How do you write a dict literal? | <code>{'a': 4, 'b': 6}</code> |
| pyth-211 | basic | How do you read, assign and delete a dictionary entry? | Index it by key — <code>d['a']</code> and <code>d['a'] = 5</code> — and delete with <code>del d['a']</code> |
| pyth-212 | basic | What does this print?<pre class="code">d = {'a': 4, 'b': 6}<br>for k in d:<br>    print(k)</pre> | <code>a</code>, then <code>b</code> — iterating a dictionary gives its keys |
| pyth-213 | basic | How do you iterate over a dictionary's values, and over its key–value pairs? | <code>.values()</code> for the values; <code>.items()</code> for the pairs, each a tuple |
