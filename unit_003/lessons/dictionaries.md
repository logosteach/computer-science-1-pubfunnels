**Python Dictionaries Video Lesson Series**  

**Target Audience:** Students with knowledge of `print()`, lists, sets, tuples, basic data types (`int`, `float`, `str`), `input()`, escape characters, and elementary `for` loops.  
**Restrictions:** No functions and no OOP in any lesson.  
**Total Lessons:** 7 (progressive from beginner to proficient)

---

### **Lesson 1: Introduction to Dictionaries – What Are They and Why Use Them?**

**Video Length:** 8–10 minutes  
**Objectives:** Understand the difference between lists/tuples and dictionaries.

**Lesson Outline:**

1. Opening Hook (0:00–0:45)
2. Real-world analogy (0:45–2:00)
3. Dictionary vs List comparison (2:00–4:30)
4. Basic syntax and first example (4:30–7:00)
5. Summary & practice challenge (7:00–end)

**Talking Points:**

- “Imagine you have a phone book. You don’t look up the 5th entry — you look up by a name. That’s exactly what a dictionary does.”
- “Lists are ordered and use numbers (indices) to find things. Dictionaries use keys (which can be strings, numbers, etc.) to find values.”
- Show side-by-side:
  
  ```python
  # List
  student_list = ["Alice", 85, "Math"]
  
  # Dictionary
  student = {"name": "Alice", "score": 85, "subject": "Math"}
  ```

- Emphasize: Dictionaries are unordered (in older Python) but [very fast for lookup](./whys_whats_and_hows/dictionaries%20are%20fast%20for%20lookup.md).
- Key vocabulary: key, value, pair, mutable.
- Practice challenge: “Create a dictionary for your favorite movie with keys: title, year, genre.”

---

### **Lesson 2: Creating Dictionaries and Accessing Values**

**Video Length:** 10–12 minutes  
**Objectives:** Learn multiple ways to create dictionaries and safely access values.

**Lesson Outline:**

1. Review from Lesson 1 (0:00–0:45)
2. Three ways to create a dictionary (0:45–3:30)
3. Accessing values with square brackets (3:30–6:00)
4. What happens if the key doesn’t exist? (6:00–8:30)
5. `get()` method introduction (8:30–10:30)
6. Mini practice (10:30–end)

**Talking Points:**

- “You can create an empty dictionary with `{}` or `dict()`.”
- Show examples:

  ```python
  person = {}                    # empty
  person = {"name": "Bob"}       # one pair
  person = dict(name="Bob", age=25)  # dict() constructor
  ```

- Accessing: `print(person["name"])` → explain KeyError danger.
- Safe access: `person.get("age")` returns `None` if missing, or you can give a default: `person.get("age", 0)`.
- Live demo: Build a small student info dictionary together using `input()`.

---

### **Lesson 3: Adding, Modifying, and Removing Items**

**Video Length:** 11 minutes  
**Objectives:** Understand dictionaries are mutable.

**Lesson Outline:**

1. Recap accessing (0:00–1:00)
2. Adding new key-value pairs (1:00–3:30)
3. Modifying existing values (3:30–5:30)
4. Removing items with `del` and `.pop()` (5:30–8:30)
5. Clearing a dictionary (8:30–9:30)
6. Practice exercises (9:30–end)

**Talking Points:**

- “Dictionaries are mutable — we can change them after creation, just like lists.”
- Code examples:
  
  ```python

  scores = {"Alice": 85}
  scores["Bob"] = 92          # add
  scores["Alice"] = 88        # modify
  del scores["Bob"]           # remove
  removed = scores.pop("Alice")  # remove and return value
  ```
- Compare `del` vs `.pop()` — `.pop()` is safer because it can return the value.
- Tip: “Think of it like editing a contact in your phone.”

---

### **Lesson 4: Dictionary Methods – Useful Tools**

**Video Length:** 12 minutes  
**Objectives:** Learn the most important built-in dictionary methods.

**Lesson Outline:**

