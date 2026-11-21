"""Leech fixes for the naṣīḥah cards (Arbaʿīn 7), 2026-11-21.
  python3 drafts/nasihah_2026-11-21.py OUTDIR   write the changed deck to OUTDIR/x/ and the draft report
  python3 drafts/nasihah_2026-11-21.py --write  rewrite decks/arbaeen_ahadith.json (after approval)
Fixes: long multi-idea deletions become short one-idea deletions; two-question cards are split; long list answers
are cut to their core or asked as "any three of"; near-identical answers are told apart. Rewritten cards get the
tag relearn-nov21, so the user can Forget and unsuspend them in one go. Card types never change (an import cannot
switch an existing note's type), and no card is removed (ids are append-only)."""
import json, re, sys, os
W = sys.argv[1] == "--write"
P = "decks/arbaeen_ahadith.json"
raw = open(P).read(); d = json.loads(raw); assert json.dumps(d, ensure_ascii=False, indent=1) == raw.rstrip("\n")
C = {c["id"]: c for c in d["cards"]}
B = lambda s: f"<bdi>{s}</bdi>"
TAG = "relearn-nov21"
before = {i: json.loads(json.dumps(c)) for i, c in C.items()}
changed, NEW = [], []

def edit(i, **f):
    c = C[i]
    for k, v in f.items():
        assert k in c, (i, k); c[k] = v
    if c["type"] == "cloze": c["extra"] = ""
    if TAG not in c["tags"]: c["tags"] = c["tags"] + [TAG]
    changed.append(i)

def new(origin, **f):
    o = C[origin]; c = {"tier": 1, "tags": [t for t in o["tags"] if t != TAG]}
    for k in ("session", "source"):
        if k in o: c[k] = o[k]
    c.update(f)
    if c["type"] == "cloze": c["extra"] = ""
    NEW.append((origin, c))

# narrator: one fact per card
edit("arbh-271", back="Tamīm ibn Aws al-Dārī RA")
new("arbh-271", type="basic", front="What is Tamīm al-Dārī RA's kunya?", back="Abū Ruqayyah")
edit("arbh-272", front="What was Tamīm al-Dārī RA's religion before Islam?", back="Christianity")
new("arbh-272", type="basic", front="In what year did Tamīm al-Dārī RA accept Islam?", back="9 AH")
edit("arbh-275", front="In what year did Tamīm al-Dārī RA die?", back="40 AH")

# the two definitions of naṣīḥah: tell them apart instead of recalling two near-identical wordings
edit("arbh-280", front="Whose definition of naṣīḥah is “seeking good, or improvement, for the other person”?", back="Ibn Ḥajar's")

# naṣīḥah to Allah
edit("arbh-282", back="Believing in Him, and denying Him any partners")
edit("arbh-283", text="Naṣīḥah to Allah also means {{c1::following His commands}} and {{c2::avoiding His prohibitions}}, "
     "{{c3::remembering Him}} in every circumstance, {{c4::thanking Him}} for His blessings, and being {{c5::sincere}} in worship")
edit("arbh-291", front="What kind of relationship do we have with Allah, according to the lesson on Arbaʿīn 7?",
     back="Servant and Lord: one of submission, obedience and sincerity")
edit("arbh-292", front="What is the foundation of our relationship with Allah?", back="Love")
new("arbh-292", type="basic", front="Love of Allah shows itself through which two feelings?", back="Hope and fear")
edit("arbh-293", back="Learning about Him, reflecting on His blessings, and thanking Him")

# naṣīḥah to the Qurʾān
edit("arbh-284", front="What must one believe about the Qurʾān's nature, as naṣīḥah to Allah's Book?",
     back="That it is Allah's uncreated word")
new("arbh-284", type="cloze", text="The Qurʾān is the {{c1::greatest miracle}} ever given, and {{c2::inimitable}}: nothing like it can ever be produced")
edit("arbh-285", front="Name any three things naṣīḥah to the Qurʾān asks of us in practice.",
     back="Any three of: reciting it regularly, learning it, teaching it, reflecting on its meanings, acting on it, showing it outward respect")
edit("arbh-294", back="Islam's beliefs, the relationship between man and his Creator, and the rules sent down in it")

# naṣīḥah to the Messenger ﷺ
edit("arbh-286", text="Naṣīḥah to the Messenger ﷺ: believing he is Allah's {{c1::final}} messenger; {{c2::loving}} and "
     "{{c3::honouring}} him; {{c4::following}} what he told us; adopting {{c5::the character the Sunnah teaches}}; loving "
     "{{c6::his household and Companions}}; and taking him as {{c7::a role model}} in every aspect of life")
