# Practice File Creation and Dual-Repo Push Rules

A practice file is a student `.py` file with comments that teach. When the instructor asks for a practice file, write it once, then publish it to **both** repositories below unless the instructor names only one destination.

Read `grok/introduction.md` first. The practice-file rules there still apply.

---

## Two repositories, two folders

| Repository | Practice folder | Example path |
|---|---|
| `logosteach/computer-science-1-pubfunnels` | `unit_00N/practice/` | `unit_002/practice/naming_variables_in_python.py` |
| `logosteach/python-with-a-worldview` | `practice/` (repo root) | `practice/naming_variables_in_python.py` |

Use the **logosteach** org copies. Do not write to `jcpartri/python-with-a-worldview` or `jcpartri/computer-science-1-pubfunnels` unless the instructor asks for the personal fork.

PubFunnels keeps practice files under the unit. The textbook repo keeps one shared `practice/` folder for all chapters.

---

## File name

- Use a clear snake_case name that matches the lesson topic.
- Examples: `order_of_operations.py`, `naming_variables_in_python.py`.
- Use the **same file name** in both repositories.
- Zero-pad the unit folder in PubFunnels: `unit_001`, `unit_002`, `unit_010`.
- If the unit folder or `practice/` folder does not exist, create it. Do not invent a parallel folder name.

---

## How to take an order

When the instructor says "create a practice file for Unit N Lesson M [topic]":

1. Read this file and `grok/introduction.md`.
2. Read the unit objectives and the matching `unit_00N/lessons/lesson_00M.html` when they exist.
3. Write one complete `.py` file that runs from top to bottom.
4. Save a working copy in the session project if needed.
5. Push the **same content** to both paths:

```text
logosteach/computer-science-1-pubfunnels   →  unit_00N/practice/<filename>.py
logosteach/python-with-a-worldview         →  practice/<filename>.py
```

6. Report both URLs and both commit SHAs. Do not claim a push succeeded unless GitHub returned a commit.

If one push fails (403 or missing permission), still finish the other path and tell the instructor which repo is waiting.

---

## Practice file shape

Start the file with a paragraph comment that states:

- Title of the practice
- Unit and lesson
- Learning objectives (observable verbs)
- Biblical connection, NKJV only, when the lesson has one
- Student instructions (predict first, complete TODOs, check solutions last)

Use comments throughout to explain. Include:

- Worked examples the student can run
- `TODO` items with a blank to fill
- Illegal syntax only inside comments so the file still runs
- A `SOLUTIONS` block at the bottom, also in comments

End the file with this exact line:

```python
# Copyright 2026 LogosTeach - All Rights Reserved
```

Also include this transparency sentence in the header comment:

```text
Labs, Practice Files and Assessments are developed in collaboration with the Grok AI assistant under instructor supervision and review.
```

Match the tone of existing files such as `unit_002/practice/order_of_operations.py`.

---

## Quality checks before you push

- Run the file. It must finish without a `SyntaxError`.
- Do not leave live lines that use illegal names (`2score`, `for = 10`, `first-name`).
- Keep student work in TODOs, not pre-filled, unless the instructor wants a key-only file.
- Scripture is NKJV. Do not invent a verse that the lesson does not use.

---

## Updates

When the instructor asks to **update** a practice file, change both copies. Do not leave PubFunnels and the textbook repo on different versions of the same filename.

If only one repo should change, the instructor will say so. Otherwise assume both.

---

## Reference copies already in place

- PubFunnels: `unit_002/practice/order_of_operations.py`
- PubFunnels: `unit_002/practice/naming_variables_in_python.py`
- Textbook: `practice/order_of_operations.py`
- Textbook: `practice/naming_variables_in_python.py`