1. Quick review of previous lessons (0:00–1:00)
2. `.keys()`, `.values()`, `.items()` (1:00–5:30)
3. `.update()` (5:30–7:30)
4. Checking if a key exists with `in` (7:30–9:30)
5. `len()` on dictionaries (9:30–10:30)
6. Practice (10:30–end)

**Talking Points:**

- Show:
  
  ```python
  player = {"name": "Mario", "lives": 3, "score": 1200}
  print(player.keys())      # dict_keys([...])
  print(player.values())
  print(player.items())     # best for looping
  ```

- “`.items()` gives us pairs — this will be super useful in the next lesson.”
- `.update()` example: merging two dictionaries.
- Membership test: `if "score" in player:`

---

### **Lesson 5: Looping Through Dictionaries**

**Video Length:** 13 minutes  
**Objectives:** Master iteration over keys, values, and pairs (using only elementary loops).

**Lesson Outline:**

1. Why looping matters with dictionaries (0:00–1:30)
2. Looping over keys (default behavior) (1:30–4:00)
3. Looping over values (4:00–6:00)
4. Looping over key-value pairs with `.items()` (6:00–10:00)
5. Common patterns and pitfalls (10:00–12:00)
6. Practice challenge (12:00–end)

**Talking Points:**
- Default: `for key in dictionary:` → only keys.
- `for value in dictionary.values():`
- Best way: `for key, value in dictionary.items():`
  ```python
  for name, score in scores.items():
      print(f"{name} has score {score}")
  ```
- Live coding: Print a nice formatted report from a dictionary of students.
- Warning: “Never modify a dictionary while looping over it directly (we’ll learn safer ways later).”

---

### **Lesson 6: Nesting – Dictionaries Inside Dictionaries and Lists**

**Video Length:** 14 minutes  
**Objectives:** Handle real-world complex data.

**Lesson Outline:**
1. Review of nesting in lists (0:00–1:30)
2. Dictionary inside a dictionary (1:30–6:00)
3. List inside a dictionary (6:00–9:00)
4. Dictionary inside a list (9:00–12:00)
5. Accessing nested data step-by-step (12:00–end)

**Talking Points:**
- Real example: Game character data.
  ```python
  player = {
      "name": "Link",
      "stats": {"health": 100, "attack": 25},
      "inventory": ["sword", "shield"]
  }
  ```
- Show how to access: `player["stats"]["health"]`
- Build a small class roster:
  ```python
  class_roster = [
      {"name": "Alice", "grades": [85, 92, 78]},
      {"name": "Bob", "grades": [90, 88, 95]}
  ]
  ```
- Emphasize reading from inside out.

---

### **Lesson 7: Practical Applications & Best Practices**

**Video Length:** 15 minutes  
**Objectives:** Tie everything together with mini-projects and tips.

**Lesson Outline:**
1. Recap of all concepts (0:00–2:00)
2. Mini Project 1 – Student Gradebook (2:00–7:00)
3. Mini Project 2 – Simple Inventory System (7:00–12:00)
4. Common mistakes & how to avoid them (12:00–14:00)
5. Final tips and next steps (14:00–end)

**Talking Points:**
- Gradebook example: Add students, update scores, calculate average using loops.
- Inventory example: Items with quantities, prices.
- Best practices:
  - Use meaningful key names.
  - Keep data types consistent when possible.
  - Use `.get()` to avoid crashes.
  - `in` operator is your friend.
- “Dictionaries are one of the most powerful tools in Python — almost every real program uses them heavily.”
- Encourage students to combine dictionaries with lists and loops in their own projects.

---

**Additional Teacher Resources (Markdown ready to copy):**

**Full Code Examples Repository Suggestion**  
Create a folder for each lesson with `.py` files.

**Suggested Homework Progression:**
- Lesson 1–2: Create 3 personal dictionaries
- Lesson 3–4: Modify and explore methods
- Lesson 5: Loop and print nicely formatted information
- Lesson 6: Build one nested structure
- Lesson 7: Complete both mini-projects

Would you like me to expand any specific lesson with full code samples, quiz questions, or slide suggestions?