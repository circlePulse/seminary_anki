#!/usr/bin/env python3
"""
Isolate the Arabic in a deck's fields, per references/arabic.md.

  python3 skill/scripts/wrap_arabic.py decks/X.json            # report only
  python3 skill/scripts/wrap_arabic.py decks/X.json --write

A line that also holds Latin text gets each Arabic run wrapped in <bdi>, inside the
cloze braces, never around them. A line that is entirely Arabic and holds a blank,
a dash or a bracket goes in one <div class="arabic">. A bare Arabic term with
nothing around it renders correctly already and is left alone.

Runs already inside <bdi>, <div class="arabic"> or <div class="science"> are not
touched. Every rewritten field is checked: stripping the added tags back out must
give the original byte for byte, or the script refuses to write.
"""
import argparse
import json
import re
import sys

AR = "؀-ۿݐ-ݿﭐ-﷿ﹰ-﻿"
_AR = re.compile(f"[{AR}]")
_LATIN = re.compile(r"[A-Za-z]")
# a run: Arabic letters, joined by spaces or by a hyphen/en dash written tight
# between letters (ق‑د‑ر, فَعِلَ–يَفْعُلُ) — those belong to one Arabic unit
_RUN = re.compile(f"[{AR}](?:[{AR}]|[  ]+(?=[{AR}])|[-‐‑–](?=[{AR}]))*")
_PROTECTED = re.compile(r'<bdi>.*?</bdi>|<div class="(?:arabic|science)">.*?</div>'
                        r'|<span class="ar">.*?</span>|<code>.*?</code>|<pre.*?</pre>|<[^>]+>',
                        re.S)
_CLOZE = re.compile(r"\{\{c\d+::((?:(?!\}\}|::).)*)(?:::(?:(?!\}\}).)*)?\}\}")
_BR = re.compile(r"(<br\s*/?>)")
FIELDS = {"basic": ("front", "back"), "bidir": ("term", "meaning"), "cloze": ("text", "extra")}


def _bare(line):
    """The visible text of a line outside existing isolates, cloze hints dropped."""
    s = re.sub(r'<bdi>.*?</bdi>|<div class="(?:arabic|science)">.*?</div>', "", line, flags=re.S)
    return re.sub(r"<[^>]+>", "", _CLOZE.sub(r"\1", s))


def _wrap_runs(line):
    out, pos = [], 0
    for m in _PROTECTED.finditer(line):
        out.append(_RUN.sub(r"<bdi>\g<0></bdi>", line[pos:m.start()]))
        out.append(m.group(0))
        pos = m.end()
    out.append(_RUN.sub(r"<bdi>\g<0></bdi>", line[pos:]))
    return "".join(out)


def wrap_line(line):
    bare = _bare(line)
    if not _AR.search(bare):
        return line
    if _LATIN.search(bare):
        return _wrap_runs(line)
    if "{{c" in line or re.search(r"[—–()\[\]]", bare) or line.count("<bdi>") >= 2:
        return f'<div class="arabic">{re.sub(r"</?bdi>", "", line)}</div>'
    return line


def wrap_field(v):
    return "".join(p if _BR.fullmatch(p) else wrap_line(p) for p in _BR.split(v))


def _strip_added(s):
    s = re.sub(r"</?bdi>", "", s)
    return re.sub(r'^<div class="arabic">(.*)</div>$', r"\1", s, flags=re.S) if "<br" not in s \
        else re.sub(r'<div class="arabic">(.*?)</div>', r"\1", s, flags=re.S)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("deck")
    ap.add_argument("--write", action="store_true")
    a = ap.parse_args()
    data = json.load(open(a.deck, encoding="utf-8"))
    changed = []
    for c in data["cards"]:
        for k in FIELDS[c["type"]]:
            old = c.get(k, "")
            new = wrap_field(old)
            if new == old:
                continue
            if _strip_added(new) != _strip_added(old):
                sys.exit(f"{c['id']}.{k}: stripping the tags does not give the original back")
            changed.append((c["id"], k, old, new))
            c[k] = new
    for i, k, old, new in changed:
        print(f"{i}.{k}\n  - {old}\n  + {new}")
    print(f"{len(changed)} field(s) in {len({i for i, *_ in changed})} card(s)")
    if a.write and changed:
        json.dump(data, open(a.deck, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        print(f"wrote {a.deck}")


if __name__ == "__main__":
    main()
