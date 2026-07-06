# Lesson Examples - Nested if Statements

These examples show how to create and trace nested if statements, when they are useful, and how to keep them clear and readable.

## Example 1: Basic Nested if Statement

```python
age = 10
has_permission = True

if age >= 5 and age <= 11:          # outer if
    print("Student is in the correct VBS age range.")
    if has_permission:              # nested if
        print("Student has permission and can register for VBS.")
    else:
        print("Permission needed from parent.")
else:
    print("Student is outside the 5-11 age range.")
```

**Trace:** Both conditions True → both messages print.

## Example 2: Nested vs Compound Conditions

**Nested (useful when decisions depend on each other):**
```python
if age >= 5 and age <= 11:
    if has_allergy:
        print("Register with allergy precautions.")
```

**Compound (better when conditions are independent):**
```python
if age >= 5 and age <= 11 and has_allergy:
    print("Register with allergy precautions.")
```

**Tip:** Use nested when the inner decision only makes sense after the outer one is True. Avoid deep nesting (more than 2-3 levels) to keep code readable.

## Example 3: Debugging Nested Logic

```python
score = 85
attendance = "good"

if score >= 70:
    if attendance == "good":
        print("Student is doing well overall.")
    else:
        print("Attendance needs improvement.")
else:
    print("Focus needed on learning.")
```

**Common bug to watch for:** Missing indentation or wrong logical operators.

## Biblical Reflection

Just as nested if statements show layers of decision-making, God often works through layers of circumstances in our lives. Yet He guides us with perfect clarity and purpose. Our job is to trust Him at every level.

**Scripture:**  
“The heart of man plans his way, but the Lord establishes his steps.” (Proverbs 16:9)  
“And we know that for those who love God all things work together for good...” (Romans 8:28)

---

*If you find any typos or errors, please let me know.*  
📧 jcpartridge@logosteach.com

© 2026 LogosTeach - All Rights Reserved.
