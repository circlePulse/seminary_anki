# Draft — scan of 2026-11-09 (39 new notes)

Status: **approved 2026-11-09 and delivered.**

Source: Notion's change history since the 11-06 scan. Changed: IOK Arabic (a new ṣarf section, irregular verbs) and
Python (APIs, 2D lists, IDs). Arbaʿīn/Qudūrī, Riyāḍ and World Religions have nothing new; World Religions' 11/03
heading still holds only a placeholder.

## Check this first

1. **Takhfīf follows the vowel before the hamzah.** Your note says the hamzah changes "depending on the harak on
   it", but the hamzah being lightened is sākin. It becomes the long vowel of the letter before it: aʾmana becomes
   āmana. The card says "the vowel before it".
2. **"A waw can be attached"** is read as: after wa- or fa-, the hamzah of mur and sal comes back (wa-ʾmur, wa-sʾal).
   Kul and khudh never take it back. Tell me if your teacher meant something else.
3. **Your `get_api_results` returns the text, not the dictionary.** It calls `json.loads(response_text)` and throws
   the result away, then returns `response_text`. It should end `return json.loads(response_text)`. The cards
   describe the steps correctly and don't quote the function.
4. **"Until you change one of them"** needs splitting in two, so there are two cards. Assigning to one name again
   separates them (pyth-267). Changing the object through one name, as with append, does not: both
   still see it (pyth-266).
5. **The memory diagrams are new,** per your note asking for visual examples. Each is drawn inside the card, so it
   needs no image file and follows light and dark mode. The sample image shows one. A dashed arrow is where a name
   used to point.

## Decisions you should know about

- **The word nāqiṣ now has two senses in your decks:** the defective verb in ṣarf, and kāna and her sisters in naḥw.
  The ṣarf card carries a small "ṣarf" label, as do mithāl and ṣaḥīḥ, and there's a card contrasting the two senses.
- **Added from what I know:**
  - The weak letters themselves (alif, wāw, yāʾ), and that the doubled verb's matching letters are the second and third.
  - An example verb for each kind, and the English names: assimilated, hollow, defective.
  - The four amr forms (kul, khudh, mur, sal) and the two Qurʾān examples.
  - On the Python side: `id()`, the urlencode example with its `+`, indexing a 2D list, and the `bump` card, which
    follows from your notes on integers and on parameters.
- **Not carded:** that your book keeps to the rules that occur in Ḥafṣ. It describes the book, not the grammar.
- **All Tier 1.**

## Ṣarf: irregular verbs (23)

