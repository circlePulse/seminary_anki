"""Inline-SVG diagrams for the Ḥafṣ ijāzah deck (2026-11-17). Everything is drawn in currentColor, so a diagram
follows the card's light or dark theme; the part a card asks about is picked out in one accent colour.
  sag(hi, v, arrow)  side view of the head, face to the left. hi: a region or part key (see SAG_PARTS).
                     v: None, 'alif', 'waw' or 'ya' (tongue, jaw and lip position for that madd letter).
                     arrow: draw the sound's path from the vocal cords out through the lips.
  tongue_top(hi)     the tongue from above, tip to the left. hi: a middle-line or edge part key.
  teeth(hi)          the upper teeth from below, front at the top. hi: a group key (see TEETH_GROUPS).
No diagram carries a text label naming a part, so a highlighted diagram can be the prompt side of a card."""
import math

ACC = "#e8590c"


def _cr(p, a=0, b=None):
    """Catmull-Rom through p as cubic segments from p[a] to p[b]."""
    b = len(p) - 1 if b is None else b
    out = []
    for i in range(a, b):
        p0, p1, p2 = p[max(i - 1, 0)], p[i], p[i + 1]
        p3 = p[min(i + 2, len(p) - 1)]
        c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6)
        c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
        out.append(f"C{c1[0]:.1f},{c1[1]:.1f} {c2[0]:.1f},{c2[1]:.1f} {p2[0]:.1f},{p2[1]:.1f}")
    return " ".join(out)


def _m(p): return f"M{p[0]:.1f},{p[1]:.1f}"
def _l(*ps): return " ".join(f"L{x:.1f},{y:.1f}" for x, y in ps)
def _sp(p, a=0, b=None): return _m(p[a]) + " " + _cr(p, a, b)
def _poly(ps): return "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in ps) + " Z"
def _path(d, extra=""): return f'<path d="{d}"{extra}/>'
def _fill(d, op=".35"): return f'<path d="{d}" fill="{ACC}" fill-opacity="{op}" stroke="none"/>'
def _line(d, w=5): return f'<path d="{d}" stroke="{ACC}" stroke-width="{w}" stroke-linecap="round" fill="none"/>'


def _svg(box, w, h, parts):
    return (f'<svg viewBox="{box}" width="{w}" height="{h}" fill="none" stroke="currentColor" stroke-width="1.5" '
            f'stroke-linejoin="round" style="display: block; margin: .5em auto 0; max-width: 100%; height: auto">'
            f'{"".join(parts)}</svg>')


# ---------------------------------------------------------------- side view
ROOF = [(60, 114), (64, 107), (71, 103), (80, 103), (92, 100), (105, 96), (125, 92), (150, 90), (175, 91),
        (198, 95), (215, 100), (230, 106), (236, 110)]
ROOF_PARTS = {"lithah": (0, 3), "muqaddam": (3, 5), "salb": (5, 9), "rikhw": (9, 12)}
UVULA = [(236, 110), (241, 120), (244, 131), (247, 138), (251, 134), (253, 122), (252, 110)]
PALATE_TOP = [(252, 110), (247, 99), (234, 90), (214, 85), (200, 84), (150, 82), (100, 82), (68, 84), (52, 88),
              (50, 96), (54, 104)]
NOSE = [(70, 14), (58, 30), (40, 52), (24, 70), (22, 80), (30, 86), (42, 88)]
NASAL_TOP = [(62, 36), (90, 30), (140, 28), (200, 30), (236, 40), (254, 58)]
BACK_WALL = [(254, 58), (264, 80), (270, 110), (272, 150), (273, 200), (273, 250), (274, 300)]
EPIGLOTTIS = [(234, 213), (239, 204), (244, 193), (247, 182), (250, 190), (249, 204), (242, 216), (234, 213)]
UP_INCISOR = [(50, 100), (57, 100), (61, 114), (59, 128), (57, 140), (53, 140), (50, 124)]

