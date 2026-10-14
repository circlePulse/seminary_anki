# Draft — ICS H32, Functions to Tests (86 new notes)

Status: **awaiting approval.**

Source: the topic toggles after *Loops* on the Python page (Functions, Scope, Format strings, Tuple, Sequence
assignment, List, Type annotations, Files, Failure, Networking, Tests), as fetched on 2026-10-14. The page has no
dates, so the session tag `oct14` is the carding date, as `sep30` was for the last batch.

## Corrections to your notes (on the cards only)

- **Slicing:** "leaving out the stop defaults to -1" is wrong: `x[3:-1]` leaves out the last element. An omitted
  stop runs to the end of the list. The card's extra says so.
- **Writing a file:** it's opening the file in `'w'` mode that empties it. Each `.write()` then adds its string at
  the cursor, rather than overwriting the file each time.
- **Return-type arrow:** the arrow is typed `->`; Notion turned yours into →.
- **Socket input:** your notes say `makefile('r')` is for sending data. `'r'` gives the input side; `'w'` is for
  sending.

## Decisions you should know about

- **Two facts added, one each from standard Python, where the notes stop short:**
  - A function with no `return` gives back `None`.
  - `.readline()` returns `'\n'` for an empty line, which is why an empty string means the end of the file.
- **Not carded:**
  - Asides: "people don't often like to do testing", "the opposite of opening it, what did you expect", "pretty
    self-explanatory".
  - Statements having side effects, already pyth-038 and pyth-039.
- **Two-way choices that would give themselves away** (argument or parameter, client or server, listening or
  connecting) are basic cards that ask for both sides.
- **All Tier 1.**

## Cards

