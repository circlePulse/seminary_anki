"""Audit 2026-11-17: apply the cloze-extra and term-coverage rules to the older decks.
  python3 drafts/audit_2026-11-17.py OUTDIR   writes the changed decks to OUTDIR/x/ and the draft report
  python3 drafts/audit_2026-11-17.py --write  rewrites decks/*.json in place (after approval)"""
import json, glob, re, sys, os
W = sys.argv[1] == "--write"
OUT = None if W else sys.argv[1]
AR = lambda s: f'<div class="arabic">{s}</div>'
B = lambda s: f"<bdi>{s}</bdi>"
strip = lambda s: re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", s or "")).strip()

decks = {f[6:-5]: (f, open(f).read()) for f in sorted(glob.glob("decks/*.json")) if not f.endswith("hafs.json")}
D = {}
for k, (f, raw) in decks.items():
    d = json.loads(raw); assert json.dumps(d, ensure_ascii=False, indent=1) == raw.rstrip("\n"); D[k] = d
C = {c["id"]: (k, c) for k, d in D.items() for c in d["cards"]}

# 1. every cloze extra goes
cleared, orig = {}, {c["id"]: c.get("extra") for d in D.values() for c in d["cards"]}
for k, d in D.items():
    for c in d["cards"]:
        if c["type"] == "cloze" and strip(c.get("extra")):
            c["extra"] = ""; cleared.setdefault(k, []).append(c["id"])

sys.path.insert(0, "skill/scripts")
from wrap_arabic import wrap_field, _strip_added
wrapped = []
for k, ids in cleared.items():
    for i in ids:
        c = C[i][1]; w = wrap_field(c["text"])
        if w != c["text"]:
            assert _strip_added(w) == _strip_added(c["text"]).replace("<bdi>", "").replace("</bdi>", "") or \
                   re.sub(r"</?bdi>", "", w) == re.sub(r"</?bdi>", "", c["text"]), i
            c["text"] = w; wrapped.append(i)

# 2. labels the cloze needs move into its text
EDITS = [("arbh-053", '<div class="arabic">', 'The opening of Ḥadīth 3:<div class="arabic">'),
         ("arbh-141", '<div class="arabic">', 'The Kalām definition of īmān:<div class="arabic">'),
         ("arbh-213", "enters the fetus: ", "enters the fetus include: "),
         ("sarf-219", '<div class="arabic">', f'With {B("نُون التَّوْكِيد الثَّقِيلَة")}:<div class="arabic">'),
         ("wrel-192", "sayings about women: ", "sayings about women (Analects 17.25): "),
         ("wrel-221", "The Daodejing: ", "The Daodejing (ch. 3): "),
         ("wrel-225", "The Daodejing on where", "The Daodejing (ch. 8) on where"),
         ("wrel-250", "The Daodejing: ", "The Daodejing (ch. 44): "),
         ("wrel-259", "ideal people ", "ideal people (ch. 80) "),
         ("wrel-277", "from the Daodejing: ", "from the Daodejing (ch. 2): ")]
for i, a, b in EDITS:
    c = C[i][1]; assert c["text"].count(a) == 1, i; c["text"] = c["text"].replace(a, b, 1)

# 3. terms, translations and facts that had no card of their own: new cards, inheriting the origin card's
#    session, source and tags
NEW = []
def new(origin, card, sci=None):
    k, o = C[origin]
    card.update(tier=1, tags=o["tags"])
    for f in ("session", "source"):
        if o.get(f, D[k].get(f)): card[f] = o.get(f, D[k].get(f))
    if sci: card["science"] = sci
    NEW.append((k, origin, card))
bid = lambda o, t, m, sci=None: new(o, {"type": "bidir", "term": AR(t), "meaning": m}, sci)
bas = lambda o, f, b: new(o, {"type": "basic", "front": f, "back": b})