# upper surface of the tongue, tip first; the jaw drop (dy) and lip push (lip) go with it
POSE = {
    None:   dict(dy=0, lip=0, U=[(62, 151), (63, 145), (70, 139), (85, 134), (100, 130), (120, 126), (140, 122),
                                 (160, 119), (178, 119), (195, 121), (212, 126), (224, 134), (230, 146), (233, 165),
                                 (234, 185), (233, 205)]),
    "alif": dict(dy=10, lip=0, U=[(63, 160), (65, 154), (72, 150), (88, 148), (105, 147), (125, 146), (145, 145),
                                  (165, 145), (185, 146), (202, 148), (215, 153), (225, 160), (230, 170), (233, 182),
                                  (234, 194), (233, 205)]),
    "waw":  dict(dy=5, lip=7, U=[(63, 156), (66, 150), (73, 146), (88, 143), (105, 140), (125, 136), (145, 130),
                                 (165, 123), (184, 118), (200, 116), (214, 119), (224, 127), (230, 140), (233, 160),
                                 (234, 183), (233, 205)]),
    "ya":   dict(dy=12, lip=0, U=[(63, 162), (65, 156), (72, 150), (86, 140), (102, 128), (120, 117), (140, 110),
                                  (160, 107), (180, 109), (198, 114), (212, 122), (223, 131), (230, 144), (233, 163),
                                  (234, 184), (233, 205)]),
}
TONGUE_PARTS = {"ras": (0, 2), "taraf": (2, 4), "wasat": (4, 8), "aqsa": (8, 11), "jidhr": (11, 15)}
SAG_PARTS = ("jawf", "halq", "fam", "khayshum", "adna_halq", "wasat_halq", "aqsa_halq", "lahah",
             *ROOF_PARTS, *TONGUE_PARTS)


def _interp(pts, x):
    """y on a piecewise-linear run of points at x (points need not be sorted)."""
    s = sorted(pts)
    for (x0, y0), (x1, y1) in zip(s, s[1:]):
        if x0 <= x <= x1:
            return y0 + (y1 - y0) * (x - x0) / (x1 - x0)
    return s[0][1] if x < s[0][0] else s[-1][1]


