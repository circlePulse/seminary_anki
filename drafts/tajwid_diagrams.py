"""Inline-SVG teeth diagram for the Ḥafṣ ijāzah deck (2026-11-17; the anatomical drawings were dropped at the user's
request). Abstract: two rows of eight boxes either side of the midline, upper jaw on top, front in the middle.
Drawn in currentColor so it follows the card's light or dark theme; the group a card asks about is filled in one
accent colour. It carries no label naming a tooth, so it can be the prompt side of a card."""

ACC = "#e8590c"
TEETH_GROUPS = {"thanaya": [0], "rabaiyat": [1], "anyab": [2], "dawahik": [3], "tawahin": [4, 5, 6], "nawajidh": [7]}


def teeth(hi):
    group = TEETH_GROUPS[hi]
    parts = ['<line x1="150" y1="18" x2="150" y2="62" stroke-dasharray="3 3" opacity=".5"/>']
    for y in (22, 42):
        for s in (-1, 1):
            for k in range(8):
                cx = 150 + s * (15 + k * 17)
                fill = f' fill="{ACC}" stroke="{ACC}"' if k in group else ""
                parts.append(f'<rect x="{cx - 7}" y="{y}" width="14" height="14" rx="2"{fill}/>')
    t = lambda x, s: f'<text x="{x}" y="12" text-anchor="middle" font-size="10" fill="currentColor" stroke="none">{s}</text>'
    parts += [t(150, "front"), t(24, "back"), t(276, "back")]
    return ('<svg viewBox="0 0 300 64" width="300" height="64" fill="none" stroke="currentColor" stroke-width="1.5" '
            'style="display: block; margin: .5em auto 0; max-width: 100%; height: auto">' + "".join(parts) + "</svg>")
