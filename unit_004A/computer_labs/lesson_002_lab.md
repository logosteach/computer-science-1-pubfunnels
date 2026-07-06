# Computer Lab: Exploring Comparison Operators in Python

## Learning Objectives

By the end of this lab, you will be able to:

- Use comparison operators (`<`, `>`, `<=`, `>=`, `==`, `!=`) to evaluate relationships between values.
- Write conditional expressions that return `True` or `False` and understand their role in decision-making.
- Apply comparisons in simple real-world scenarios that reflect careful discernment.

## Lab Topics

- Comparison operators: `<`, `>`, `<=`, `>=`, `==`, `!=`
- Boolean results from comparisons
- Basic use in `if` statements (preview)

## Materials / Prior Knowledge

**You should already know:** Variables, basic data types (int, float, str), printing output.  
**You will need:** Python (IDLE, VS Code, or online interpreter) and a new file `comparison_operators_lab.py`.

---

### Step 0: Setup

```python
# Comparison Operators Lab
# Remember: Comparisons always return True or False (Boolean)
print("Ready to compare values!")
```

**Question 0:** What do you think the operators `==` and `!=` check for? (Write your guess before coding.)

### Step 1: Basic Numerical Comparisons

**Context:**  
Just as we discern truth from error (1 Kings 18:21), comparison operators help us evaluate relationships clearly.

**Your Challenge:**  

1. Assign `age = 17` and `min_age = 18`.  
2. Use `>=` and `<` to check if someone can enter a youth event.  
3. Print clear messages using the results.

```python
age = 17
min_age = 18

# TODO: Complete the comparisons
can_enter = age >= min_age
is_younger = age < min_age

print(f"Age: {age}")
print(f"Can enter (age >= {min_age})? {can_enter}")
print(f"Is younger than {min_age}? {is_younger}")
```

**Expected Output / Test It:**  
```
Age: 17
Can enter (age >= 18)? False
Is younger than 18? True
```

**Question 1:** What happens if you change `age` to 18? Why?

### Step 2: Equality and Inequality

**Context:**  
Equality checks are useful for validation, like confirming correct answers or matching values.

**Your Challenge:**  

1. Set `correct_answer = 42` and `user_guess = 42`.  
2. Use `==` and `!=` to check the guess.  
3. Add one more comparison with a different guess.

```python
correct_answer = 42
user_guess = 42

# TODO: Add == and != checks and print results
print(f"Guess correct? {user_guess == correct_answer}")
print(f"Guess incorrect? {user_guess != correct_answer}")
```

**Expected Output / Test It:**

```console
Guess correct? True
Guess incorrect? False
```

**Question 2:** Change `user_guess` to 40. What changes, and how might this be useful in a quiz program?

### Step 3: Combining Comparisons (Short Integration)

**Context:**  
We often need to check ranges, just as wisdom requires balanced judgment.

**Your Challenge:**  
Use `<=` and `>=` to check if a temperature is in a comfortable range.

```python
temp = 72
min_comfort = 65
max_comfort = 78

# TODO: Check if temp is within comfortable range
is_comfortable = (temp >= min_comfort) and (temp <= max_comfort)
print(f"Temperature {temp}°F comfortable? {is_comfortable}")
```

**Expected Output / Test It:**  

```console
Temperature 72°F comfortable? True
```

---

### Final Integration Code

Run this after completing the steps. It ties everything together:

```python
# Final Integration - Comparison Operators in Action
score = 85
passing = 70
perfect = 100

print("=== Grade Report ===")
print(f"Score: {score}")
print(f"Passing (>= {passing})? {score >= passing}")
print(f"Perfect (== {perfect})? {score == perfect}")
print(f"Needs improvement (!= {perfect})? {score != perfect}")
print(f"Above average (> {passing + 10})? {score > passing + 10}")
```

---

### Lab Reflection (Answer in your notebook)

1. What does `==` check compared to `=`?  
2. How did changing variable values affect the Boolean results?  
3. Give one real-life example (school, faith, or daily life) where comparison operators would be useful.

### Bonus Challenge (Optional – 2–3 minutes)

Add `<=` and `>=` checks for a student’s quiz score against letter grade thresholds (e.g., A >= 90).

---

**You’re done!**  
You just practiced the foundational comparison operators that power decision-making in Python programs. These tools help us write code with clarity and truth-seeking precision.  

Save your file as `comparison_operators_lab.py` and be ready to discuss your answers in class!

© LogosTeach 2026 - All Rights Reserved.