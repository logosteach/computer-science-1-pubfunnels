# Python with a Worldview  

**LogosTeach**

---

# Lesson 001 - Introduction to Loops: Examples & Illustrations

Below are helpful examples and illustrations for each learning objective in this lesson.

## 1. Explain why repetition is necessary in programming

**Why repetition matters:** Many tasks in life and programming require doing the same action multiple times. Writing the same code over and over is inefficient and error-prone.

**Real-world examples:**

- Printing 100 student report cards
- Sending reminder emails to 500 customers
- Calculating the total of all items in a shopping cart
- Checking every item in an inventory list

**Programming benefit:** Loops allow us to write the code once and repeat it as many times as needed.

## 2. Describe the two main types of loops in Python: while and for

**for loop:** Best when you know how many times you want to repeat (definite iteration).

```python
for i in range(5):
    print("Hello!", i)
```

**while loop:** Best when you want to repeat until a condition becomes false (indefinite iteration).

```python
count = 0
while count < 5:
    print("Hello!", count)
    count += 1
```

## 3. Understand the basic concept of iteration

**Iteration** means repeating a process. Each repetition is called an **iteration**.

**Example:** Imagine a washing machine cycle. Each full rotation of the drum is one iteration.

```python
# Simple iteration example
for number in [1, 2, 3, 4, 5]:
    print("Processing item", number)
```

This loop performs 5 iterations — one for each number in the list.

## 4. Recognize the danger of infinite loops and how to prevent them

**Infinite Loop Danger:** A loop that never stops running.

```python
# DANGEROUS - Infinite Loop!
while True:
    print("This will never stop!")
```

**How to prevent infinite loops:**

- Always include a condition that will eventually become False
- Use a counter that increases/decreases toward the stopping condition
- Include a `break` statement when a goal is reached

```python
count = 0
while count < 10:  # Safe condition
    print(count)
    count += 1  # Progress toward stopping condition
```

## 5. Biblical Reflection

> Just as God established rhythms and cycles in creation — day and night, seasons, and the rhythm of life —  
> loops help us bring order and repetition into our programs.  
> We can trust that God’s character is faithful and consistent, just as we can rely on well-written loops to behave predictably.

> **Scripture:** “While the earth remains, seedtime and harvest, cold and heat, summer and winter, day and night, shall not cease.” (Genesis 8:22)

---

*If you find any typos or errors, please let me know.*  

[📧 Send me an email](mailto:info@logosteach.com?subject=Examples%20for%20Lesson%20001)

---

© 2026 LogosTeach - All Rights Reserved.
