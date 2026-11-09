"""Inline-SVG memory diagrams for Python cards (approved 2026-11-09). mem() draws names on the left, objects on the
right and an arrow per reference; a dashed, dimmed arrow or box is an old binding. Everything is currentColor, so a
diagram follows the card's light or dark theme and needs no media file. Append the returned string to a field."""
import math

FONT = 'font-family="SF Mono, Menlo, Consolas, DejaVu Sans Mono, monospace"'


def txt(x, y, s, anchor="middle", size=14, dim=False):
    o = ' opacity=".55"' if dim else ""
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{size}" {FONT} fill="currentColor" stroke="none"{o}>{s}</text>'


def box(x, y, w, h, s, dim=False):
    o = ' opacity=".45"' if dim else ""
    return f'<rect x="{x}" y="{y - h / 2}" width="{w}" height="{h}" rx="4"{o}/>' + txt(x + w / 2, y + 5, s, dim=dim)


def arrow(x1, y1, x2, y2, old=False):
    a, L = math.atan2(y2 - y1, x2 - x1), 8
    p = lambda d: f"{x2 - L * math.cos(a + d):.1f},{y2 - L * math.sin(a + d):.1f}"
    o = ' stroke-dasharray="4 4" opacity=".45"' if old else ""
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2 - 2 * math.cos(a):.1f}" y2="{y2 - 2 * math.sin(a):.1f}"{o}/>'
            f'<polygon points="{x2},{y2} {p(0.4)} {p(-0.4)}" fill="currentColor"{o}/>')


def svg(w, h, *parts):
    return (f'<svg viewBox="0 0 {w} {h}" width="{w}" height="{h}" fill="none" stroke="currentColor" stroke-width="1.5" '
            f'style="display: block; margin: .5em auto 0; max-width: 100%; height: auto">{"".join(parts)}</svg>')


def mem(names, boxes, links, ids=None):
    """A memory diagram: names on the left, objects on the right, an arrow per reference.
    names {label: row}; boxes {key: (text, row[, dim])}; links [(label, key[, old])]; ids {key: caption}."""
    row = 46 if ids else 40
    y = lambda r: 22 + r * row
    rows = max(list(names.values()) + [v[1] for v in boxes.values()]) + 1
    parts = [txt(84, y(r) + 5, n, "end") for n, r in names.items()]
    for key, v in boxes.items():
        parts.append(box(160, y(v[1]), 124, 28, v[0], len(v) > 2 and v[2]))
        if ids and key in ids:
            parts.append(txt(222, y(v[1]) + 27, ids[key], size=10, dim=True))
    for l in links:
        parts.append(arrow(92, y(names[l[0]]), 158, y(boxes[l[1]][1]), len(l) > 2 and l[2]))
    return svg(300, int(rows * row) + (10 if ids else 4), *parts)


cap = lambda s: f'<div style="color: var(--muted); font-size: .8em; margin-top: .6em">{s}</div>'
