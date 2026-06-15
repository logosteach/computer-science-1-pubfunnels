# Lesson 004 - Loop Control Statements: Break and Continue: Examples & Illustrations

Below are clear examples and illustrations for each learning objective in this lesson.

## 1. Use the break statement to exit a loop early

**`break` immediately exits the loop.**

```python
for i in range(10):
    print(i)
    if i == 5:
        print("Found 5! Stopping...")
        break
```

**Output:** 0 1 2 3 4 5 Found 5! Stopping...

## 2. Use the continue statement to skip the rest of the current iteration

**`continue` skips to the next iteration.**

```python
for i in range(8):
    if i % 2 == 0:  # Skip even numbers
        continue
    print(i)
```

**Output:** 1 3 5 7 (only odd numbers)

## 3. Apply break and continue to solve practical programming problems

**Practical Example: Search with early exit**

```python
numbers = [12, 45, 67, 89, 34, 67, 23]
for num in numbers:
    if num == 67:
        print("Found target:", num)
        break
    print("Checking...", num)
else:
    print("Target not found")
```

**Another Example: Skip invalid input**

```python
while True:
    user_input = input("Enter a positive number: ")
    if user_input == "quit":
        break
    if not user_input.isdigit() or int(user_input) <= 0:
        print("Invalid input. Try again.")
        continue
    print("Valid number entered:", user_input)
    break
```

## 4. Understand how these statements affect loop execution

| Statement   | Effect |
|-------------|--------|
| **break**   | Completely exits the loop (like an emergency stop) |
| **continue**| Skips the rest of the current iteration and moves to the next one |

**Important:** Both `break` and `continue` only affect the innermost loop when using nested loops.

## 5. Biblical Reflection

> In programming, **break** is like repentance — we stop going in the wrong direction.  
> **Continue** is like pressing forward — we keep going toward the goal despite setbacks.

**Scripture:**

> “Brothers and sisters, I do not consider myself yet to have taken hold of it. But one thing I do: Forgetting what is behind and straining toward what is ahead, I press on toward the goal to win the prize for which God has called me heavenward in Christ Jesus.”  
> (Philippians 3:13-14)

---

*If you find any typos or errors, please let me know.*

[📧 Send me an email](mailto:info@logosteach.com?subject=Examples%20for%20Lesson%20004)

© 2026 LogosTeach - All Rights Reserved.