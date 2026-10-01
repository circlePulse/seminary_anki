#!/usr/bin/env python3
"""
Guard the id lockfile.

Card ids are the only link between a regenerated deck and notes that already
carry review history in Anki. The note GUID is derived from (course, id), so if
an id changes, that note stops being an update and becomes a duplicate — and the
original's scheduling data is orphaned with no way to recover it.

The danger is not malice, it is a one-line loop. Ids were originally assigned
positionally:

    for i, c in enumerate(cards, 1):
        c["id"] = f"nahw-{i:03d}"

Re-run that after inserting a card anywhere but the end and every id downstream
shifts by one. Nothing in Anki would complain; you would simply find the deck
duplicated at the next import.

So: ids are APPEND-ONLY. New cards take the next unused number. Deleting a card
frees nothing — its id is burned.

This script fails the build if any previously recorded id is missing, if an id
has moved to a different deck, or if any deck contains a duplicate.
Run: python3 skill/scripts/check_ids.py [--update]
"""

import collections
import datetime
import glob
import hashlib
import json
import os
import re
import sys

LOCK = "ids.lock.json"
# A renumber shifts every id at once. A real edit touches a handful. Anything
# above this fraction of a deck changing fingerprint in one build is treated as
# a renumber, not as editing.
RENUMBER_FRACTION = 0.25
MIN_DECK_FOR_CHECK = 8


def fingerprint(card):
    """Hash of the card's primary field — what the id is supposed to point at."""
    first = card.get("front") or card.get("term") or card.get("text") or ""
    # Tags and whitespace are dropped entirely, so a markup-only edit (wrapping a run
    # in <bdi>, moving a line into <div class="arabic">) never reads as a new card.
    first = re.sub(r"<[^>]+>", "", first)
    first = re.sub(r"\s+", "", first).lower()
    return hashlib.sha1(first.encode("utf-8")).hexdigest()[:12]


def load_decks():
    out = {}
    for f in sorted(glob.glob("decks/*.json")):
        out[os.path.basename(f)[:-5]] = json.load(open(f, encoding="utf-8"))
    return out


def main():
    update = "--update" in sys.argv
    decks = load_decks()
    if not decks:
        sys.exit("no decks found — run from the repo root")

    current = {n: [c["id"] for c in d["cards"]] for n, d in decks.items()}
    fps = {n: {c["id"]: fingerprint(c) for c in d["cards"]} for n, d in decks.items()}
    errors, warnings = [], []

    # within-collection duplicates
    owner = {}
    for name, ids in current.items():
        for i, cid in enumerate(ids):
            if not cid:
                errors.append(f"{name}: card at position {i+1} has no id")
            elif cid in owner:
                errors.append(f"duplicate id {cid}: in both {owner[cid]} and {name}")
            else:
                owner[cid] = name

    if os.path.exists(LOCK):
        lock = json.load(open(LOCK))
        for name, rec in lock.get("decks", {}).items():
            if name not in current:
                warnings.append(f"deck {name} is in the lockfile but not in decks/")
                continue
            now = set(current[name])
            gone = [i for i in rec["ids"] if i not in now]
            if gone:
                errors.append(
                    f"{name}: {len(gone)} id(s) vanished — {', '.join(gone[:6])}"
                    f"{' …' if len(gone) > 6 else ''}\n"
                    f"    These notes exist in Anki with review history. Removing or "
                    f"renumbering an id orphans them.\n"
                    f"    If a card was genuinely deleted, remove it from the lockfile "
                    f"by hand and suspend it in Anki instead."
                )
            for cid in now:
                if cid in owner and owner[cid] != name:
                    errors.append(f"id {cid} moved decks")

            # an id must keep pointing at the same card
            old_fp = rec.get("fp", {})
            if old_fp:
                changed = [i for i, h in old_fp.items()
                           if i in fps[name] and fps[name][i] != h]
                n_tracked = len([i for i in old_fp if i in fps[name]])
                if (n_tracked >= MIN_DECK_FOR_CHECK
                        and len(changed) / n_tracked > RENUMBER_FRACTION):
                    # --update is the documented way to accept a deliberate mass
                    # rewrite; vanished or moved ids still fail regardless.
                    (warnings if update else errors).append(
                        f"{name}: {len(changed)}/{n_tracked} ids now point at a "
                        f"different card.\n"
                        f"    That is the signature of a RENUMBER, not of editing — "
                        f"ids were almost certainly reassigned positionally.\n"
                        f"    Every one of those notes would import as a duplicate and "
                        f"orphan its review history.\n"
                        f"    Restore the ids from git before building. If this really "
                        f"was a mass rewrite, re-run with --update."
                    )
                elif changed:
                    warnings.append(
                        f"{name}: {len(changed)} card(s) edited "
                        f"({', '.join(changed[:5])}{' …' if len(changed) > 5 else ''}) "
                        f"— re-run with --update once the build looks right")
        new = sum(len(set(current[n]) - set(lock["decks"].get(n, {}).get("ids", [])))
                  for n in current)
        print(f"  {sum(len(v) for v in current.values())} ids, {new} new since last lock")
    else:
        warnings.append("no lockfile yet — creating one")

    for w in warnings:
        print(f"  note: {w}")
    if errors:
        print("\nID CHECK FAILED\n")
        for e in errors:
            print(f"  {e}")
        sys.exit(1)

    if update or not os.path.exists(LOCK):
        out = {"_comment": "APPEND-ONLY. An id here must never change or disappear. "
                           "It is the only link between a regenerated deck and notes "
                           "that already carry review history in Anki.",
               "generated": datetime.date.today().isoformat(), "decks": {}}
        for name, d in decks.items():
            out["decks"][name] = {"course": d["course"], "topic": d["topic"],
                                  "count": len(d["cards"]), "ids": current[name],
                                  "fp": fps[name]}
        json.dump(out, open(LOCK, "w"), indent=1)
        print(f"  lockfile updated ({sum(len(v) for v in current.values())} ids)")
    else:
        print("  ok — no ids lost")


if __name__ == "__main__":
    main()
