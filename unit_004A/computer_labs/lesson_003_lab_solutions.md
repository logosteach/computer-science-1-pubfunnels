# Computer Lab: Comparison Operators in Python - SOLUTIONS

## Learning Objectives

By the end of this lab, you will be able to:

- Use the comparison operators `<`, `>`, `<=`, `>=`, `==`, and `!=` correctly.
- Understand that comparisons return Boolean (`True` / `False`) values.
- Apply comparisons in practical scenarios with discernment.

## Solutions with Explanations

### Step 0: Setup

```python
print("=== Comparison Operators Lab - SOLUTIONS ===")
```

### Step 1: Numerical Comparisons

```python
age = 17
min_age = 18

can_enter = age >= min_age
is_younger = age < min_age

print(f"Age: {age}")
print(f"Can enter (age >= {min_age})? {can_enter}")
print(f"Is younger than {min_age}? {is_younger}")
```

**Explanation:** `>=` checks "at least" and `<` checks "less than". Change `age` to 18+ to see `can_enter` become `True`.

### Step 2: Equality and Inequality

```python
correct = 42
guess = 42

print(f"Guess: {guess}")
print(f"Correct (==)? {guess == correct}")
print(f"Wrong (!=)? {guess != correct}")
```

**Explanation:** `==` tests equality; `!=` tests inequality. Try `guess = 40` to observe the change.

### Step 3: Range Check

```python
temp = 72
min_comfort = 65
max_comfort = 78

comfortable = (temp >= min_comfort) and (temp <= max_comfort)
print(f"Temperature {temp}°F comfortable? {comfortable}")
```
**Explanation:** Combines comparisons with `and` to verify a value is within bounds.

### Final Integration

```python
score = 85
passing = 70

print("=== Grade Check ===")
print(f"Passing (>= {passing})? {score >= passing}")
print(f"Perfect (== 100)? {score == 100}")
print(f"Needs improvement (!= 100)? {score != 100}")
```

## Instructor Notes

- Encourage students to experiment by changing variable values.
- Discuss how these operators prepare for `if` statements and real decision-making.

---

**You’re done!**  

Save and review this solutions file after completing the lab.

© LogosTeach 2026 - All Rights Reserved.