# Lesson 005 - The Pass Statement and Loop Else Clause: Examples & Illustrations

Below are clear examples and illustrations for each learning objective in this lesson.

## 1. Use the pass statement as a placeholder

**Using `pass` in a loop (placeholder):**

```python
for i in range(5):
    if i == 2:
        pass  # TODO: Add logic later
    else:
        print(i)
```

**Using `pass` in conditional blocks:**

```python
number = 10
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    pass  # Do nothing for zero (placeholder)
```

## 2 & 3. The optional else clause with for and while loops

**For Loop with `else`:**

```python
for i in range(5):
    print(i)
else:
    print("Loop completed normally!")
```

**For Loop with `break` (else does NOT run):**

```python
for i in range(10):
    print(i)
    if i == 3:
        print("Breaking early...")
        break
else:
    print("Loop completed normally!")
```

**While Loop with `else`:**

```python
count = 0
while count < 5:
    print(count)
    count += 1
else:
    print("While loop finished successfully!")
```

## 4. Practical use of pass and else clause

**Realistic Example — Searching with else clause:**

```python
numbers = [12, 45, 67, 23, 89]
target = 67
for num in numbers:
    if num == target:
        print("Target found!")
        break
else:
    print("Target not found in the list.")
```

**Cleaner Code Tip:** Use `pass` when you're sketching structure and `else` to handle "no break occurred" scenarios cleanly.

## 5. Biblical Reflection

> The **else** clause in a loop runs only when the loop completes normally — without encountering a `break`.  
> In the same way, God’s promises are “Yes” and “Amen” when we remain faithful and do not quit prematurely.

**Scripture:**

> “For all the promises of God find their Yes in him. That is why it is through him that we utter our Amen to God for his glory.”  
> (2 Corinthians 1:20)

---

*If you find any typos or errors, please let me know.*

[📧 Send me an email](mailto:info@logosteach.com?subject=Examples%20for%20Lesson%20005)

---

© 2026 LogosTeach - All Rights Reserved.
