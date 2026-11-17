"""Inline-SVG teeth diagram for the Ḥafṣ ijāzah deck (2026-11-17; the anatomical drawings were dropped at the user's
request). Equal squares set along the curve of the upper jaw, front at the top, eight either side of the midline;
the lower jaw mirrors it. Drawn in currentColor so it follows the card's light or dark theme; the group a card asks
about is filled in one accent colour. It carries no label naming a tooth, so it can be the prompt side of a card."""
import math

ACC = "#e8590c"
TEETH_GROUPS = {"thanaya": [0], "rabaiyat": [1], "anyab": [2], "dawahik": [3], "tawahin": [4, 5, 6], "nawajidh": [7]}
SIZE, GAP, C, TOP = 16, 4, 90.0, 30    # square side, gap along the arch, arch width (y = TOP + x²/C), front edge


def _x_at(length):
    """x on the arch y = TOP + x²/C whose arc length from the midline is `length`."""
    h = C / 2
    arc = lambda x: h * ((x / h) * math.hypot(1, x / h) + math.asinh(x / h)) / 2
    lo, hi = 0.0, 300.0
    for _ in range(50):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if arc(mid) < length else (lo, mid)
    return lo


def teeth(hi):
    group = TEETH_GROUPS[hi]
    parts = []
    for k in range(8):
        x = _x_at(GAP / 2 + SIZE / 2 + k * (SIZE + GAP))
        ang = math.degrees(math.atan(2 * x / C))
        fill = f' fill="{ACC}" stroke="{ACC}"' if k in group else ""
        for s in (1, -1):
            parts.append(f'<rect x="{-SIZE / 2}" y="{-SIZE / 2}" width="{SIZE}" height="{SIZE}" rx="2" '
                         f'transform="translate({150 + s * x:.1f},{TOP + x * x / C:.1f}) rotate({s * ang:.1f})"{fill}/>')
    t = lambda x, y, s: (f'<text x="{x}" y="{y}" text-anchor="middle" font-size="10" fill="currentColor" '
                         f'stroke="none">{s}</text>')
    parts += [t(150, 12, "front"), t(150, 150, "upper jaw (the lower mirrors it)")]
    return ('<svg viewBox="0 0 300 158" width="300" height="158" fill="none" stroke="currentColor" stroke-width="1.5" '
            'style="display: block; margin: .5em auto 0; max-width: 100%; height: auto">' + "".join(parts) + "</svg>")
