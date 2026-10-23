# Draft — ICS H32: example project notes (4 new notes)

Status: **awaiting approval.**

Source: the new *Example project notes* toggle on the Python page, fetched on 2026-10-23. The page has no dates, so
the session tag `oct23` is the carding date, as before.

## Decisions you should know about

- **Code example is mine:** your notes have none, so the "What does this print?" card splits a date on "-".
- **All Tier 1.**

## Cards

| id | Type | Front | Back |
|---|---|---|---|
| pyth-214 | basic | In a module, what does a leading underscore on a function or variable name indicate? | That it's private — by convention only; nothing enforces it |
| pyth-215 | basic | What does an all-uppercase variable name indicate? | A constant — again a convention that nothing enforces |
| pyth-216 | basic | What does <code>.split()</code> split on, by default and otherwise? | Whitespace by default — or whatever separator you pass it |
| pyth-217 | basic | What does this print?<pre class="code">print('2026-10-23'.split('-'))</pre> | <code>['2026', '10', '23']</code> — a list of the pieces between each separator |
