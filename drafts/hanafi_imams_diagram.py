"""Inline-SVG diagram for the Ḥanafī shorthand names (2026-11-18, modelled on the user's own diagram): Abū Ḥanīfah
on top, Abū Yūsuf and Muḥammad below; the imams a term names are filled and joined, the other is dimmed. Drawn in
currentColor plus one accent, so it follows the card's light or dark theme. The <title> names the pair, so each
diagram has distinct text for the gloss index without showing it."""
ACC = "#3a9b74"
BOX = {"AH": (95, 10, "Abū Ḥanīfah"), "AY": (10, 100, "Abū Yūsuf"), "M": (190, 100, "Muḥammad")}
LINK = {frozenset(("AH", "AY")): "M128,42 L68,100", frozenset(("AH", "M")): "M172,42 L232,100",
        frozenset(("AY", "M")): "M110,116 L190,116"}


def imams(on, title):
    parts = [f"<title>{title}</title>"]
    for pair, d in LINK.items():
        if pair <= set(on):
            parts.append(f'<path d="{d}" stroke="{ACC}" stroke-width="2.5"/>')
    for k, (x, y, name) in BOX.items():
        lit = k in on
        fill = f'fill="{ACC}" fill-opacity=".3" stroke="{ACC}"' if lit else 'fill="none" stroke="currentColor" opacity=".35"'
        look = ' font-weight="600"' if lit else ' opacity=".45"'
        parts.append(f'<rect x="{x}" y="{y}" width="100" height="32" rx="6" {fill} stroke-width="1.5"/>'
                     f'<text x="{x + 50}" y="{y + 21}" text-anchor="middle" font-size="14" fill="currentColor" '
                     f'stroke="none"{look}>{name}</text>')
    return ('<svg viewBox="0 0 300 142" width="300" height="142" fill="none" '
            'style="display: block; margin: .5em auto 0; max-width: 100%; height: auto">' + "".join(parts) + "</svg>")