| id | Type | Front | Back |
|---|---|---|---|
| sarf-324 | cloze | For ṣarf, the Arabic letters fall into three groups: {{c1::the hamzah}}, {{c2::the weak letters, <bdi>حُرُوف العِلَّة</bdi>}} and {{c3::the sound letters, <bdi>حُرُوف صَحِيحَة</bdi> — all the rest}} | The weak letters are <bdi>ا</bdi>, <bdi>و</bdi> and <bdi>ي</bdi>. |
| sarf-325 | bidir | <bdi>حَرْف العِلَّة</bdi> (ḥarf al-ʿillah) | a weak letter: <bdi>ا</bdi>, <bdi>و</bdi> or <bdi>ي</bdi> |
| sarf-326 | bidir | <bdi>صَحِيح</bdi> (ṣaḥīḥ), of a verb | a regular, “sound” verb — no hamzah, no doubled letter and no weak letter among its roots |
| sarf-327 | basic | How do some grammarians use <bdi>صَحِيح</bdi> and <bdi>سَالِم</bdi> differently from the class? | For them <bdi>صَحِيح</bdi> is any verb that isn't <bdi>مُعْتَلّ</bdi>, and <bdi>سَالِم</bdi> is the sub-type that matches the class's <bdi>صَحِيح</bdi> |
| sarf-328 | cloze | The irregular verbs are of three kinds: {{c1::<bdi>مَهْمُوز</bdi>}}, {{c2::<bdi>مُضَاعَف</bdi>}} and {{c3::<bdi>مُعْتَلّ</bdi>}} | With a hamzah; with a doubled letter; with a weak letter. |
| sarf-329 | bidir | <bdi>مَهْمُوز</bdi> (mahmūz) | a verb with a hamzah among its root letters, such as <bdi>أَكَلَ</bdi> |
| sarf-330 | basic | How is the <bdi>مَهْمُوز</bdi> divided? | By which root letter is the hamzah: the fāʾ, as in <bdi>أَكَلَ</bdi>; the ʿayn, as in <bdi>سَأَلَ</bdi>; or the lām, as in <bdi>قَرَأَ</bdi> |
| sarf-331 | bidir | <bdi>مُضَاعَف</bdi> (muḍāʿaf), also <bdi>مُضَعَّف</bdi> | a doubled verb: its second and third root letters are the same, such as <bdi>مَدَّ</bdi> |
| sarf-332 | bidir | <bdi>مُعْتَلّ</bdi> (muʿtall) | a weak verb: one with a weak letter among its roots |
| sarf-333 | cloze | The kinds of <bdi>مُعْتَلّ</bdi>: {{c1::<bdi>مِثَال</bdi>}}, {{c2::<bdi>أَجْوَف</bdi>}}, {{c3::<bdi>نَاقِص</bdi>}}, {{c4::<bdi>لَفِيف مَقْرُون</bdi>}} and {{c5::<bdi>لَفِيف مَفْرُوق</bdi>}} | The weak letter is first, second or third; then two weak letters, side by side or apart. |
| sarf-334 | bidir | <bdi>مِثَال</bdi> (mithāl) | an assimilated verb: its first root letter is weak, such as <bdi>وَعَدَ</bdi> |
| sarf-335 | bidir | <bdi>أَجْوَف</bdi> (ajwaf) | a hollow verb: its second root letter is weak, such as <bdi>قَالَ</bdi> |
| sarf-336 | bidir | <bdi>نَاقِص</bdi> (nāqiṣ) | a defective verb: its third root letter is weak, such as <bdi>دَعَا</bdi> |
| sarf-337 | bidir | <bdi>لَفِيف مَقْرُون</bdi> (lafīf maqrūn) | a verb with two weak letters side by side: the ʿayn and the lām, such as <bdi>طَوَى</bdi> |
| sarf-338 | bidir | <bdi>لَفِيف مَفْرُوق</bdi> (lafīf mafrūq) | a verb with two weak letters apart: the fāʾ and the lām, such as <bdi>وَقَى</bdi> |
| sarf-339 | basic | <bdi>نَاقِص</bdi> means one thing of a verb in ṣarf and another in naḥw. What are they? | In ṣarf, a verb whose third root letter is weak, like <bdi>دَعَا</bdi>. In naḥw, an incomplete verb — <bdi>كَانَ</bdi> and her sisters — which needs a khabar. |
| sarf-340 | basic | Which two changes can apply to the hamzah of a <bdi>مَهْمُوز</bdi> verb? | <bdi>تَخْفِيف</bdi> (takhfīf), lightening it, and <bdi>حَذْف</bdi> (ḥadhf), dropping it |
| sarf-341 | bidir | <bdi>تَخْفِيف</bdi> (takhfīf) or <bdi>تَسْهِيل</bdi> (tashīl), of the hamzah | lightening the hamzah: changing it to <bdi>ا</bdi>, <bdi>و</bdi> or <bdi>ي</bdi> to match the vowel before it |
| sarf-342 | basic | When must a hamzah be lightened, and when is it optional? | It must be when two hamzahs meet and the second is sākin: <bdi>أَأْمَنَ</bdi> becomes <bdi>آمَنَ</bdi>. A single sākin hamzah may be: <bdi>رَأْس</bdi> can be read <bdi>رَاس</bdi>. |
| sarf-343 | bidir | <bdi>حَذْف</bdi> (ḥadhf) | dropping a letter from a word |
| sarf-344 | basic | In the amr of which four verbs is the hamzah most often dropped? | <div class="arabic">أَكَلَ ، أَخَذَ ، أَمَرَ ، سَأَلَ</div> |
| sarf-345 | cloze | The amr of <bdi>أَكَلَ</bdi> is {{c1::<bdi>كُلْ</bdi>}}; of <bdi>أَخَذَ</bdi>, {{c2::<bdi>خُذْ</bdi>}}; of <bdi>أَمَرَ</bdi>, {{c3::<bdi>مُرْ</bdi>}}; of <bdi>سَأَلَ</bdi>, {{c4::<bdi>سَلْ</bdi>}} | Each drops its hamzah. |
| sarf-346 | basic | For which of <bdi>كُلْ</bdi>, <bdi>خُذْ</bdi>, <bdi>مُرْ</bdi> and <bdi>سَلْ</bdi> does the hamzah stay dropped everywhere, and for which only at the start of speech? | Everywhere for <bdi>كُلْ</bdi> and <bdi>خُذْ</bdi>. For <bdi>مُرْ</bdi> and <bdi>سَلْ</bdi> only at the start: after <bdi>وَ</bdi> or <bdi>فَ</bdi> the hamzah usually returns, as in <bdi>وَأْمُرْ أَهْلَكَ بِالصَّلَاةِ</bdi> (20:132) and <bdi>وَاسْأَلِ القَرْيَةَ</bdi> (12:82). |

