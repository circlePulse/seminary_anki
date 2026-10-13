#!/usr/bin/env python3
"""Run from the repo root: python3 skill/scripts/check_direction.py — expect "total 0".

Which card sides flip to right-to-left under a dir="auto" container? dir=auto takes the first strong
letter in the subtree, skipping <bdi> and elements with their own dir attribute. A side flips when that
letter is Arabic; it shows the damage when the side also has Latin text laid out inside the flipped box."""
import json, re, glob, importlib.util, collections
spec = importlib.util.spec_from_file_location('g', 'skill/scripts/generate_deck.py')
g = importlib.util.module_from_spec(spec); spec.loader.exec_module(g)
AR, LAT = re.compile(r'[؀-ۿ]'), re.compile(r'[A-Za-z]')
C = re.compile(r"\{\{c(\d+)::((?:(?!\}\}|::).)*)(?:::((?:(?!\}\}).)*))?\}\}")
from html.parser import HTMLParser
VOID = {'br', 'hr', 'img', 'input', 'meta', 'link'}
class _FS(HTMLParser):
    """dir=auto's rule: the first strong letter in the subtree, skipping <bdi> and any element
    that carries its own dir attribute (with everything inside it)."""
    def __init__(self):
        super().__init__(); self.skip = 0; self.res = None
    def handle_starttag(self, tag, attrs):
        if tag in VOID: return
        if self.skip or tag == 'bdi' or any(k == 'dir' for k, _ in attrs): self.skip += 1
    def handle_endtag(self, tag):
        if tag in VOID: return
        if self.skip: self.skip -= 1
    def handle_data(self, data):
        if self.skip or self.res: return
        for ch in data:
            if AR.match(ch): self.res = 'rtl'; return
            if LAT.match(ch): self.res = 'ltr'; return
def first_strong(html):
    p = _FS(); p.feed(html); return p.res or 'none'
def outside_rtl_blocks(html):   # Latin text not sitting inside its own rtl/isolated block
    h = re.sub(r'<div class="arabic">.*?</div>', '', html, flags=re.S)
    return re.sub(r'<[^>]+>', ' ', h)
def rendered(c, d):
    kind, f, _ = g.payload(c, d); m = g.MODELS[kind]
    if kind == 'cloze':
        n = int(re.search(r'\{\{c(\d+)::', f[0]).group(1))
        t = C.sub(lambda mm: mm.group(2), f[0])
        tmpl = m.templates[0]['afmt'].replace('{{cloze:Text}}', t).replace('{{Extra}}', f[1]).replace('{{Source}}', '')
        return [tmpl]
    names = [x['name'] for x in m.fields]; fd = dict(zip(names, f)); fd['Source'] = ''
    out = []
    for t in m.templates:
        q = t['qfmt']; a = t['afmt'].replace('{{FrontSide}}', q)
        for k, v in fd.items(): a = a.replace('{{%s}}' % k, v)
        out.append(a)
    return out
tot = collections.Counter(); ex = collections.defaultdict(list)
for fpath in sorted(glob.glob('decks/*.json')):
    d = json.load(open(fpath)); deck = fpath.split('/')[-1][:-5]
    for c in d['cards']:
        for html in rendered(c, d):
            if first_strong(html) == 'rtl' and LAT.search(outside_rtl_blocks(html)):
                tot[deck] += 1; ex[deck].append(c['id']); break
print('notes with at least one flipped side, by deck:')
for k, v in tot.most_common(): print(f'  {k:16} {v:4}   e.g. {", ".join(sorted(set(ex[k]))[:6])}')
print('total', sum(tot.values()))