def sag(hi=None, v=None, arrow=False):
    pose = POSE[v]
    dy, lip, U = pose["dy"], pose["lip"], pose["U"]
    fade = lambda x, full=100, half=170: dy if x < full else dy / 2 if x < half else 0
    up_lip = [(42, 88), (36, 96), (30 - .4 * lip, 110), (32 - lip, 126), (40 - lip, 134), (50 - .6 * lip, 140)]
    low = [(50 - .6 * lip, 143), (38 - lip, 148), (32 - lip, 160), (36, 172), (46, 178), (42, 190), (42, 204),
           (52, 218), (75, 228), (120, 236), (170, 244), (205, 252), (212, 275), (214, 300)]
    low = [(x, y + (dy if i < 8 else dy * .6 if i == 8 else dy * .3 if i == 9 else 0)) for i, (x, y) in enumerate(low)]
    lo_inc = [(51, 146 + dy), (55, 146 + dy), (59, 158 + dy), (60, 176 + dy), (53, 176 + dy), (49, 160 + dy)]
    under = [(233, 205), (222, 212), (195, 214), (160, 210), (125, 200), (95, 186), (75, 172), (65, 163)]
    under = [(x, y + fade(x)) for x, y in under] + [U[0]]
    lips_mid = (50 - .6 * lip, 141.5 + dy / 2)

    hl = []
    if hi == "fam":
        hl.append(_fill(_m(lips_mid) + " " + _l(ROOF[0]) + " " + _cr(ROOF) + " " + _cr(UVULA, 0, 3) + " " +
                        _l(U[11]) + " " + _cr(U[11::-1]) + " Z"))
    elif hi == "jawf":
        hl.append(_fill(_m(lips_mid) + " " + _l(ROOF[0]) + " " + _cr(ROOF) + " " + _cr(UVULA, 0, 3) + " " +
                        _l((271, 138), (272, 150), (273, 200), (273, 226), (256, 226), (257, 270), (237, 270),
                           (236, 218)) + " " + _cr(U[::-1]) + " Z"))
    elif hi == "halq":
        hl.append(_fill(_m((226, 126)) + " " +
                        _l((271, 126), (272, 150), (273, 200), (273, 226), (256, 226), (257, 270), (237, 270),
                           (236, 218), (233, 205)) + " " + _cr(U[15:10:-1]) + " Z"))
    elif hi == "khayshum":
        hl.append(_fill(_sp(NASAL_TOP) + " " + _l((264, 80), (266, 98), (252, 110)) + " " +
                        _cr(PALATE_TOP, 0, 8) + " " + _l((42, 88), (32, 82), (30, 74), (40, 58), (54, 42)) + " Z"))
    elif hi == "adna_halq":
        hl.append(_fill(_poly([(225, 128), (271, 128), (272, 182), (234, 182), (233, 165), (230, 146), (224, 134)])))
    elif hi == "wasat_halq":
        hl.append(_fill(_poly([(234, 184), (272, 184), (273, 226), (256, 226), (236, 218), (233, 206)])))
        hl.append(_fill(_sp(EPIGLOTTIS) + " Z", ".8"))
    elif hi == "aqsa_halq":
        hl.append(_fill(_poly([(237, 262), (257, 262), (257, 282), (237, 282)])))
    elif hi == "lahah":
        hl.append(_fill(_sp(UVULA) + " Z", ".8"))
    elif hi in ROOF_PARTS:
        hl.append(_line(_sp(ROOF, *ROOF_PARTS[hi])))
    elif hi in TONGUE_PARTS:
        hl.append(_line(_sp(U, *TONGUE_PARTS[hi]), 6))
    elif hi is not None:
        raise KeyError(hi)

    parts = hl + [
        _path(_sp(NOSE + up_lip)),                                     # nose and upper lip
        _path(_sp(low)),                                               # lower lip, chin, neck
        _path(_sp(NASAL_TOP)), _path(_sp(BACK_WALL)),                  # nasal roof, back of the throat
        _path(_sp(ROOF) + " " + _cr(UVULA) + " " + _cr(PALATE_TOP)),   # palate and uvula
        _path(_poly(UP_INCISOR)), _path(_poly(lo_inc)),                # front teeth
        _path(_sp(U) + " " + _cr(under) + " Z"),                       # tongue
        _path(_sp(EPIGLOTTIS) + " Z"),
        _path("M236,218 L237,300 M256,226 L257,300"),                  # larynx
        _path(_poly([(237, 267), (248, 272), (237, 277)]) + " " + _poly([(256, 267), (250, 272), (256, 277)]),
              ' fill="currentColor"' if hi != "aqsa_halq" else f' fill="{ACC}" stroke="{ACC}"'),
    ]
    if arrow:
        mouth = [(x, (_interp(ROOF, x) + _interp(U[:12], x)) / 2) for x in (214, 190, 160, 130, 100, 76)]
        end = (22 - lip, 141.5 + dy / 2)
        pts = [(247, 266), (250, 230), (253, 190), (252, 158), (238, 134)] + mouth + [lips_mid, end]
        a = math.atan2(end[1] - pts[-2][1], end[0] - pts[-2][0])
        head = [end, (end[0] - 8 * math.cos(a + .45), end[1] - 8 * math.sin(a + .45)),
                (end[0] - 8 * math.cos(a - .45), end[1] - 8 * math.sin(a - .45))]
        parts += [_path(_sp(pts), f' stroke="{ACC}" stroke-width="2" stroke-dasharray="5 4"'),
                  _path(_poly(head), f' fill="{ACC}" stroke="{ACC}"')]
    return _svg("10 5 280 300", 280, 300, parts)


