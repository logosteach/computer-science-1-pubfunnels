# Unit 4A: Logic Flow and Conditional Statements Assessment

**Student Name:** _______________________________     **Date:** _______________________________

**Unit:** 4A – Logic Flow and Conditional Statements     **Total Points Possible:** ______

---

## Instructions

Review all learning objectives from the lessons in this unit before beginning. You may use your IDE to write and test your code. Please minimize the use of AI tools during this assessment — the goal is to develop independent thinking, creativity, and problem-solving skills. Write all code as clearly and cleanly as possible, and test your solutions thoroughly before submitting. This assessment is designed for both students working asynchronously alone and those in a group with an instructor.

---

## Section 1: Knowledge & Understanding

### 1. Which of the following correctly describes Boolean values in Python? (__ points)

a) Boolean values are the two special values `True` and `False` that form the foundation of all decision-making in programs

b) Boolean values can only be the integers 0 and 1

c) Boolean values are the same as string values "True" and "False"

d) Boolean values must always be written in lowercase as `true` and `false`

### 2. Which of the following is the correct way to check if a variable `age` is greater than or equal to 18 using a comparator operator? (__ points)

a) `if age = 18:`

b) `if age => 18:`

c) `if age >= 18:`

d) `if age > 18 or age == 18:`

### 3. What is the result of the following compound condition when `age = 25` and `has_ticket = True`? (__ points)

```python
if age >= 18 and has_ticket:
    print("Entry allowed")
```

a) The print statement will not execute because `and` requires both conditions to be False

b) The print statement will execute because both conditions are True

c) The print statement will execute only if one condition is True (short-circuit behavior)

d) This will cause a syntax error because compound conditions are not allowed with `and`

### 4. What will Python do when evaluating this compound condition: `if x > 0 or y / 0 == 5:` (assuming `x = 10` and `y = 0`)? (__ points)

a) It will raise a ZeroDivisionError because it evaluates both sides of `or`

b) It will evaluate the division anyway because `or` always checks both sides

c) It will raise an error because division by zero is not allowed in conditions

d) It will not raise an error because short-circuit evaluation stops after the first True condition (`x > 0`)

### 5. Which of the following is **NOT** a valid use of an `if`/`elif`/`else` structure? (__ points)

a) Using `elif` to handle multiple mutually exclusive conditions like grade ranges (A, B, C, etc.)

b) Using multiple independent `if` statements to check several unrelated conditions that can all be True at the same time

c) Placing an `else` block before any `elif` blocks

d) Using `if` to check a simple condition and `else` to handle the opposite case

::: page-break :::

### 6. What is the output of the following code? (__ points)

```python
score = 85
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("F")
```

a) A

b) B

c) C

d) F

### 7. What is the output of the following code? (__ points)

```python
score = 85
if score >= 90:
    print("A")
if score >= 80:
    print("B")
if score >= 70:
    print("C")
else:
    print("F")
```

a) Only "B" is printed

b) "A", "B", and "C" are all printed

c) "B" and "C" are printed

d) Only "F" is printed

::: page-break :::

### 8. Which of the following best demonstrates **nested** `if` statements? (__ points)

a)
```python
if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teen")
```

b)
```python
if has_ticket:
    if age >= 18:
        print("Full access")
    else:
        print("Limited access")
```

c)
```python
if age >= 18 and has_ticket:
    print("Entry allowed")
```

d)
```python
if score > 90 or score == 100:
    print("Excellent")
```

### 9. Which of the following is a common pitfall when writing conditional statements? (__ points)

a) Using consistent 4-space indentation for all code blocks

b) Forgetting the colon (`:`) after the condition in an `if` statement

c) Using descriptive variable names like `is_eligible`

d) Testing code with multiple input values to check all branches

### 10. What is the final value of `age` after this code runs? (__ points)

```python
age = 25
if age >= 18:
    age = 15   # First if triggers
if age > 20:
    age = 34   # Second if does NOT trigger (15 is not > 20)
if age < 20:
    age = 34   # Third if triggers on the current value of 15
print(age)
```

a) 25

b) 15

c) 34

d) The code will cause an error

### 11. Which statement about the ternary operator is **true**? (__ points)

a) The ternary operator can only be used for simple assignments and cannot replace multi-line `if`/`else` blocks

b) The ternary operator always improves code readability and should be used for every `if`/`else`

c) The syntax is `condition ? true_value : false_value` (like in other languages)

d) The ternary operator works only with numeric values

### 12. What is the value of `result` after this ternary expression? (__ points)

```python
age = 16
result = "Adult" if age >= 18 else "Minor"
```

a) "Adult"

b) "Minor"

c) True

d) This code will cause a SyntaxError

### 13. Look at the following code. Which of the following statements is true? (__ points)

```python
score = 85
if score >= 90:
    print("A")
elif score >= 80
    print("B")
elif score >= 70:
    print("C")
else:
    print("F")
```

a) The code runs without errors and prints "B"

b) The code has a missing colon (`:`) after the condition in the first `elif` statement

c) The code has an indentation error

d) There are no errors in the code

### 14. What does the `not` operator do in a condition like `if not is_logged_in:` ? (__ points)

a) It inverts the Boolean value (True becomes False, False becomes True)

b) It checks if the variable is not equal to zero

c) It combines two conditions with logical OR

d) It has no effect on the condition

### 15. Which best practice should you follow when writing conditional statements? (__ points)

a) Always use `== True` to check Boolean variables

b) Use clear, descriptive variable names and keep conditions simple and readable

c) Nest as many `if` statements as possible to handle every possible case

d) Write very long single-line conditions with many `and`/`or` operators

### 16. What is the purpose of short-circuit evaluation in Python? (__ points)

a) To make the code run slower for better debugging

