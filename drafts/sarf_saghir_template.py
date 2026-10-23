#!/usr/bin/env python3
"""Sample ṣarf ṣaghīr cloze (the pattern the user supplied, on صَرَّفَ). Writes a one-card scratch deck to build/
for rendering. Nothing goes into decks/sarf.json until the user approves."""
import json

root = "/home/user/seminary_anki/"
G = lambda s: f'<span style="color: var(--muted)">{s}</span>'          # the pattern's fixed words, greyed
td = lambda s, span=1: f'<td class="arabic"{f" colspan={span}" if span > 1 else ""}>{s}</td>'


def saghir(madi, mud, masdar, fail, madi_m, mud_m, mafool, amr, nahy, zarf, zarf_is_mafool):
    """One table: the active line, the passive line, then amr, nahy and ẓarf. The māḍī stays visible as the cue.
    A form that appears twice shares its cloze number, so one copy can't give the other away."""
    z = 6 if zarf_is_mafool else 9
    rows = [
        [td(madi), td(f"{{{{c1::{mud}}}}}"), td(f"{{{{c2::{masdar}}}}}"), td(f"{G('فَهُوَ')} {{{{c3::{fail}}}}}")],
        [td(f"{G('وَ')}{{{{c4::{madi_m}}}}}"), td(f"{{{{c5::{mud_m}}}}}"), td(f"{{{{c2::{masdar}}}}}"),
         td(f"{G('فَهُوَ')} {{{{c6::{mafool}}}}}")],
        [td(f"{G('الأَمْرُ مِنْهُ')} {{{{c7::{amr}}}}}"), td(f"{G('وَالنَّهْيُ عَنْهُ')} {{{{c8::{nahy}}}}}"),
         td(f"{G('وَالظَّرْفُ مِنْهُ')} {{{{c{z}::{zarf}}}}}", 2)],
    ]
    return '<table dir="rtl" style="color: inherit">' + "".join("<tr>" + "".join(r) + "</tr>" for r in rows) + "</table>"


card = dict(type="cloze", tier=1, id="sarf-220",
            text=saghir("صَرَّفَ", "يُصَرِّفُ", "تَصْرِيفًا", "مُصَرِّفٌ", "صُرِّفَ", "يُصَرَّفُ", "مُصَرَّفٌ",
                        "صَرِّفْ", "لَا تُصَرِّفْ", "مُصَرَّفٌ", zarf_is_mafool=True),
            extra="", tags=["sarf", "sarf-saghir", "tafil"], session="oct23",
            source="Ṣarf ṣaghīr — the class pattern, 2026-10-23")
deck = json.load(open(root + "decks/sarf.json", encoding="utf-8"))
deck["cards"] = [card]; deck["expected_count"] = 1
json.dump(deck, open(root + "build/sarf_saghir_sample.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(card["text"])
