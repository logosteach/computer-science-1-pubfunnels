# Five Lessons: Building a Basic Tkinter GUI Application

By the end of these five lessons, students will be able to create a basic GUI application that includes:
- A menu system
- An Entry widget (single-line text field)
- A Text widget (multi-line text box)
- Clickable buttons with event-driven behavior

---

## Lesson 1 – The Tkinter Window & Your First Widgets

**Goal:** Students can create a window, add labels and a simple button, and control basic layout with `pack()`.

**Content**
- Importing `tkinter` and creating the root window
- `title()`, `geometry()`, and `mainloop()`
- `Label` widget
- Basic `Button` (no real functionality yet)
- `pack()` geometry manager (side, fill, expand, padx/pady)

**Key Outcome:** A window that displays a greeting and a non-functional button.

---

## Lesson 2 – Event-Driven Buttons

**Goal:** Students understand that buttons are event sources and can attach behavior to them.

**Content**
- The `command=` parameter
- Defining simple callback functions
- Updating a `Label` from a button click
- Disabling/enabling buttons
- Brief introduction to `bind()` for completeness (focus stays on `command=`)

**Key Outcome:** Buttons that actually do something when clicked (change text, show messages, etc.).

---

## Lesson 3 – Text Input Widgets: Entry & Text

**Goal:** Students can collect and display text from both single-line and multi-line widgets.

**Content**
- `Entry` widget (single-line text field)
  - `.get()`, `.insert()`, `.delete()`
- `Text` widget (multi-line text box)
  - `.get("1.0", "end")`, `.insert()`, `.delete()`
- Connecting buttons to read from and write to these widgets
- Simple validation idea (e.g., checking if an Entry is empty)

**Key Outcome:** A small form with an Entry, a Text area, and buttons that transfer or clear text between them.

---

## Lesson 4 – Layout & Building a Coherent Interface

**Goal:** Students can arrange multiple widgets cleanly and begin thinking in terms of a complete interface.

**Content**
- Switching to (or mixing) the `grid()` geometry manager
- Using `Frame` widgets to group related controls
- Combining Entry + Text + multiple Buttons in one window
- Making the interface resize reasonably
- Simple state management (keeping track of what the user has typed)

**Key Outcome:** A well-organized window that already looks and behaves like a real mini-application (still without menus).

---

## Lesson 5 – Menus + Putting It All Together

**Goal:** Students add a full menu system and assemble everything into one cohesive basic application.

**Content**
- Creating a menubar with `Menu`
- Adding cascades (`File`, `Edit`, `Help`, etc.)
- Menu items that call the same functions already written for buttons
- Keyboard accelerators (optional but nice)
- Final integration: a complete small application that uses
  - menubar
  - Entry (text field)
  - Text (text box)
  - several event-driven buttons
  - clean layout

**Key Outcome:** Students can create and explain a basic GUI application that contains a menu system, text field, text box, and clickable buttons with real event handling.