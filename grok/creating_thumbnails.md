# Lesson Thumbnail Creation Rules

Every PubFunnels lesson should have a thumbnail image. Create these from the 2nd Edition book-cover layout and palette. Do not invent a new design for each lesson.

Read `static/css/book_styles_2nd_edition.css` before drawing. Those `--ed2-*` variables are the only colors allowed on the thumbnail unless the instructor names a change.

The approved example is `unit_002_lesson_001_thumbnail.jpg` (Unit 2, Lesson 1, Order of Operations). Duplicate that layout. Change only the unit number, the lesson number, the lesson title, and the faint code in the bottom band.

---

## Size and file name

- Canvas size is always **1080 x 720** pixels (landscape). This is the PubFunnels recommended thumbnail size.
- Save as a JPEG at high quality, or PNG if the instructor asks.
- File name:

```text
unit_00N_lesson_00M_thumbnail.jpg
```

Examples: `unit_002_lesson_001_thumbnail.jpg`, `unit_005_lesson_003_thumbnail.jpg`.

- Zero-pad unit and lesson numbers to three digits.
- Place the finished file where the instructor asks. If they do not say, save it next to the other lesson assets and report the path.

---

## What to put on the thumbnail

The thumbnail is the 2nd Edition cover turned landscape. Map the cover slots like this:

| Cover slot | Thumbnail text |
|---|---|
| Where "2nd Edition" sat (coral top band) | `UNIT N` |
| Where "PYTHON" sat (gold middle band) | `LESSON M` |
| Between the two gold anchors (teal bar) | Lesson title, uppercase |

Do **not** put any of the following on a lesson thumbnail:

- "2nd Edition"
- "By John C. Partridge" or any author line
- The Hebrews 6:19 verse or any other Scripture line
- "WITH A WORLDVIEW"
- Course subtitle "The Christian Creator's Guide..."
- A grade, a duration, or a unit nickname unless the instructor asks

---

## Four-band layout (top to bottom)

Keep these four horizontal bands. Do not tilt, add perspective, or use a Star Wars crawl.

### 1. Coral top band (about 168 px)

- Fill: `--ed2-coral` `#F06024` (hot circuit marks may use `--ed2-coral-hot` `#FC5F28`).
- Texture: faint streaming binary (`0` and `1`) plus light gold circuit traces. Texture must stay behind the type.
- Type: `UNIT N` centered, white, bold, large. Example: `UNIT 2`.
- No author line above it.

### 2. Gold middle band (about 268 px)

- Fill: `--ed2-gold` `#FD9C1F`. Flat fill. No photo texture that fights the title.
- Type: `LESSON M` centered, very large, white fill, coral outline using `--ed2-coral-deep` `#E24A1C`.
- This line is the visual hero, the same role "PYTHON" has on the book.

### 3. Teal title bar (about 72 px)

- Fill: `--ed2-teal` `#1689A4`.
- Two small gold anchors (`--ed2-subtitle-gold` `#F5D36A`), one on each side of the title.
- Lesson name centered between the anchors, uppercase, gold. Example: `ORDER OF OPERATIONS`.
- Keep the title on one line if it fits. If it is long, reduce the type size before wrapping to two lines.

### 4. Aqua bottom band (remaining height, about 212 px)

- Fill: `--ed2-aqua` `#7BD2DE` with a light `--ed2-sea` `#53BFD3` wave edge at the bottom.
- Overlay faint Python code at low opacity (about 10 to 20 percent). Prefer snippets that belong to **this lesson**, not random noise.
- Do not put a Scripture caption on this band.

---

## Type and drawing rules

- Prefer Source Sans 3 (Bold / Black for UNIT and LESSON, SemiBold for the title on the teal bar).
- `LESSON M` must stay readable at thumbnail size. Give it a 3 to 4 px coral stroke so it separates from the gold field.
- Keep all type horizontal and head-on. No angled type.
- Do not let cover text from a source image show through. If you crop the 2nd Edition cover for texture, paint out "2nd Edition", the author line, PYTHON, and the verse before you add the lesson words.
- Prefer a deterministic draw (PIL or similar) over an image-generation model when the instructor needs exact type, size, and placement. Image models drift and snap captions to the bottom edge.

---

## Colors (2nd Edition only)

Use these first. Full set is in `static/css/book_styles_2nd_edition.css`.

- Coral: `#F06024`
- Coral deep (PYTHON-style outline): `#E24A1C`
- Gold: `#FD9C1F`
- Teal bar: `#1689A4`
- Aqua field: `#7BD2DE`
- Sea / wave: `#53BFD3`
- Title gold: `#F5D36A`
- White: `#FFFFFF`

Do not fall back to the first-edition navy / rust palette (`book_cover_colors.css`) unless the instructor asks for a first-edition thumbnail.

---

## How to take an order

When the instructor says "make a thumbnail for Unit X Lesson Y [title]":

1. Read this file and `static/css/book_styles_2nd_edition.css`.
2. Confirm unit number, lesson number, and official lesson title.
3. Draw 1080 x 720 with the four bands above.
4. Put lesson-specific code in the aqua band if you know the topic.
5. Save as `unit_00X_lesson_00Y_thumbnail.jpg`.
6. Report the path and the pixel size. Do not claim the file is saved until it exists.

---

## Reference

- Palette: `static/css/book_styles_2nd_edition.css`
- First-edition palette (do not use for these thumbnails): `static/css/book_cover_colors.css`
- Canonical example: Unit 2 Lesson 1 Order of Operations
