# seminary_anki

Source of truth for my IOK Seminary Anki decks. The `.apkg` files are build
artifacts; **this repo is the real collection.**

## If you are Claude, start here

1. Read `skill/SKILL.md` in full, then the reference files it points to.
2. `decks/*.json` is the source. Never rebuild a deck from the conversation, from
   Notion, or from memory — read the JSON, edit it, rebuild.
3. **Never reassign card ids.** See the warning below; it is the one mistake that
   cannot be undone.
4. Run `./build.sh` to rebuild everything. It refuses to build if ids have moved.
5. Commit `decks/`, `ids.lock.json`, `delivered.json`, `registry/` and `drafts/`. `build/` is ignored.
6. **Deliver deltas only.** `delivered.json` is the record of what is in Anki. A routine
   update ships only notes that are new or changed against it — never the whole deck.

## The one irreversible mistake

A note's Anki GUID is derived from `(course, card id)`. That mapping is the only
link between a rebuilt deck and notes that already carry review history.

Change an id and the note does not update — it imports as a **duplicate**, and the
original's scheduling data is orphaned with no way to get it back. Content can
always be re-derived from Notion. Styling can be rewritten in ten minutes. Review
history cannot be reconstructed from anything.

So ids are **append-only**. A new card takes the next unused number. A deleted card
burns its id forever. Never write:

```python
for i, c in enumerate(cards, 1):      # NEVER
    c["id"] = f"nahw-{i:03d}"
```

That line is how the ids were first assigned, and re-running it after inserting a
card anywhere but the end shifts every id downstream. Nothing in Anki would
complain — the deck would simply appear twice at the next import.

`skill/scripts/check_ids.py` guards this. It fingerprints every id against the card
it points at, and fails the build when a large fraction of a deck's ids suddenly
point somewhere else, which is the signature of a renumber rather than of editing.
`build.sh` runs it first.

## Layout

```
decks/              one JSON per deck — THE SOURCE
ids.lock.json       append-only id ledger + content fingerprints
registry/
  gloss-index.md    generated: every English gloss, with collisions flagged
  shared-terms.md   hand-kept: one Arabic word, different senses per science
  forward-refs.md   hand-kept: deferred material, and which note it will edit
drafts/             the review artefact for each deck, kept for provenance
skill/              the seminary-anki skill — prompts, references, scripts
build/              .apkg output, gitignored
```

## Where this runs

On the user's own machine, through Claude Code in the Claude Desktop app. The folder
is permanent — there is no sandbox to rebuild from. Run sessions locally rather than
in the cloud; a cloud session keeps only what is explicitly delivered. Commit and push
at the end of every session.

## Workflow

```bash
./build.sh                                        # check ids, show pending deliveries, regen registry
python3 skill/scripts/generate_deck.py decks/X.json --delta   # deliver ONLY new/changed notes
./build.sh --full                                 # complete decks — fresh collection or recovery only
python3 skill/scripts/check_ids.py --update       # re-lock after intentional edits
python3 skill/scripts/reconcile.py export.apkg    # diff Anki against source
# the .apkg lands in build/ — import it from there
```

Import settings in Anki: **Update notes = Always**, **Update note types = Always**,
**Merge note types = off**. Off keeps the canary alive — if a notetype schema ever
drifts you get a visible `Seminary Basic+` instead of a silent rewrite.

## Editing

Edits go in `decks/*.json`, then rebuild. A card fixed only inside Anki is reverted
at the next import — it survives long enough for you to trust it, then disappears.
If you do fix something mid-review, run `reconcile.py` afterwards so it gets folded
back into the source.

## State as of the first commit

| Deck | Course | Notes |
|---|---|---|
| nahw | ARB-201 | 104 |
| sarf | ARB-201 | 68 |
| arbaeen | HDT-201 | 69 |
| arbaeen2 | HDT-201 | 4 |
| quduri | HDT-201 | 50 |
| riyad | HDT-202 | 4 |
| vocab | VOCAB | 29 |
| **Total** | | **328** |

Notetype ids are pinned in `skill/scripts/ids.py`. They are placeholders adopted at
first build — if notes exist in Anki on differently-numbered notetypes, follow the
migration note at the top of that file before building again.