# ---------------------------------------------------------------- tongue from above
TT_UP = [(286, 18), (250, 15), (190, 16), (130, 19), (88, 26), (58, 38), (40, 52), (31, 66), (29, 75)]
TT = TT_UP + [(x, 150 - y) for x, y in reversed(TT_UP[:-1])]
MID_ZONES = {"ras": (29, 40), "taraf": (40, 88), "wasat": (88, 170), "aqsa": (170, 235), "jidhr": (235, 286)}
EDGE_ZONES = {"hafah": (1, 7), "aqsa_hafah": (1, 4), "adna_hafah": (4, 6), "muntaha_hafah": (6, 7)}


def tongue_top(hi=None):
    mirror = lambda ps: [(x, 150 - y) for x, y in ps]
    parts = []
    if hi in MID_ZONES:
        a, b = MID_ZONES[hi]
        if hi == "ras":
            parts.append(f'<ellipse cx="36" cy="75" rx="8" ry="11" fill="{ACC}" fill-opacity=".55" stroke="none"/>')
        else:
            parts.append(f'<rect x="{a + 1}" y="62" width="{b - a - 2}" height="26" rx="8" fill="{ACC}" '
                         f'fill-opacity=".45" stroke="none"/>')
    elif hi in EDGE_ZONES:
        a, b = EDGE_ZONES[hi]
        parts += [_line(_sp(TT_UP, a, b), 6), _line(_sp(mirror(TT_UP), a, b), 6)]
    elif hi is not None:
        raise KeyError(hi)
    parts += [
        _path(_sp(TT)),
        _path("M286,18 L286,132", ' stroke-dasharray="4 4" opacity=".6"'),   # the root runs on, down the throat
        _path("M29,75 L286,75", ' stroke-dasharray="2 4" opacity=".45"'),     # middle line
        _path("".join(f"M{x},68 L{x},82 " for x in (40, 88, 170, 235)), ' opacity=".6"'),
        '<text x="14" y="79" text-anchor="middle" font-size="10" fill="currentColor" stroke="none">front</text>',
    ]
    return _svg("0 0 300 150", 300, 150, parts)


# ---------------------------------------------------------------- teeth
TEETH_MM = [(8.5, 7), (6.5, 6.5), (7.5, 8), (7, 9), (6.5, 9), (10, 11), (9, 11), (8.5, 10)]  # width along the arch, depth
TEETH_GROUPS = {"thanaya": [0], "rabaiyat": [1], "anyab": [2], "dawahik": [3], "tawahin": [4, 5, 6], "nawajidh": [7]}


def teeth(hi=None):
    s, gap, c = 3.0, 3.0, 80.0
    arc = lambda x: c / 2 * ((x / (c / 2)) * math.hypot(1, x / (c / 2)) + math.asinh(x / (c / 2))) / 2
    def x_at(L):
        lo, hi_ = 0.0, 200.0
        for _ in range(50):
            mid = (lo + hi_) / 2
            lo, hi_ = (mid, hi_) if arc(mid) < L else (lo, mid)
        return lo
    groups = TEETH_GROUPS.get(hi, []) if hi else []
    if hi and hi not in TEETH_GROUPS:
        raise KeyError(hi)
    parts, pos = [], gap / 2
    for k, (md, bl) in enumerate(TEETH_MM):
        w, h = md * s, bl * s
        x = x_at(pos + w / 2)
        pos += w + gap
        ang = math.degrees(math.atan(x / (c / 2)))
        rx = w * .45 if k == 2 else min(w, h) * .3
        style = f' fill="{ACC}" fill-opacity=".6" stroke="{ACC}"' if k in groups else ""
        for sx in (1, -1):
            cx, cy = 150 + sx * x, 34 + x * x / c
            parts.append(f'<rect x="{-w / 2:.1f}" y="{-h / 2:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{rx:.1f}" '
                         f'transform="translate({cx:.1f},{cy:.1f}) rotate({sx * ang:.1f})"{style}/>')
    parts.append('<text x="150" y="14" text-anchor="middle" font-size="10" fill="currentColor" stroke="none">'
                 'front</text>')
    return _svg("0 0 300 230", 300, 230, parts)