## Python: APIs, 2D lists, IDs and memory (16)

| id | Type | Front | Back |
|---|---|---|---|
| pyth-254 | basic | What is an API? | A way for programs to ask something questions programmatically. It isn't only for the web: programs that only ever run on one computer use APIs too. |
| pyth-255 | basic | Why would a program ask a web API rather than fetch a website's page? | The raw source of a modern, rich website runs to thousands and thousands of lines. An API answers the program's question directly, often as JSON. |
| pyth-256 | basic | In what format does a web API often respond, and how does Python read it? | JSON. The <code>json</code> module's <code>json.loads()</code> converts JSON text into Python data types: dictionaries, lists and so on. |
| pyth-257 | basic | Which module does URL (percent) encoding in Python, and what do you pass its <code>urlencode</code>? | <code>urllib.parse</code>. <code>urlencode</code> takes a list of tuples, one <code>(name, value)</code> pair per query parameter. |
| pyth-258 | basic | What does this return?<pre class="code">urllib.parse.urlencode([('q', 'lakers clippers'), ('maxResults', 10)])</pre> | <code>'q=lakers+clippers&amp;maxResults=10'</code> — each pair becomes <code>name=value</code>, joined by <code>&amp;</code>. Here the space is encoded as <code>+</code>, which in a query string means the same as <code>%20</code>. |
| pyth-259 | cloze | Accessing a web API, end to end: {{c1::build the URL, encoding the query parameters with <code>urlencode</code>}}; {{c2::make a <code>Request</code> and pass it to <code>urlopen</code>}}; {{c3::read the response and decode it as UTF-8}}; {{c4::convert the JSON text with <code>json.loads</code>}}; and {{c5::close the response, in a <code>finally</code> block}} |  |
| pyth-260 | basic | What is a 2D list? | A list in which each element is a list, as in <code>grid = [[1, 2, 3], [4, 5, 6]]</code> |
| pyth-261 | basic | What does this print?<pre class="code">grid = [[1, 2, 3], [4, 5, 6]]<br>print(grid[1][0])</pre> | <code>4</code> — <code>grid[1]</code> is the second inner list, and <code>[0]</code> is its first element |
| pyth-262 | basic | What does every object in a running Python program have, and what is guaranteed about it? | An ID, which <code>id()</code> returns. No two objects alive at the same time ever share one. *[diagram]*  |
| pyth-263 | basic | What happens in memory here?<pre class="code">x = 5<br>x += 1</pre> | The integer <code>5</code> isn't changed. <code>x</code> is re-attached to a different object, <code>6</code>, so <code>id(x)</code> changes. *Before:* *[diagram]*  *After <code>x += 1</code>:* *[diagram]*  |
| pyth-264 | basic | How does a list hold its items in memory? | It holds references, not the items themselves: each element points to an object, which can live anywhere else in memory and be as large as it likes. *[diagram]*  |
| pyth-265 | basic | What does this print, and why?<pre class="code">a = [1, 2]<br>before = id(a)<br>a.append(3)<br>print(id(a) == before)</pre> | <code>True</code> — appending changes the list in place. It's still the same object, so its ID doesn't change. *Before:* *[diagram]*  *After <code>a.append(3)</code>:* *[diagram]*  |
| pyth-266 | basic | What does this print, and why?<pre class="code">a = [1, 2]<br>b = a<br>b.append(3)<br>print(a)</pre> | <code>[1, 2, 3]</code> — <code>b = a</code> copies nothing. Both names point at the same list, so a change made through one shows through the other. *[diagram]*  |
| pyth-267 | basic | What does this print, and why?<pre class="code">a = [1, 2]<br>b = a<br>b = [9]<br>print(a)</pre> | <code>[1, 2]</code> — assigning to <code>b</code> again re-attaches it to a new object. <code>a</code> still points at the first list, which nothing changed. *[diagram]*  |
| pyth-268 | basic | What does this print, and why?<pre class="code">def add_zero(nums):<br>    nums.append(0)<br><br>scores = [7, 8]<br>add_zero(scores)<br>print(scores)</pre> | <code>[7, 8, 0]</code> — passing a list to a function doesn't copy it. <code>nums</code> is another name for the caller's list, so the function changed a variable outside itself. *[diagram]*  |
| pyth-269 | basic | What does this print, and why?<pre class="code">def bump(n):<br>    n += 1<br><br>x = 5<br>bump(x)<br>print(x)</pre> | <code>5</code> — <code>n += 1</code> re-attaches <code>n</code> to a new object, <code>6</code>. Nothing changed the <code>5</code> that <code>x</code> points at. *[diagram]*  |
