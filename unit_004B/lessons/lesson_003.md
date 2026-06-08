# Lesson 003 - The For Loop and the range() Function: Examples & Illustrations

Below are clear examples and illustrations for each learning objective in this lesson.

## 1. Understand the range() function — what it produces and how to use it in a for loop

**What does `range()` produce?**  
It generates a sequence of numbers (it returns a **range object**, not a list).

```python
print(range(5))          # range(0, 5)
print(list(range(5)))    # [0, 1, 2, 3, 4]
```

**Using it in a for loop:**

```python
for i in range(5):
    print("Iteration", i)
```

**Output:**  
Iteration 0  
Iteration 1  
Iteration 2  
Iteration 3  
Iteration 4

## 2. Use the range() function with start, stop, and step parameters

**Full syntax:** `range(start, stop, step)`

```python
# Count from 2 to 10 (stop is exclusive)
for i in range(2, 11):
    print(i)

# Count by 2s (step)
for i in range(0, 21, 2):
    print(i)  # 0, 2, 4, ..., 20

# Count backwards
for i in range(10, 0, -1):
    print(i)  # 10 down to 1
```

## 3. Iterate over sequences such as strings and simple lists

**Looping over a list:**

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("I like", fruit)
```

**Looping over a string (character by character):**

```python
for letter in "Python":
    print(letter)
```

**Output:** P y t h o n (one letter per line)

## 4. Explain when to use a for loop versus a while loop

| Use a **for** loop when…                          | Use a **while** loop when…                     |
|---------------------------------------------------|------------------------------------------------|
| You know how many times you want to repeat (fixed number) | You don’t know in advance how many times it will run |
| Iterating over a list, string, range, etc.        | Repeating until a condition becomes False      |
| Example: printing numbers 1–10                    | Example: keep asking for password until correct |

## 5. Biblical Reflection

> Just as a **for loop** moves through a known sequence one step at a time, God leads us step by step through life.  
> We don’t always see the full journey ahead, but we can trust His Word to light the next step.

> **Scripture:**  
> “Your word is a lamp to my feet and a light to my path.” (Psalm 119:105)  
>   
> “Trust in the Lord with all your heart, and do not lean on your own understanding. In all your ways acknowledge him, and he will make straight your paths.” (Proverbs 3:5-6)

---

*If you find any typos or errors, please let me know.*  

[📧 Send me an email](mailto:info@logosteach.com?subject=Examples%20for%20Lesson%20003)

---

© 2026 LogosTeach - All Rights Reserved.
