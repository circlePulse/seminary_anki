# Draft — scan of 2026-11-06 (92 new notes)

Status: **awaiting approval.**

Source: Notion's change history since the 11-03 scan. Changed: Python (HTTP), Arbaʿīn Ḥadīth 9 and 10, and Qudūrī's
Kitāb al-Ṣalāh. World Religions has only an empty 11/03 heading so far. Arabic and Riyāḍ are unchanged. Your Arbaʿīn
to-do now reads "Arba'in 1-10 test on 11/18 (no memorization needed)".

## Check this first

1. **The muʾadhdhin turns right for ḥayya ʿalā al-ṣalāh and left for ḥayya ʿalā al-falāḥ.** Your notes have it the
   other way round. The card has right first, as Qudūrī says.
2. **ʿIshāʾ is best delayed until just before a third of the night has passed.** Your notes say 2/3, but the ḥadīth and
   Qudūrī have a third.
3. **The Shāfiʿī ʿawrah of a man is between the navel and the knee, with neither included.** Your notes say "above
   the knee to above the navel".
4. **The adhān without wuḍūʾ:** Qudūrī allows it, and it's the iqāmah without wuḍūʾ that he calls disliked. The card
   says both.
5. **The 300 status codes** are redirects, mostly, as well as "something is off".
6. **The Ḥadīth 9 and 10 translations are mine,** as before. They're in `texts/arbaeen_h09.md` and `h10.md` with the
   matn. Three cards rest on them.

## Decisions you should know about

- **Not carded:** that tarjīʿ is "pretty much only done in remote areas of Yemen nowadays", which I can't confirm.
- **Added from what I know:** example URLs and requests on the Python cards, %20 for percent encoding, 4:103 for the
  prayer times, and the ahl al-ṣuffah gloss.
- **All Tier 1.**

## Python: HTTP (22)

| id | Type | Front | Back |
|---|---|---|---|
| pyth-232 | basic | What does HTTP stand for, and what is it used for? | Hypertext Transfer Protocol — fetching the documents you see in a browser |
| pyth-233 | basic | What kind of protocol is HTTP? | Request-response: a client connects and the server accepts; the client sends a request, and the server sends back a response |
| pyth-234 | basic | What is a URL? | A uniform resource locator: where a piece of information you want is |
| pyth-235 | cloze | A URL gives first the {{c1::scheme}}, which says which protocol is used; then the {{c2::host}}, plus optionally a {{c3::port}}; and after the slash, the {{c4::document or resource}} you want | In <code>http://www.example.com:8000/index.html</code>: scheme <code>http</code>, host <code>www.example.com</code>, port <code>8000</code>, resource <code>/index.html</code>. |
| pyth-236 | basic | What are HTTP verbs, and which is the simplest? | Words that describe what you want done; the simplest is <code>GET</code> |
| pyth-237 | cloze | The first line of an HTTP request: the {{c1::verb}}, a space, {{c2::the rest of the URL after the scheme, host and port}}, a space, and {{c3::the protocol version}} | For example, <code>GET /index.html HTTP/1.1</code>. |
| pyth-238 | basic | What are HTTP headers, and how is each one written? | Extra information after the first line — think of them as parameters. Each is a word, a colon, a space, then the information. |
| pyth-239 | basic | Which header is required in an HTTP request, and how does a request show it has ended? | <code>Host</code>; and a blank line ends the request |
| pyth-240 | basic | How does an HTTP response begin? | With the protocol, then the status code — such as the famous 404 — and then some headers |
| pyth-241 | cloze | HTTP status codes: the 200s, {{c1::everything is fine}}; the 300s, {{c2::something is off — usually a redirect}}; the 400s, {{c3::the client did something wrong}}; the 500s, {{c4::the server did something wrong}} | From the server's side the 500s are “I did something wrong”, and the 400s “you did”. |
| pyth-242 | basic | Which HTTP version is in plain human-readable text, and which is the latest? | HTTP/1.1 is plain text; HTTP/3 is the latest |
| pyth-243 | basic | What does HTTPS add to HTTP? | It's secure HTTP, which most web servers use: the same protocol, but the requests and responses are encrypted, and the server proves to the client that it is who it says it is |
| pyth-244 | basic | Under HTTPS, how does a server prove who it is? | A trusted authority vouches for it. Authorities vouch for each other, in a chain that ends at a root certificate built into the OS, which is trusted implicitly. |
| pyth-245 | basic | Which part of Python's library makes HTTP requests, and how do you make one? | <code>urllib.request</code>. Create a <code>Request</code>, initialised with a URL, and pass it to <code>urlopen</code>, which gives back a response object. |
| pyth-246 | basic | On a response object, what do <code>.status</code>, <code>.headers</code> and <code>.close()</code> do? | <code>.status</code> gives the status code; <code>.headers</code> gives the headers and acts like a dictionary; <code>.close()</code> closes the response |
| pyth-247 | basic | What does this print?<pre class="code">for x in response.headers:
    print(f'{x}: {response.headers[x]}')</pre> | Each header of the response, one per line, as <code>Name: value</code> |
