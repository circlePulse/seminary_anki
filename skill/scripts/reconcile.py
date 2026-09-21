#!/usr/bin/env python3
"""
Diff your live Anki collection against the source in decks/.

The repo is the source of truth, and every deck is rebuilt from it. That means a
card hand-edited in Anki is silently reverted at the next import — the edit
survives until you rebuild, then vanishes, which is worse than never fixing it,
because by then you trust it.

This closes that loop. Export from Anki (File → Export → Anki Deck Package, with
scheduling included or not — it doesn't matter here), then:

    python3 skill/scripts/reconcile.py ~/Downloads/collection.apkg

Every note whose text differs from the source is reported, along with notes that
exist on one side only. Nothing is written; it tells you what to fix and where.

When a difference is real, fix it in decks/*.json and rebuild — never the other
way round.
"""

import glob
import json
import os
import re
import sqlite3
import sys
import tempfile
import zipfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import genanki  # noqa: E402  (only for guid_for — same hash the build uses)

FSEP = "\x1f"


def norm(s):
    """Compare what the card says, not how it is marked up."""
    s = re.sub(r"<div class=\"science\">.*?</div>", " ", s)
    s = re.sub(r"<[^>]+>", " ", s)
    s = s.replace("&nbsp;", " ").replace("&amp;", "&")
    return re.sub(r"\s+", " ", s).strip()


def source_notes():
    out = {}
    for f in sorted(glob.glob("decks/*.json")):
        d = json.load(open(f, encoding="utf-8"))
        for c in d["cards"]:
            guid = genanki.guid_for(d["course"], c["id"])
            if c["type"] == "basic":
                fields = [c["front"], c["back"]]
            elif c["type"] == "bidir":
                fields = [c["term"], c["meaning"]]
            else:
                fields = [c["text"], c.get("extra", "")]
            out[guid] = {"deck": os.path.basename(f)[:-5], "id": c["id"],
                         "fields": [norm(x) for x in fields]}
    return out


def collection_notes(path):
    tmp = tempfile.mkdtemp()
    with zipfile.ZipFile(path) as z:
        inner = next((n for n in ("collection.anki21b", "collection.anki21",
                                  "collection.anki2") if n in z.namelist()), None)
        if not inner:
            sys.exit(f"no collection database inside {path}")
        if inner.endswith("b"):
            sys.exit("This export is zstd-compressed. Re-export with "
                     "'Support older Anki versions' ticked, or export as .colpkg "
                     "from an older scheme.")
        z.extract(inner, tmp)
    db = sqlite3.connect(os.path.join(tmp, inner))
    out = {}
    for guid, flds in db.execute("select guid, flds from notes"):
        parts = flds.split(FSEP)
        out[guid] = [norm(p) for p in parts[:2]]
    return out


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    src, col = source_notes(), collection_notes(sys.argv[1])

    drifted, missing = [], []
    for guid, s in src.items():
        if guid not in col:
            missing.append(s)
            continue
        if s["fields"] != col[guid][:len(s["fields"])]:
            drifted.append((s, col[guid]))
    unknown = [g for g in col if g not in src]

    print(f"source: {len(src)} notes    collection: {len(col)} notes\n")

    if drifted:
        print(f"DIFFERENT — {len(drifted)} note(s) edited in Anki since the last build:\n")
        for s, c in drifted:
            print(f"  {s['id']}  ({s['deck']})")
            for i, (a, b) in enumerate(zip(s["fields"], c)):
                if a != b:
                    print(f"    source: {a[:90]}")
                    print(f"    anki:   {b[:90]}")
            print()
        print("  Fix these in decks/*.json, then rebuild. Editing in Anki alone")
        print("  will not survive the next import.\n")

    if missing:
        print(f"NOT IN ANKI — {len(missing)} note(s) in source but not imported:")
        for s in missing[:20]:
            print(f"  {s['id']} ({s['deck']})")
        if len(missing) > 20:
            print(f"  … and {len(missing)-20} more")
        print()

    if unknown:
        print(f"NOT IN SOURCE — {len(unknown)} note(s) in Anki with no source entry.")
        print("  Expect these if you have decks from before this repo, or made cards")
        print("  by hand. Worth folding into decks/ so they survive a rebuild.\n")

    if not (drifted or missing):
        print("In sync.")


if __name__ == "__main__":
    main()