bid("voc-200", "عَزِيمَة", f"the ruling in its original strictness — the opposite of a {B('رُخْصَة')}")
bid("voc-372", "إِفْرَاط", f"overdoing it, going to an extreme — the opposite of {B('تَفْرِيط')}")
bid("voc-341", "تَرْهِيب", f"deterring by warning — the pair of {B('تَرْغِيب')}")
bid("voc-323", "كِهَانَة", f"soothsaying, the craft of a {B('كَاهِن')}")
bid("voc-246", "عِدَّة", "a woman's waiting period")
bid("voc-293", "تَرْجَمَة", "a biographical entry, a biography")
bid("voc-358", "أَهْل الأَهْوَاء", "the people of caprice: sects that follow their whims")
bid("voc-277", "رِيبَة", "misgiving, what unsettles the heart")
bid("voc-380", "أَكْمَلَ", "to complete, to perfect")
bid("voc-261", "أُصُول الفِقْه", "the foundations of fiqh: its legal theory")
bid("voc-263", "الفُرُوع", "the detailed rulings of fiqh, built on its foundations", "فِقْه")
bas("voc-388", f"Besides a definition, what else is a {B('حَدّ')}?", "A fixed punishment set by the Sharīʿah.")
bas("voc-109", f"Besides a need, what else can {B('إِرْب')} mean?", "A limb. The sense depends on the passage.")
bas("voc-480", f"In ḥajj and ʿumrah, what does {B('قَصَّرَ')} mean?", "To cut the hair short.")
bas("voc-370", f"In the plural, what vowel does a {B('فَعْلَة')} noun take on its ʿayn?",
    f"A fatḥah: {B('شَهْوَة')} makes {B('شَهَوَات')}, and {B('نَفْحَة')} makes {B('نَفَحَات')}.")
bas("voc-232", f"Why is this world called {B('الدُّنْيَا')}?",
    f"It is the feminine of {B('أَدْنَى')}, nearer or lower: the nearer, lower life.")
bas("voc-482", "How does al-Nawawī define istiqāmah?", f"{B('لُزُومُ طَاعَةِ اللهِ')} — holding to obedience to Allah.")
bas("voc-484", "What does al-Nawawī call istiqāmah?", f"{B('نِظَامُ الأُمُورِ')} — the order of affairs.")
bid("arbh-182", "مُتَّفَقٌ عَلَيْهِ", "related by both al-Bukhārī and Muslim")
bid("arbh-199", "حُسْن الخَاتِمَة", "a good ending to one's life")
bid("arbh-199", "سُوء الخَاتِمَة", "a bad ending to one's life")
bid("arbh-329", "أَهْل الصُّفَّة", "the poor Companions who lived at the Prophet's ﷺ mosque")
bid("arbh-262", "حِمَى", "a private pasture")
bid("arbh-174", "الصَّادِقُ المَصْدُوقُ", "the truthful, the one believed — said of the Prophet ﷺ")
bid("arbh-302", "أَخْلَاق", "character, conduct")
bid("nahw-224", "الشَّبَه الافْتِقَارِيّ", "resembling a ḥarf in dependence: needing other words to complete the meaning")
bid("nahw-225", "الشَّبَه الوَضْعِيّ", "resembling a ḥarf in form: being built of fewer than three letters")
bas("nahw-235", "Which relative pronouns are muʿrab?",
    f"Only the duals: {B('اللَّذَانِ')} and {B('اللَّتَانِ')} in rafʿ, {B('اللَّذَيْنِ')} and {B('اللَّتَيْنِ')} in naṣb and jarr. The rest are mabnī.")
bas("nahw-239", "Which demonstratives are muʿrab?",
    f"Only the duals: {B('هٰذَانِ')} and {B('هَاتَانِ')} in rafʿ, {B('هٰذَيْنِ')} and {B('هَاتَيْنِ')} in naṣb and jarr, and the far ones likewise. The rest are mabnī.")
bid("qud-349", "الفَجْر الصَّادِق", "true dawn (the second dawn)")
bid("qud-350", "الفَجْر الكَاذِب", "false dawn (the first dawn)")
bas("wrel-299", "In the Eightfold Path, what is right intention also translated as?", "Right thought.")
bas("sarf-204", "An unvowelled word fits both a place pattern and a tool pattern. Which reading should you try first, and why?",
    f"The {B('اِسْم الظَّرْف')}: it is more common than the {B('اِسْم الآلَة')}.")