| pyth-248 | basic | What does <code>response.read()</code> return, and how do you turn it into a <code>str</code>? | All the response's content, as <code>bytes</code> — Python may display it like a string, but it's still bytes. Call <code>.decode()</code>, passing the encoding as a keyword argument: in this class, probably <code>utf-8</code>. |
| pyth-249 | basic | How do you turn a <code>str</code> into <code>bytes</code>? | Call <code>.encode()</code> on it, with the encoding |
| pyth-250 | basic | How can Python serve the current directory over HTTP on localhost? | <code>python3 -m http.server {port}</code> |
| pyth-251 | basic | Why isn't the page you get from a YouTube search a file in a directory? | Web pages aren't just files in a directory any more: the URL carries your query, and the page is built for it |
| pyth-252 | cloze | After the {{c1::<code>?</code>}} in a URL come the query parameters, separated by {{c2::<code>&amp;</code>}}; each has a name and a value, separated by {{c3::<code>=</code>}} | As in <code>/results?search_query=cats</code>. |
| pyth-253 | basic | What is percent encoding? | The URL's escape sequences: a <code>%</code> followed by a character's code, as in <code>%20</code> for a space |

## Arbaʿīn Ḥadīth 9 and 10 (32)

| id | Type | Front | Back |
|---|---|---|---|
| arbh-327 | basic | Who narrates the ḥadīth “what I have forbidden you, avoid” (Arbaʿīn 9)? | Abū Hurayrah RA |
| arbh-328 | basic | What was Abū Hurayrah's full name, and what does “Abū Hurayrah” mean? | ʿAbd al-Raḥmān ibn Ṣakhr. It means “father of the kitten”, a nickname the Prophet ﷺ gave him. |
| arbh-329 | basic | When did Abū Hurayrah RA accept Islam, and which group of Companions was he among? | In 7 AH, the year of Khaybar. He was one of <bdi>أَهْل الصُّفَّة</bdi> (ahl al-ṣuffah), the poor Companions who lived at the Prophet's ﷺ mosque. |
| arbh-330 | basic | How many aḥādīth did Abū Hurayrah RA narrate? | 5,374 — the most of anyone |
| arbh-331 | cloze | Why Arbaʿīn 9 matters: al-Nawawī counts it among {{c1::the important principles of the dīn}}; it is from {{c2::<bdi>جَوَامِع الكَلِم</bdi>}}; and it stresses {{c3::holding to the teachings of the Sunnah}} | None |
| arbh-332 | basic | What was the background to the ḥadīth “what I have forbidden you, avoid”? | The Prophet ﷺ said that Ḥajj is obligatory. Someone asked whether it was every year, and he stayed silent three times; then he said that had he said yes, it would have become obligatory, and too hard. So: don't ask about what he has left unspecified. |
| arbh-333 | basic | In the ḥadīth “what I have forbidden you, avoid” (Arbaʿīn 9), what does the Prophet ﷺ say to do with what he forbade and with what he commanded? | “What I have forbidden you, avoid; and what I have commanded you, do of it as much as you are able” |
| arbh-334 | basic | In the ḥadīth “what I have forbidden you, avoid”, what does “avoid what I have forbidden” cover? | Both the disliked and the outright ḥarām, from the Qurʾān and the Sunnah. Avoiding them is important, and rewarded. |
| arbh-335 | basic | In the ḥadīth “what I have forbidden you, avoid”, what does “do as much of it as you can” cover, and why only as much as we can? | Both the encouraged and the obligatory, from the Qurʾān and the Sunnah. We are weak by nature and not perfect, but we're required to give our best effort. |
| arbh-336 | basic | What two causes of earlier nations' downfall does the ḥadīth “what I have forbidden you, avoid” name? | Excessive questioning — unnecessary, or meant to avoid an obligation, like the Banū Isrāʾīl and the cow — and disagreeing with their prophets |
| arbh-337 | basic | How do scholars rank avoiding prohibitions against following commands? | As equally important, or even more important |
| arbh-338 | basic | What is the best way to draw closer to Allah, according to the notes on Arbaʿīn 9? | Obeying His commands, above all the obligations: the best way to grow in His love and attain His mercy. The first focus is the obligations, and the most important of them is the prayer. |
| arbh-339 | basic | What does <bdi>لَا يُكَلِّفُ اللَّهُ نَفْسًا إِلَّا وُسْعَهَا</bdi> (2:286) refer to, according to the notes on Arbaʿīn 9? | Religious obligations, not trials — it is probably the most misquoted verse of the Qurʾān |
| arbh-340 | basic | Why is “we're not required to be perfect” not an excuse to skip acts we don't like? | Because we all have the capacity to obey Allah's commands. Allah wants ease for us, not hardship (2:185), and the religion is ease — but that ease is the capacity to obey. |
| arbh-341 | basic | What does Arbaʿīn 9 teach about asking questions? | Some questions are useless or have an ulterior purpose; good questions are encouraged |
| arbh-342 | basic | Who narrates the ḥadīth “Allah is good and accepts only what is good” (Arbaʿīn 10)? | Abū Hurayrah RA |
| arbh-343 | basic | Why is the ḥadīth “Allah is good and accepts only what is good” one of the foundations of Islam? | It describes deeds and their intention, and it stresses lawful sustenance |
| arbh-344 | bidir | <bdi>طَيِّب</bdi> (ṭayyib) | good, pure, wholesome and healthy; as Allah's attribute, pure and perfect, free of any shortcoming |
| arbh-345 | basic | Which deeds does Allah accept, according to the ḥadīth “Allah is good and accepts only what is good”? | Only the good and pure: a deed must be sincere, and done according to the Sharīʿah. Ostentation and arrogance are impurities. |
| arbh-346 | bidir | <bdi>قَبُول الإِصَابَة</bdi> (qabūl al-iṣābah) | acceptance of a deed as correct: the legal obligation is fulfilled, as in praying properly |
| arbh-347 | bidir | <bdi>قَبُول الإِثَابَة</bdi> (qabūl al-ithābah) | acceptance of a deed with reward: earning Allah's pleasure, so that two correct prayers can differ greatly in reward |
| arbh-348 | basic | The prayer of someone who drinks wine is “not accepted for forty days”. Which acceptance does it lack? | Qabūl al-ithābah: the prayer is correct (iṣābah) but earns no reward |
| arbh-349 | basic | What does Ibn Rajab say is ṭayyib in the believer? | His whole being: his heart, through the faith in it; his tongue, through remembrance; and his body, through righteous deeds, the fruits of faith |
| arbh-350 | basic | In the ḥadīth “Allah is good and accepts only what is good” (Arbaʿīn 10), what does the Prophet ﷺ say Allah commanded the believers, and which verses does he recite? | What He commanded the messengers: “O messengers, eat of the good things and do righteous deeds” (23:51) and “O you who believe, eat of the good things We have provided you” (2:172) |
| arbh-351 | basic | In those two verses, what are the ṭayyibāt? | What Allah has allowed us to eat and consume |
| arbh-352 | basic | Whose duʿāʾ, in the ḥadīth “Allah is good and accepts only what is good”, will not be answered, despite everything that should help it? | A man who travels far, dishevelled and dusty, stretching his hands to the sky — “O Lord, O Lord!” — while his food, drink and clothing are unlawful and he has been nourished by the unlawful |
| arbh-353 | cloze | What helps a duʿāʾ be accepted: {{c1::after the five daily prayers}}, {{c2::the last third of the night}}, {{c3::between the adhān and the iqāmah}}, {{c4::travelling}}, {{c5::sickness}}, {{c6::hardship}} and {{c7::being oppressed}} | None |
| arbh-354 | basic | What prevents a duʿāʾ from being answered, according to the notes on Arbaʿīn 10? | Consuming, wearing or being sustained by the impermissible. If we don't answer Allah's call, how will He answer ours? |
| arbh-355 | basic | How does “halal and ṭayyib” compare with halal alone, and what is the ruling on seeking lawful income? | It's a higher standard: lawful, and also pure, wholesome and healthy. Seeking a lawful income is farḍ. |
| arbh-356 | basic | How does unlawful food affect us, according to the notes on Arbaʿīn 10? | Spiritually: as some foods harm the body, unlawful food harms the soul |
| arbh-357 | basic | If a duʿāʾ seems unanswered, what might be happening instead? | It may be bad for us; Allah may give it later; He may reward, bless and raise us instead; He may give it in the hereafter; or it may expiate our sins |
| arbh-358 | basic | When will a duʿāʾ be answered, according to the notes on Arbaʿīn 10? | When it asks for something lawful, with full faith in Allah, and avoids the things that block it |

