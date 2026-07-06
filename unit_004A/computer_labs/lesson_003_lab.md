# Computer Lab: Comparison Operators in Python

## Learning Objectives

By the end of this lab, you will be able to:

- Use the comparison operators `<`, `>`, `<=`, `>=`, `==`, and `!=` to evaluate relationships between values.
- Understand that all comparisons return Boolean values (`True` or `False`).
- Apply comparisons in practical scenarios that require clear discernment.

## Lab Topics

- Comparison operators: `<`, `>`, `<=`, `>=`, `==`, `!=`
- Boolean results
- Basic decision-making with comparisons

## Materials / Prior Knowledge

**You should already know:** Variables, `print()` statements, basic data types.  
**You will need:** Python environment and this file saved as `comparison_operators_lab.py`.

---

### Step 0: Setup

```python
print("=== Comparison Operators Lab ===")
```

**Question 0:** What do you think `==` checks for compared to `=`?

### Step 1: Numerical Comparisons

**Context:**  
Comparisons help us evaluate situations with clarity and truth.

**Your Challenge:**  

1. Set `age = 17` and `min_age = 18`.  
2. Use `>=` and `<` to determine eligibility.

```python
age = 17
min_age = 18

can_enter = age >= min_age
is_younger = age < min_age

print(f"Age: {age}")
print(f"Can enter? {can_enter}")
print(f"Younger? {is_younger}")
```

**Expected Output / Test It:**  

```
Age: 17
Can enter? False
Younger? True
```

**Question 1:** Change `age` to 18. What happens and why?

### Step 2: Equality Checks

**Your Challenge:**  
Test equality and inequality with a quiz score example.

```python
correct = 42
guess = 42

print(f"Correct guess? {guess == correct}")
print(f"Wrong guess? {guess != correct}")
```

**Expected Output / Test It:**  

```
Correct guess? True
Wrong guess? False
```

**Question 2:** Change `guess` to 40. Explain the results.

### Step 3: Range Check

**Your Challenge:**  
Check if a value falls within a range.

```python
temp = 72
min_comfort = 65
max_comfort = 78

comfortable = (temp >= min_comfort) and (temp <= max_comfort)
print(f"Temperature {temp}°F comfortable? {comfortable}")
```

---

### Final Integration Code

```python
score = 85
passing = 70

print("Grade Check:")
print(f"Passing? {score >= passing}")
print(f"Perfect? {score == 100}")
```

---

### Lab Reflection (Answer in your notebook)

1. What is the difference between `=` and `==`?  
2. How did changing values affect the results?  
3. Give one real-life example where these operators would be useful.

---

You’re done!  

You just practiced the comparison operators that form the foundation of logical decision-making in Python.  

Save your file as `lesson_003_lab.py` and be ready to discuss.

© LogosTeach 2026 - All Rights Reserved.