| id | Type | Front | Back |
|---|---|---|---|
| pyth-107 | basic | Why break a problem into functions that know as little about each other as possible? | To avoid the “avalanche of complexity” — each small piece stays understandable on its own |
| pyth-108 | basic | Which keyword defines a function? | <code>def</code> |
| pyth-109 | basic | What is the difference between an argument and a parameter? | An argument is what you pass into a function; it lands inside the function as a parameter |
| pyth-110 | basic | What happens when a <code>return</code> statement is reached? | Its expression is evaluated, and control goes back to whatever called the function, carrying that value |
| pyth-111 | basic | What does a function give back if it never reaches a <code>return</code>? | <code>None</code> — a function always returns a value |
| pyth-112 | basic | What does this print?<pre class="code">def f():<br>    return 1<br><br>print(f)</pre> | Something like <code>&lt;function f at 0x…&gt;</code> — naming a function without parentheses is legal; it gives the function object and its memory address, without calling it |
| pyth-113 | basic | Which argument types will Python accept for a function's parameters? | Any — as long as what the function does with them is legal |
| pyth-114 | basic | What is a docstring? | A string literal as the first line of a function, describing what it does |
| pyth-115 | basic | What does a long, complicated docstring suggest? | That the function is doing too much |
| pyth-116 | cloze | A docstring longer than one line uses {{c1::<code>'''</code>, a multi-line string literal}}; you read a docstring back with {{c2::<code>function_name.__doc__</code>}} |  |
| pyth-117 | basic | When must a function be defined, relative to its use? | Before it is called |
| pyth-118 | basic | When a name exists both globally and locally, which one does Python use? | The most local one |
| pyth-119 | cloze | Python looks a name up in this order: {{c1::local}}, {{c2::enclosing}}, {{c3::global}}, {{c4::built-in}} | LEGB |
| pyth-120 | basic | What is the enclosing scope? | With nested functions: the local scope of the function in which the inner function is defined |
| pyth-121 | basic | Which variables are local to a function call? | Every variable assigned inside it, its parameters included — local to that one call |
| pyth-122 | basic | What does this print?<pre class="code">q = 1<br><br>def f():<br>    print(q)<br>    q = 2<br><br>f()</pre> | Nothing — it raises <code>UnboundLocalError</code>. Python parses the whole function first, sees <code>q</code> assigned, and treats it as local throughout; at the print it exists but has no value yet. |
| pyth-123 | basic | What does this print?<pre class="code">name = 'Boo'<br>print(f'Hi {name}')</pre> | <code>Hi Boo</code> — an <code>f</code> before a string literal lets you put values into it in braces |
| pyth-124 | basic | What is a tuple? | An immutable sequence of values, of any mixture of types |
| pyth-125 | basic | What does it mean that a tuple is immutable, and what else behaves that way? | You can't change it — you build a new one instead, just as with a string |
| pyth-126 | basic | What does it mean that a tuple is a sequence? | The order of its values matters |
| pyth-127 | basic | When is a tuple the natural choice? | When, before the program runs, you know how many values you need and what each one is |
| pyth-128 | basic | How do you write a tuple literal, and when do you need the parentheses? | Expressions separated by commas: <code>('Boo', 11, 3.5)</code>. Parentheses are needed where it would otherwise be ambiguous — in a function call, where commas separate arguments. |
| pyth-129 | basic | Which operations does a tuple share with a string? | Taking its length with <code>len()</code>, and indexing with <code>[]</code> |
| pyth-130 | basic | What does this print?<pre class="code">point = 34, 28<br>x, y = point<br>print(y)</pre> | <code>28</code> — sequence assignment unpacks anything iterable into a matching sequence of variables |
| pyth-131 | basic | How do you swap two variables in one line? | <code>a, b = b, a</code> |
| pyth-132 | basic | What is a list, and how is it written differently from a tuple? | A mutable sequence of objects, written in square brackets: <code>[1, 2, 3]</code> |
| pyth-133 | basic | What does this print?<pre class="code">x = [1, 2, 3, 4, 5]<br>print(x[-1])</pre> | <code>5</code> — a negative index counts from the end: <code>[0]</code> is the first element, <code>[-1]</code> the last |
| pyth-134 | basic | What does <code>.append()</code> do to a list? | Adds one element to the end — changing the list itself |
| pyth-135 | basic | What does this print?<pre class="code">x = [1, 2]<br>x.append([3, 4])<br>print(x)</pre> | <code>[1, 2, [3, 4]]</code> — appending a list nests it as a single element, since an element can be of any type |
| pyth-136 | basic | How do you add another list's elements to a list, rather than nesting the list? | <code>.extend()</code>, or <code>+=</code> — a concatenation, as with strings |
| pyth-137 | basic | How do you replace one element of a list, and how do you delete one? | Assign by index, <code>x[3] = 5</code>; delete with <code>del x[5]</code> |
| pyth-138 | basic | What does calling <code>list()</code> on an iterable do? | Builds a new list from its values |
| pyth-139 | basic | What does this print?<pre class="code">x = [0, 1, 2, 3, 4, 5, 6, 7, 8]<br>print(x[3:7])</pre> | <code>[3, 4, 5, 6]</code> — like a range, a slice's start is inclusive and its stop exclusive |
| pyth-140 | cloze | In a slice, leaving out the start means {{c1::from index 0}}; leaving out the stop means {{c2::to the end of the list}}; the optional third value is {{c3::the step, as in a range}} | Your notes say the stop defaults to -1, but <code>x[3:-1]</code> leaves out the last element. An omitted stop runs to the end. |
| pyth-141 | basic | What does this print?<pre class="code">x = [1, 2, 3]<br>print(x[::-1])</pre> | <code>[3, 2, 1]</code> — a negative step walks backwards, so this builds a reversed copy (ranges can step backwards too) |
| pyth-142 | basic | What do type annotations do, and what don't they do? | They state your intentions about types; Python doesn't enforce them — it's dynamically typed, and types are dealt with as the program runs |
| pyth-143 | basic | What can be given a type annotation? | Variables, function parameters, function return types, and more |
| pyth-144 | basic | If annotations aren't enforced, what makes them useful? | Tools such as VS Code flag code that contradicts them |
| pyth-145 | basic | From when are type annotations required in ICS H32? | From Project 1 |
| pyth-146 | basic | How do you annotate a parameter and a return type? | A colon and the type after the parameter, and <code>-&gt;</code> and the type after the parameter list: <code>def f(x: int) -&gt; str:</code> |
| pyth-147 | basic | After an annotation's colon, what can you technically write, and what should you write? | Any legal Python expression — but you should write a type, such as <code>str</code> |
| pyth-148 | cloze | Annotating a value that may be one of several types: {{c1::<code>int &#124; float</code>}}; a tuple: {{c2::<code>tuple[type1, type2]</code>}}; a list: {{c3::<code>list[int]</code>, naming its elements' type}}; a list of mixed elements: {{c4::<code>list[int &#124; float]</code>}} |  |
| pyth-149 | basic | What is a file? | A container in which a sequence of bytes is stored — the basic abstraction of a file system |
| pyth-150 | basic | What is a byte? | A sequence of eight bits, each either 1 or 0 |
| pyth-151 | basic | What do file names mean to the computer? | Nothing — they mean something only to humans. A name ending in <code>.jpg</code> is essentially a guess about the contents. |
| pyth-152 | basic | What does <code>\n</code> stand for in Python? | An abstraction of whatever the system uses to mark a newline — which differs between systems |
| pyth-153 | basic | Why clean data the moment it comes into your program? | Then you never have to deal with it later, and the rest of the program can focus on its own job |
| pyth-154 | basic | What does <code>open()</code> take, and what does it return? | A path, absolute or relative, and a mode — 'r' to read or 'w' to write, as text. It returns a file object. |
| pyth-155 | basic | What is pathlib's <code>Path</code> for? | You pass it a string, and it works out the right path for your system |
| pyth-156 | basic | What does the <code>/</code> operator do with a <code>Path</code>? | Appends to it — joining on the next part of the path |
| pyth-157 | cloze | On a <code>Path</code>: {{c1::<code>.exists()</code>}} says whether it's on your machine; {{c2::<code>.is_file()</code> and <code>.is_dir()</code>}} say what kind it is; {{c3::<code>.open()</code>}} opens it as <code>open()</code> does; {{c4::<code>.iterdir()</code>}} gives an iterable over a directory's contents |  |
| pyth-158 | basic | How do you get a directory's contents as a list? | Pass the iterable to the list constructor: <code>list(p.iterdir())</code> |
| pyth-159 | basic | What does a file object's <code>.mode</code> tell you? | Which mode it was opened in — read or write |
| pyth-160 | basic | What happens if you open a file that doesn't exist in 'w' mode? | It's created |
| pyth-161 | basic | Why close a file as soon as you no longer need it? | An open file can affect how other programs can access it |
| pyth-162 | basic | Why can data you wrote to a file be lost, and what prevents it? | Writes go to a buffer in memory, written out only when it fills, so a program that stops early can lose them. <code>.close()</code> saves them; <code>.flush()</code> empties the buffer on demand. |
| pyth-163 | basic | What, physically, is a “line” in a text file? | Nothing in itself — just characters that tell software to show a line break |
| pyth-164 | basic | What does <code>.readline()</code> return, and what does it do to the file's cursor? | The text from the cursor up to and including the next newline, if there is one — and it moves the cursor to the next line |
| pyth-165 | basic | What does it mean when <code>.readline()</code> returns an empty string? | You're at the end of the file — an empty line still gives <code>'\n'</code> |
| pyth-166 | basic | What does opening a file in 'w' mode do to it, and what does <code>.write()</code> then do? | Opening in 'w' empties the file; each .write() then adds the string you pass it at the cursor |
| pyth-167 | basic | What kinds of failure can hit a program that is itself correct? | Failures from outside it — a file that can't be opened, bad input |
| pyth-168 | basic | What is an exception? | An object that represents failure |
| pyth-169 | basic | What does a traceback show? | Where the problem happened, and how the program got to that line — traced outward through the calls |
| pyth-170 | basic | What does a function return when it raises an exception? | No value at all |
| pyth-171 | basic | What happens to the rest of a <code>try</code> block when a statement in it raises an exception? | It's skipped — you leave the try block immediately |
| pyth-172 | cloze | After <code>try:</code>, <code>except</code> runs {{c1::if an exception is raised}}; <code>else</code> runs {{c2::after the try block, if no exception was raised}}; <code>finally</code> runs {{c3::after the try block, no matter what happened}} |  |
| pyth-173 | basic | How do you narrow an <code>except</code> clause, and why should you? | Name the type of exception after it — exceptions fall into categories. Specific clauses can be chained, and being specific is better. |
| pyth-174 | basic | How do you raise an exception yourself? | <code>raise</code> with a type and a message: <code>raise ValueError('Bad input!')</code> |
| pyth-175 | basic | What is a socket? | One end of a connection, provided by the operating system — like a tin can on a string, with a socket at the other end |
| pyth-176 | basic | What two streams does a socket have? | An input stream and an output stream |
| pyth-177 | basic | What ordering does the course rely on for messages over a connection? | They arrive in the order they were sent, or not at all — even though the pieces may be received out of order |
| pyth-178 | basic | Why are networked programs more fallible than local ones? | External circumstances can break the connection |
| pyth-179 | basic | Of two programs on a connection, which is the client and which the server? | The one that establishes the connection is the client, connecting; the one that accepts it is the server, listening |
| pyth-180 | basic | What is the loopback address? | <code>127.0.0.1</code> — your own machine |
| pyth-181 | basic | What is a port, and what range do port numbers cover? | A number naming one place on a machine where a program might be listening — 0 to 65535, that is 2¹⁶ values. Some ports are standard. |
| pyth-182 | basic | How do you create a socket in Python? | <code>import socket</code>, then <code>socket.socket()</code> |
| pyth-183 | basic | How does a client connect, and how do you know it worked? | Call <code>connect((host, port))</code> with a tuple; it worked if no exception was raised |
| pyth-184 | basic | How do you get file-like objects for a socket's two streams? | <code>makefile('r')</code> for input and <code>makefile('w')</code> for output — pseudo-file objects |
| pyth-185 | basic | How do you send a line through a socket's output file, and why the second step? | <code>.write()</code> the string, then <code>.flush()</code> so the buffer is actually sent |
| pyth-186 | basic | What does <code>.readline()</code> on a socket's input do to newline sequences? | It collapses them back to <code>\n</code> |
| pyth-187 | basic | In what order do you close a socket connection? | The input, then the output, then the socket |
| pyth-188 | basic | How do you know when something you're writing is done, and what's the better way to check? | Run it and see if it works — better, automate it: write programs that test your programs |
| pyth-189 | basic | What does an <code>assert</code> statement do? | States something you believe to be true; if it's false, an exception — <code>AssertionError</code> — is raised |
| pyth-190 | basic | What does this print?<pre class="code">assert 10 &gt; 8, 'making sure the universe still maths'</pre> | Nothing — the condition is true. If it were false, an <code>AssertionError</code> with that message would be raised. |
| pyth-191 | basic | How do you test that code raises the exception you expect? | <pre class="code">try:<br>    remove_all([1, 3, 5, 7, 8], 99)<br>    assert False, 'ValueError should have been raised'<br>except ValueError:<br>    pass</pre>Put an <code>assert False</code> after the call that should fail, and catch the expected exception. |
| pyth-192 | basic | What will the course teach later about tests? | How to separate tests from the code |