## Qudūrī: Kitāb al-Ṣalāh (38)

| id | Type | Front | Back |
|---|---|---|---|
| qud-348 | basic | What does the Qurʾān say about the prayer times, and who specified them? | The prayer is prescribed for the believers at fixed times (4:103). Jibrīl specified them: he led the Prophet ﷺ in prayer on two days, once at the start of each time and once at its end, and said the time is what lies between. |
| qud-349 | basic | When does the Fajr time begin and end? | It begins at true dawn (<bdi>الفَجْر الصَّادِق</bdi>, also called the second dawn) and ends at sunrise, just as the disk breaks the horizon. One shouldn't pray while the sun is rising. |
| qud-350 | basic | How do false dawn and true dawn differ? | False dawn (<bdi>الفَجْر الكَاذِب</bdi>, the first) is a vertical white light that appears and then disappears. True dawn comes 15–20 minutes later, as a horizontal light. |
| qud-351 | basic | When does the Ẓuhr time begin? | At zawāl, when the sun passes its zenith |
| qud-352 | basic | When does Ẓuhr end and ʿAṣr begin, according to Abū Ḥanīfah, and according to the majority? | Abū Ḥanīfah: when an object's shadow is twice its length. The majority, the Ṣāḥibān among them: when it equals its length. Neither counts the shadow at zawāl. |
| qud-353 | basic | Given the disagreement over the end of Ẓuhr, what do the Ḥanafī scholars recommend? | Out of caution, to pray Ẓuhr within the majority's time and ʿAṣr after Abū Ḥanīfah's — a recommendation, not binding |
| qud-354 | basic | When does the ʿAṣr time end? | At sunset, just before the whole disk disappears below the horizon |
| qud-355 | basic | When does the Maghrib time end, and how do Abū Ḥanīfah and the majority differ? | When the twilight disappears: the white twilight, for Abū Ḥanīfah; the red, for the majority and the Ṣāḥibān. It goes by what people see where they are, so a valley and a mountain differ. |
| qud-356 | basic | What are the times of ʿIshāʾ and of Witr? | ʿIshāʾ runs from the end of Maghrib until just before Fajr. Witr ends at the same time, but begins only once one has prayed ʿIshāʾ. |
| qud-357 | basic | What is the recommended time for Fajr in the Ḥanafī school, and how did Imam Muḥammad reconcile the views? | Delayed until al-isfār, when there's a little light, not total darkness. The Shāfiʿīs and Mālikīs prefer the opposite, and both have narrations. Imam Muḥammad: begin in the dark and pray long enough that it grows light. |
| qud-358 | basic | When is Ẓuhr best prayed, in summer and in winter? | In summer, after waiting for it to cool a little; in winter, early |
| qud-359 | basic | Until when is it recommended to delay ʿAṣr? | For as long as the sun hasn't changed — in colour, or in becoming easy to look at |
| qud-360 | basic | What is recommended for Maghrib, and what follows from it? | To hasten it — which is why the Ḥanafīs say there's no sunnah prayer between its adhān and iqāmah |
| qud-361 | basic | Until when is it recommended to delay ʿIshāʾ? | Until just before a third of the night has passed — the night being Maghrib to Fajr, in thirds. The Prophet ﷺ said that if it weren't a burden, he would have made this time obligatory. |
| qud-362 | basic | When is Witr best prayed? | At the end of the night, for someone who prays at night; before sleeping, for someone not in the habit or unsure of waking. It should be the last prayer of the day. |
| qud-363 | basic | Someone prays Witr, sleeps, and then wakes in the night. What does he do? | Pray tahajjud, without praying Witr again |
| qud-364 | bidir | <bdi>الأَذَان</bdi> (al-adhān) | the call to prayer — linguistically the announcement, technically a specific announcement at specific times |
| qud-365 | basic | What is the ruling on the adhān, and for which prayers? | Sunnah muʾakkadah, for the five daily prayers and Jumuʿah, and no others. It's recommended even for someone praying alone, out loud. |
| qud-366 | bidir | <bdi>التَّرْجِيع</bdi> (tarjīʿ) | saying the two shahādahs quietly and then loudly in the adhān — not in the Ḥanafī adhān, nor in Bilāl's, but a sunnah for the Shāfiʿīs |
| qud-367 | basic | What does the adhān of Fajr add, and where? | After <bdi>حَيَّ عَلَى الفَلَاحِ</bdi>: <bdi>الصَّلَاةُ خَيْرٌ مِنَ النَّوْمِ</bdi>, twice |
| qud-368 | basic | How does the iqāmah differ from the adhān? | It's the same, except that after <bdi>حَيَّ عَلَى الفَلَاحِ</bdi> it adds <bdi>قَدْ قَامَتِ الصَّلَاةُ</bdi>, twice. The Shāfiʿīs and Ḥanbalīs say its phrases once. |
| qud-369 | basic | At what pace are the adhān and the iqāmah said? | The adhān slowly and measured; the iqāmah quickly |
| qud-370 | basic | Which way does the muʾadhdhin face, and where does he turn? | Towards the qiblah, though it isn't obligatory. He turns his face to the right for <bdi>حَيَّ عَلَى الصَّلَاةِ</bdi> and to the left for <bdi>حَيَّ عَلَى الفَلَاحِ</bdi>. |
| qud-371 | basic | Someone has missed several prayers. How does he make the adhān and iqāmah for them? | Both for the first; after that, both, or just the iqāmah |
| qud-372 | basic | Why does Qudūrī write <bdi>فَاتَتْهُ صَلَوَاتٌ</bdi>, making the prayers the subject — “prayers escaped him”? | Out of adab |
| qud-373 | basic | What is the ruling on giving the adhān and iqāmah without wuḍūʾ, or in major impurity? | Best in ritual purity. Without wuḍūʾ it's allowed, though Qudūrī singles out the iqāmah as disliked; giving the adhān in major impurity is disliked. |
| qud-374 | basic | Which adhān may be given before its time begins? | Fajr's, according to Abū Yūsuf; no other |
| qud-375 | bidir | <bdi>الشَّرْط</bdi> (sharṭ), in fiqh | a precondition: the existence of something depends on it, but it lies outside its essence |
| qud-376 | basic | What are the shurūṭ of the prayer, as a group? | All farḍ, and required for the prayer to be valid, but not part of the prayer itself |
| qud-377 | cloze | The shurūṭ of the prayer: {{c1::purity from ritual and physical impurity}}, {{c2::covering the ʿawrah}}, {{c3::the intention}}, {{c4::the time having entered}}, {{c5::facing the qiblah}} and {{c6::the taḥrīmah}} | None |
| qud-378 | bidir | <bdi>العَوْرَة</bdi> (al-ʿawrah) | the parts of the body that must be covered |
| qud-379 | basic | What is a man's ʿawrah, for the Ḥanafīs and for the Shāfiʿīs? | For the Ḥanafīs, from below the navel to below the knee, so the knee is included. For the Shāfiʿīs, what's between the navel and the knee, with neither included. |
| qud-380 | basic | What is a free woman's ʿawrah, and what do the Ḥanafīs also exclude? | Everything except the face and hands; the Ḥanafīs also exclude the feet |
| qud-381 | basic | What is a female slave's ʿawrah? | A man's, plus the belly and back — so her hair, and below her knees, are not ʿawrah |
| qud-382 | basic | How does someone with nothing to cover the ʿawrah pray? | Sitting, gesturing for rukūʿ and sujūd with movements of the head. Standing suffices, but sitting is much better. |
| qud-383 | basic | Someone can't find anything to remove an impurity with. What does he do? | He prays with it, and doesn't repeat the prayer |
| qud-384 | basic | What must the intention for the prayer be like, and must it be said aloud? | Made for the prayer, with no gap between it and the start of the prayer. Saying it aloud is neither sunnah nor required. |
| qud-385 | basic | What is the taḥrīmah, and what is discussed about it? | Saying Allāhu akbar to begin the prayer; whether it's a rukn or a sharṭ |