edit("arbh-295", front="The lesson on Arbaʿīn 7 calls the Prophet ﷺ the physical manifestation of what?",
     back="The Qurʾān — he is the most perfect example of a human being")
edit("arbh-296", front="What is the foundation of our relationship with the Prophet ﷺ?", back="Love, with honour, respect and reverence")
new("arbh-296", type="cloze", text="Our relationship with the Prophet ﷺ is nurtured by {{c1::learning about him}}, "
    "{{c2::following his Sunnah}} and {{c3::sending abundant salutations on him}}")

# naṣīḥah to the leaders
edit("arbh-287", text="Naṣīḥah to the leaders of the Muslims: obeying them {{c1::in the truth}}; {{c2::reminding them of the truth}}; "
     "advising them of {{c3::what they have neglected}}; reminding them of {{c4::the Muslims' rights}}; not "
     "{{c5::rebelling against them with the sword}}; {{c6::praying behind them}}; and {{c7::supplicating for their correction}}")
edit("arbh-297", front="What is our default relationship with those in authority?", back="Obedience, though not absolute")
new("arbh-297", type="basic", front="What limits obedience to those in authority?",
    back=f"There is no obedience to the creation in disobedience to the Creator: {B('لَا طَاعَةَ لِمَخْلُوقٍ فِي مَعْصِيَةِ الخَالِقِ')}")
edit("arbh-298", front="Why do Muslim citizens follow the law of the land by default?",
     back="Order, peace and security in society are among Islam's priorities")
new("arbh-298", type="basic", front="Up to what point do Muslim citizens follow the law of the land?",
    back="As long as it doesn't infringe personal rights or religious freedoms")

# naṣīḥah to the common folk, and to others
edit("arbh-289", text="Naṣīḥah to the common folk: guiding them to {{c1::what sets their affairs right in both lives}}; "
     "protecting them from {{c2::harm}} and helping them {{c3::in need}}; {{c4::ordering good and forbidding evil}}, kindly "
     "and sincerely; showing them {{c5::mercy}}, honouring their elders and being kind to the young; and {{c6::not cheating them}}, but supporting them")
edit("arbh-290", back="Giving each its due rights and responsibilities")
new("arbh-290", type="basic", front="In each of the five relationships of Arbaʿīn 7, what should one stress more than one's rights, and why?",
    back="One's responsibilities: it nurtures the relationship and makes it stronger")
edit("arbh-300", back="As a major component of its teachings: Islam is not individualistic")
edit("arbh-301", text="How we must treat others: with respect, {{c1::kindness}} and care; sympathy, {{c2::compassion}} and "
     "generosity; love, {{c3::mercy}} and forgiveness")
edit("arbh-281", text=C["arbh-281"]["text"])   # only its extra goes (the cloze rule); the tag lets it be found too
C["arbh-281"]["tags"].remove(TAG)

n = max(int(c["id"].split("-")[1]) for c in d["cards"] if c["id"].startswith("arbh-"))
for origin, c in NEW:
    n += 1; c["id"] = f"arbh-{n:03d}"; d["cards"].append(c)
d["expected_count"] = len(d["cards"])
out = json.dumps(d, ensure_ascii=False, indent=1) + ("\n" if raw.endswith("\n") else "")
if W:
    open(P, "w").write(out)
else:
    os.makedirs(sys.argv[1] + "/x", exist_ok=True); open(sys.argv[1] + "/x/arbaeen_ahadith.json", "w").write(out)
    strip = lambda s: re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", s or "")).strip()
    show = lambda c: (f"Front: {strip(c['front'])} / Back: {strip(c['back'])}" if c["type"] == "basic" else f"Cloze: {strip(c['text'])}")
    L = ["# Draft — leech fixes for the naṣīḥah cards (2026-11-21)", "", "Status: **awaiting approval.**", "",
         f"Rewritten cards get the tag {TAG}. After importing, search the browser for tag:{TAG}, select all, then Forget them and unsuspend them (Anki suspends leeches).", "",
         f"## Rewritten ({len(changed) - 1}, plus arbh-281 losing its extra)", ""]
    for i in changed:
        if i == "arbh-281": continue
        L += [f"- **{i}**", f"  - Was: {show(before[i])}", f"  - Now: {show(C[i])}"]
    L += ["", f"## New ({len(NEW)})", ""] + [f"- **{c['id']}** (split from {o}): {show(c)}" for o, c in NEW]
    open("drafts/draft_2026-11-21_nasihah.md", "w").write("\n".join(L) + "\n")
    print(len(changed), "changed,", len(NEW), "new")