for i in ("riyad-011", "riyad-013", "riyad-015", "riyad-017", "riyad-019", "riyad-021", "riyad-023", "riyad-025",
          "riyad-027", "riyad-029", "riyad-031", "riyad-033"):
    o = C[i][1]
    matn = re.sub(r"\{\{c\d+::(.*?)(?:::[^}]*)?\}\}", r"\1", re.search(r'<div class="arabic">(.*)</div>', o["text"]).group(1))
    ex = strip(orig[i])
    tr = ex[ex.index("“") + 1:]
    tr = tr.split(" — It is said")[0] if i == "riyad-033" else tr[:tr.rindex("”")]
    bas(i, "Translate:" + AR(matn), "“" + tr.rstrip("”") + "”")
bas("riyad-025", f"In Ibn ʿAbbās's ḥadīth, al-Tirmidhī's narration (Arbaʿīn 19) has a different word for {B('أَمَامَكَ')} in {B('احْفَظِ اللهَ تَجِدْهُ أَمَامَكَ')}. What is it?",
    B("تُجَاهَكَ"))

PFX = {"vocab": "voc", "arbaeen_ahadith": "arbh", "nahw": "nahw", "quduri": "qud", "riyad": "riyad", "wrel": "wrel", "sarf": "sarf"}
for k, origin, card in NEW:
    p = PFX[k]; n = max(int(c["id"].split("-")[1]) for c in D[k]["cards"] if c["id"].startswith(p + "-"))
    card["id"] = f"{p}-{n + 1:03d}"; D[k]["cards"].append(card)
for k, d in D.items():
    d["expected_count"] = len(d["cards"])
    f, raw = decks[k]
    out = json.dumps(d, ensure_ascii=False, indent=1) + ("\n" if raw.endswith("\n") else "")
    if W: open(f, "w").write(out)
    elif cleared.get(k) or any(x[0] == k for x in NEW):
        os.makedirs(f"{OUT}/x", exist_ok=True); open(f"{OUT}/x/{k}.json", "w").write(out)

if not W:   # the draft report
    show = lambda s: re.sub(r"</?bdi>", "", re.sub(r'<div class="arabic">(.*?)</div>', r" \1", s)).strip()
    L = ["# Draft — audit of the older decks against the 2026-11-17 rules", "",
         "Status: **awaiting approval.** Nothing is built yet.", "",
         "Rules checked: cloze cards carry no extra; every term, definition or translation on a card is tested by its own card or a cloze deletion.",
         "Not checked: order clozes for sequences (that needs the notes, not the decks), and one fact per card (the earlier, separate offer).", "",
         "## 1. Cloze extras cleared", "",
         f"Every cloze extra in the older decks is emptied: {sum(map(len, cleared.values()))} cards. Changed cards keep their scheduling.", "",
         "Most extras were one of four things, so nothing is lost by dropping them:",
         "- Already tested: a meaning another card tests (most vocab verb chains and plurals have a two-way card for the word or its maṣdar).",
         "- Commentary: \"Eleven in total.\", \"Two words a letter apart\", \"In the order of the ḥadīth\".",
         "- Examples and citations: example words, verses and URLs.",
         "- Spelling notes on your own word lists (\"your شاطيء…\") and alternative plurals.", "",
         "Where an extra held something untested, it became a card (section 3). Where it held a label the cloze needs, the label moved into the cloze text (section 2).", ""]
    for k, ids in cleared.items(): L.append(f"- {k} ({len(ids)}): " + ", ".join(ids))
    L += ["", f"Also: {len(wrapped)} of these clozes had Arabic not yet wrapped in <bdi> (the old backlog); since they are re-sent anyway, they are wrapped now: " + ", ".join(wrapped) + ".", "", "## 2. Labels moved into the cloze text", ""]
    for i, a, b in EDITS: L.append(f"- {i}: now opens or reads \"{show(b).strip(': ')}\"")
    L += ["", f"## 3. New cards ({len(NEW)})", "",
          "Each takes the origin card's source, session and tags. Riyāḍ translations use the wording already on the cards.", ""]
    for k, origin, c in NEW:
        body = (f"{show(c['term'])} ↔ {show(c['meaning'])}" if c["type"] == "bidir"
                else f"Front: {show(c['front'])} / Back: {show(c['back'])}")
        L.append(f"- **{c['id']}** (from {origin}{', science label: ' + c['science'] if c.get('science') else ''}): {body}")
    open("drafts/draft_2026-11-17c_audit.md", "w").write("\n".join(L) + "\n")
    print("cleared", sum(map(len, cleared.values())), "| edits", len(EDITS), "| new", len(NEW))