b) To avoid unnecessary computations or errors when the result is already known

c) To force evaluation of all parts of a compound condition

d) To convert `and` into `or`

### 17. Consider this code: (__ points)

```python
name = ""
if name:
    print("Name provided")
else:
    print("No name")
```

What is printed?

a) Nothing (empty output)

b) "Name provided"

c) An error because empty string cannot be used in `if`

d) "No name"

::: page-break :::

### 18. Which of the following is the best way to rewrite this nested structure using `elif` for better readability? (__ points)

```python
if age < 13:
    print("Child")
else:
    if age < 18:
        print("Teen")
    else:
        print("Adult")
```

a) Keep it as nested because it is clearer

b)
```python
if age < 13:
    print("Child")
elif age < 18:
    print("Teen")
else:
    print("Adult")
```

c) Use a ternary operator for all three cases

d) Use only independent `if` statements

### 19. What does this code print when `is_member = True`? (__ points)

```python
is_member = True
status = "Premium Member" if is_member else "Regular Member"
print(status)
```

a) Nothing

b) True

c) "Regular Member"

d) "Premium Member"

### 20. Which biblical principle is most closely connected to writing clear, ordered conditional logic in programming? (__ points)

a) God gave us free choice without any consequences

b) Doing all things decently and in order reflects good stewardship of our minds and abilities

c) We should always make decisions based only on feelings

d) Complex code is always better because it shows creativity

---

## Section 2: Short Answer & Explanation

### 1. (__ points)

Explain the difference between `True` and `False` and why Boolean values are the foundation of all decision-making in Python programs. Give one real-world example of how they are used.

*(Write your answer below)*

### 2. (__ points)

Write a short code example using at least three different comparator operators (`==`, `>`, `<=`, etc.). Then explain what the code does and the expected Boolean result for specific values.

*(Write your answer below)*

### 3. (__ points)

Describe what a compound conditional expression is. Write an example using `and` and `or` and explain the role of parentheses in controlling the order of evaluation.

*(Write your answer below)*

### 4. (__ points)

What is short-circuit evaluation? Give an example of a compound condition where short-circuiting prevents a potential error (such as division by zero), and explain why this feature is useful.

*(Write your answer below)*

### 5. (__ points)

Explain the difference between using chained `elif` statements versus multiple independent `if` statements. Provide a brief scenario where one is preferable over the other.

*(Write your answer below)*

### 6. (__ points)

What is a nested `if` statement? Write a simple example and explain when nested conditionals are useful versus when you should use compound conditions instead.

*(Write your answer below)*

### 7. (__ points)

What are truthy and falsy values in Python? List at least four examples of falsy values and explain why `if name:` is often preferred over `if name != ""` for checking if a string has content.

*(Write your answer below)*

### 8. (__ points)

Identify two common pitfalls when writing conditional statements and explain how to avoid them. Give a "before" (buggy) and "after" (fixed) code example for one of them.

*(Write your answer below)*

### 9. (__ points)

Explain the syntax and purpose of the ternary operator. Convert this `if`/`else` to a ternary: `if score >= 60: result = "Pass" else: result = "Fail"`. When should you avoid using a ternary?

*(Write your answer below)*

### 10. (__ points)

Describe a real-world scenario (such as a ticket system, eligibility checker, or game decision) where you would combine several concepts from this unit (`if`/`elif`, compound conditions, ternary, etc.). Briefly outline the logic you would use.

*(Write your answer below)*

::: page-break :::

## Section 3: Coding Problems

### Coding Problem 1 (__ points)

Write a program named `eligibility_checker.py`.

The program should ask the user for their age (integer) and whether they have a membership card (`yes` or `no`).

- Use an `if`/`elif`/`else` chain to determine and print a clear message about eligibility for a special event (e.g., "Full access", "Limited access", "Not eligible").
- Use a ternary operator somewhere in the program to decide a bonus message (e.g., "Welcome back!" vs "First time?").
- Use at least one compound condition (`and`/`or`).
- Include comments explaining your logic and best practices you followed.
- Test with several inputs (including edge cases like age 0, 17, 18).

```python
# Your code here for eligibility_checker.py
```

### Coding Problem 2 (__ points)

Write a program named `grade_advisor.py`.

The program should ask the user for a numeric score (0–100).

- Use `if`/`elif`/`else` to print the letter grade (A/B/C/D/F).
- Use truthy/falsy concepts or a ternary to handle invalid scores (e.g., negative or >100) and print an appropriate message.
- Include a short reflection comment at the end explaining one best practice you used and one potential pitfall you avoided.
- Make the code clean, readable, and handle basic input gracefully.

```python
# Your code here for grade_advisor.py
```

::: page-break :::

## Biblical Integration & Reflection

**Reflect:** (__ points)

In this unit you have learned how to use conditional logic (`if`/`elif`/`else`, ternary operators, compound conditions, etc.) to make clear, ordered decisions in Python programs.

**Reflect and explain** (in 4–6 sentences): How does writing careful, readable conditional logic in code remind you of the biblical call to make wise choices in life? Connect at least two specific programming concepts from this unit (e.g., order of conditions, avoiding pitfalls, truthy/falsy, or short-circuit evaluation) to Scripture and the importance of discernment, stewardship, or walking in God’s ways. Use at least one verse from the New King James Version (NKJV) in your reflection.

*(Write your reflection below)*

---

> Labs, Practice Files and Assessments are developed in collaboration with the Grok AI assistant under instructor supervision and review.

**Deliverable:** Submit this completed assessment (and the two Python files: `eligibility_checker.py` and `grade_advisor.py`). Self-grade your work where possible and compare with provided solutions. Whether you are working asynchronously alone or in a group with an instructor, be ready to discuss your reasoning and design choices.

© 2026 LogosTeach - All Rights Reserved.
