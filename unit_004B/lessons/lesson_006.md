# Python with a Worldview  
**LogosTeach**

# Lesson 006 - Nested Loops  
## Examples and Illustrations

Below are clear examples and illustrations for each learning objective in this lesson.

## 1. Create and understand nested for and while loops

**Basic Nested For Loops:**

```python
for outer in range(3):  # Outer loop
    for inner in range(4):  # Inner loop
        print(f"({outer}, {inner})", end=" ")
    print()  # New line after inner loop
```

## 2. Use nested loops to solve problems (patterns, tables, grids)

**Example: Multiplication Table**

```python
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i*j:3}", end=" ")
    print()
```

**Example: Star Pattern (Right Triangle)**

```python
rows = 5
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end="")
    print()
```

## 3. Trace the execution of nested loops (outer vs inner)

**Tracing Example:**

```python
for outer in range(1, 4):
    print(f"Outer loop: {outer}")
    for inner in range(1, 3):
        print(f" Inner loop: {inner} (inside outer {outer})")
    print("--- Finished inner loop ---")
```

## 4. Avoid common pitfalls (excessive nesting & off-by-one errors)

**Common Mistake — Off-by-one:**

```python
for i in range(5):  # Wrong: goes 0 to 4
    for j in range(5):
        print(i, j)
```

**Better Practice:**

```python
for i in range(1, 6):  # Clearer: 1 to 5
    for j in range(1, 6):
        print(i, j)
```

**Tip:** Avoid nesting more than 3 levels deep when possible. Consider using functions to simplify deeply nested code.

## 5. Biblical Reflection

> Nested loops show us that God often works in layers — He has purposes within purposes.  
> What looks complex to us is beautifully intricate and orderly in His perfect plan.

**Scripture:**

> “For I know the plans I have for you,” declares the Lord, “plans to prosper you and not to harm you, plans to give you hope and a future.”  
> (Jeremiah 29:11)

> “Oh, the depth of the riches of the wisdom and knowledge of God! How unsearchable his judgments, and his paths beyond tracing out!”  
> (Romans 11:33-34)

---

*If you find any typos or errors, please let me know.*

[📧 Send me an email](mailto:info@logosteach.com?subject=Examples%20for%20Lesson%20006)

---

© 2026 LogosTeach - All Rights Reserved.
