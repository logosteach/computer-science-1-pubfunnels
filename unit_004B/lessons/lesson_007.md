# Lesson 007 - Putting It All Together: Loops Best Practices

Below are clear examples, common pitfalls, and best practices for each learning objective.

## 1. Choose the most appropriate loop (for or while)

| Use **for** loop when...                          | Use **while** loop when...                     |
|---------------------------------------------------|------------------------------------------------|
| You know the number of iterations in advance     | You don’t know how many times it will run     |
| Iterating over a list, string, or range          | Repeating based on a condition                |

**Example - for loop (better choice):**

```python
for student in students:
    print("Processing", student)
```

**Example - while loop (better choice):**

```python
while not game_over:
    process_turn()
```

## 2. Identify and fix common loop errors

**Common Error 1: Infinite Loop**

```python
count = 0
while count < 10:
    print(count)  # Forgot to increment!
```

**Fixed Version:**

```python
count = 0
while count < 10:
    print(count)
    count += 1
```

**Common Error 2: Off-by-One**

```python
for i in range(5):  # Prints 0 to 4 (only 5 numbers)
    print(i)
```

**Fixed Version (if you want 1 to 5):**

```python
for i in range(1, 6):  # Correct: 1 to 5
    print(i)
```

## 3. Debug loops using print statements

**Debugging Example:**

```python
numbers = [3, 7, 2, 9, 1]
target = 9
for i in range(len(numbers)):
    print(f"Checking index {i}: {numbers[i]}")  # Debug print
    if numbers[i] == target:
        print("Target found at index", i)
        break
```

## 4. Write clean, readable, and efficient loop code (Best Practices)

**Good Practice Examples:**

```python
# Clean & Readable
for student in students:
    process_student_record(student)

# Use meaningful variable names
total_sales = 0
for sale in daily_sales:
    total_sales += sale
```

**Avoid Deep Nesting:**

```python
# Instead of deep nesting, consider using functions or list comprehensions
squares = [x**2 for x in range(10)]
```

**Best Practices Summary:**

- Use `for` when possible — it's usually cleaner
- Keep loops as simple as possible
- Use meaningful variable names
- Limit nesting depth (ideally no more than 2–3 levels)
- Include comments for complex logic

## 5. Biblical Reflection

> Mastering loops teaches us diligence, patience, and the importance of doing things in an orderly way.  
> Just as we write clear and efficient code, God calls us to live with purpose and excellence.

**Scripture:**

> “Let all things be done decently and in order.” (1 Corinthians 14:40)

> “Whatever you do, work at it with all your heart, as working for the Lord…” (Colossians 3:23)

---

*If you find any typos or errors, please let me know.*

[📧 Send me an email](mailto:info@logosteach.com?subject=Examples%20for%20Lesson%20007)

---

© 2026 LogosTeach - All Rights Reserved.