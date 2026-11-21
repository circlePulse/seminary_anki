"""Merge drafts/<prefix>_<deck>_batch.json into decks, numbering ids after each deck's highest of the given prefix.
  python3 drafts/merge_batches.py PREFIX OUTDIR     scratch copies in OUTDIR/x/
  python3 drafts/merge_batches.py PREFIX --write    in place"""
import json, glob, sys, os
pre, out = sys.argv[1], sys.argv[2]
PFX = {"arbaeen_ahadith": "arbh", "quduri": "qud", "wrel": "wrel", "pyth": "pyth", "nahw": "nahw", "sarf": "sarf",
       "vocab": "voc", "riyad": "riyad", "hafs": "hafs"}
for f in sorted(glob.glob(f"drafts/{pre}_*_batch.json")):
    name = f[len(f"drafts/{pre}_"):-len("_batch.json")]
    p = f"decks/{name}.json"; raw = open(p).read(); d = json.loads(raw)
    assert json.dumps(d, ensure_ascii=False, indent=1) == raw.rstrip("\n")
    k = PFX[name]; n = max(int(c["id"].split("-")[1]) for c in d["cards"] if c["id"].startswith(k + "-"))
    for c in json.load(open(f)):
        n += 1; c = {"id": f"{k}-{n:03d}", **c}; d["cards"].append(c)
    d["expected_count"] = len(d["cards"])
    s = json.dumps(d, ensure_ascii=False, indent=1) + ("\n" if raw.endswith("\n") else "")
    if out == "--write": open(p, "w").write(s)
    else: os.makedirs(f"{out}/x", exist_ok=True); open(f"{out}/x/{name}.json", "w").write(s)
    print(name, "->", len(d["cards"]))
