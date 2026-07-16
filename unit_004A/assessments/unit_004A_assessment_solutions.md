# Unit 4A Assessment – Solutions

**Unit:** 4A – Logic Flow and Conditional Statements  

**Note:** These solutions are for instructor use and student self-checking. Partial credit and thoughtful explanations should be considered. No formal grade scale is provided — use professional judgment.

---

## Section 1: Knowledge & Understanding – Solutions

### 1. Which of the following correctly describes Boolean values in Python?

**Correct Answer:** a  

**Explanation:** Boolean values are the two special values `True` and `False`. They form the foundation of all decision-making. Options b–d are common beginner misconceptions.

### 2. Which of the following is the correct way to check if a variable `age` is greater than or equal to 18?

**Correct Answer:** c  

**Explanation:** `>=` is the correct comparator. a uses assignment; b uses invalid syntax; d is logically equivalent but not the single clean comparator.

### 3. Compound condition with `age = 25` and `has_ticket = True`

**Correct Answer:** b  

**Explanation:** Both conditions are True, so the `and` expression is True and the print statement executes.

### 4. Short-circuit with `x = 10` and `y = 0`

**Correct Answer:** d  

**Explanation:** Because the left side of `or` is True, Python short-circuits and never evaluates the right side, avoiding the ZeroDivisionError.

### 5. Which is NOT a valid use of if/elif/else?

**Correct Answer:** c  

**Explanation:** `else` must come last, after all `elif` blocks (if any). Placing it earlier is a syntax error.

### 6. Output of the if/elif/else grade code with score = 85

**Correct Answer:** b  

**Explanation:** The first matching condition is `score >= 80`, so "B" is printed and the remaining branches are skipped.

### 7. Output of independent if statements with score = 85

**Correct Answer:** c  

**Explanation:** Independent `if` statements are all checked. Both `>= 80` and `>= 70` are True, so "B" and "C" print. The `else` belongs only to the last `if`.

### 8. Which best demonstrates nested if statements?

**Correct Answer:** b  

**Explanation:** Option b shows an `if` inside another `if` block (true nesting). The others are chained elif, compound, or single if.

### 9. Common pitfall

**Correct Answer:** b  

**Explanation:** Forgetting the colon after a condition is a very common SyntaxError. The other options are best practices.

### 10. Final value of age after sequential ifs

**Correct Answer:** c  

**Explanation:** First if sets age = 15. Second if (age > 20) is False and skipped. Third if (age < 20) is True and sets age = 34.

### 11. Which statement about the ternary operator is true?

**Correct Answer:** a  

**Explanation:** Ternary is ideal for simple assignments. Multi-line logic or complex conditions should stay as full if/else for readability.

### 12. Value of result from ternary with age = 16

**Correct Answer:** b  

**Explanation:** age >= 18 is False, so the else value "Minor" is assigned.

### 13. Code with missing colon

**Correct Answer:** b  

**Explanation:** Exactly one error: missing colon after `elif score >= 80`.

### 14. What does the not operator do?

**Correct Answer:** a  

**Explanation:** `not` inverts the Boolean value of the expression that follows it.

### 15. Best practice for conditionals

**Correct Answer:** b  

**Explanation:** Clear names and simple, readable conditions are essential best practices (Lesson 6).

### 16. Purpose of short-circuit evaluation

**Correct Answer:** b  

**Explanation:** It avoids unnecessary work and potential errors when the final result is already known.

### 17. Empty string in if condition

**Correct Answer:** d  

**Explanation:** Empty string is falsy, so the else branch runs and prints "No name".

### 18. Best rewrite of nested structure

**Correct Answer:** b  

**Explanation:** A flat elif chain is clearer and more readable for exclusive age ranges than unnecessary nesting.

### 19. Ternary with is_member = True

**Correct Answer:** d  

**Explanation:** The condition is True, so "Premium Member" is selected.

### 20. Biblical principle connected to clear conditional logic

**Correct Answer:** b  

**Explanation:** 1 Corinthians 14:40 (NKJV) – “Let all things be done decently and in order.” Clear, ordered code reflects good stewardship.

---

## Section 2: Short Answer & Explanation – Sample Solutions

### 1. Boolean True/False foundation

**Sample Answer:**  
Boolean values are the two special constants True and False. Every decision a program makes ultimately reduces to True or False. They form the foundation of all conditional logic (if statements, loops, etc.). Real-world example: checking whether a user is logged in or whether a temperature is above a threshold to turn on a fan.

### 2. Comparator operators example

**Sample Answer:**

```python
age = 25
score = 88
name = "Alex"
print(age >= 18)      # True
print(score == 100)   # False
print(name != "")     # True
```

The code evaluates three different comparisons and prints the Boolean results.

### 3. Compound conditional expression

**Sample Answer:**  
A compound conditional combines multiple conditions using and, or, or not. Example: `if age >= 18 and has_ticket or is_vip:`. Parentheses control evaluation order because not has higher precedence than and, which has higher precedence than or. Use parentheses for clarity.

### 4. Short-circuit evaluation

**Sample Answer:**  
Short-circuit evaluation means Python stops evaluating a compound condition as soon as the final result is known. Example: `if x != 0 and y / x > 5:` – if x is 0 the division is never attempted. This prevents errors and improves efficiency.

### 5. elif vs independent ifs

**Sample Answer:**  
Chained elif checks conditions in order and stops at the first True. Independent ifs check every condition. Prefer elif when categories are mutually exclusive (e.g., letter grades). Prefer independent ifs when multiple actions can legitimately happen together (e.g., multiple warnings).

### 6. Nested if

**Sample Answer:**

```python
if has_ticket:
    if age >= 18:
        print("Full access")
    else:
        print("Limited access")
else:
    print("No entry")
```

Nested ifs are useful when a decision depends on a previous decision. Prefer compound conditions when the logic can be expressed more flatly and clearly.

### 7. Truthy and falsy

**Sample Answer:**  
Falsy values include: False, None, 0, 0.0, "", [], {}, set(). Truthy values are everything else. `if name:` is preferred because it is more Pythonic and works for any falsy empty value, not just empty strings.

### 8. Common pitfalls

**Sample Answer:**  
Two common pitfalls: (1) using = instead of ==, (2) missing colon after condition.  
Before (buggy): `if age = 18 print("Adult")`  
After (fixed): `if age == 18: print("Adult")`  
Always double-check assignment vs comparison and colon placement.

### 9. Ternary operator

**Sample Answer:**  
Syntax: `value_if_true if condition else value_if_false`.  
Converted: `result = "Pass" if score >= 60 else "Fail"`  
Avoid ternary when the logic is complex, multi-line, or hard to read.

### 10. Real-world scenario

**Sample Answer:**  
Theme-park ticket advisor. Ask age, height, and season pass status. Use if/elif/else for age-based pricing, a compound condition for full-access rides (height >= 48 and has pass), and a ternary for a welcome message. This combines almost every concept from the unit.

---

## Section 3: Coding Problems – Sample Solutions

### Coding Problem 1: eligibility_checker.py

```python
print("=== Special Event Eligibility Checker ===")

age = int(input("Enter your age: "))
has_card = input("Do you have a membership card? (yes/no): ").strip().lower()

# Compound condition + if/elif/else chain
if age >= 18 and has_card == "yes":
    access = "Full access"
elif age >= 13:
    access = "Limited access (with adult supervision)"
else:
    access = "Not eligible"

print(f"Eligibility: {access}")

# Ternary for bonus message
bonus = "Welcome back, valued member!" if has_card == "yes" else "First-time visitor – enjoy the day!"
print(bonus)

# Best practices: clear variable names, strip().lower(), comments, tested edge cases
```

**Notes for grading:** Students should have clean input handling, at least one compound condition, an if/elif/else chain, a ternary, and comments. No functions.

### Coding Problem 2: grade_advisor.py

```python
print("=== Grade Advisor ===")

score_input = input("Enter your numeric score (0-100): ").strip()

# Handle empty or invalid input with truthy/falsy and conversion
if not score_input:
    print("No score entered.")
else:
    score = float(score_input)
    if score < 0 or score > 100:
        print("Invalid score. Please enter a value between 0 and 100.")
    elif score >= 90:
        print("Letter grade: A")
    elif score >= 80:
        print("Letter grade: B")
    elif score >= 70:
        print("Letter grade: C")
    elif score >= 60:
        print("Letter grade: D")
    else:
        print("Letter grade: F")

# Reflection comment
# Best practice used: clear if/elif/else chain ordered from highest to lowest.
# Pitfall avoided: using = instead of == and forgetting the colon after conditions.
```

**Notes for grading:** Look for proper grade ranges, handling of invalid scores (using truthy/falsy or ternary is fine), clean code, and a thoughtful reflection comment.

---

## Biblical Integration & Reflection – Sample Response

**Sample Reflection:**

Writing clear conditional logic teaches me the importance of ordered, intentional decision-making. Just as the order of if/elif conditions matters and a missing colon can break an entire program, the choices I make in life need careful thought and the right sequence. Short-circuit evaluation reminds me that I should not keep evaluating every option when God’s Word has already given a clear answer. The principle “Let all things be done decently and in order” (1 Corinthians 14:40 NKJV) applies both to code and to living wisely. Clear code is good stewardship of the mind God gave me, and clear choices honor Him.

---

> Labs, Practice Files and Assessments are developed in collaboration with the Grok AI assistant under instructor supervision and review.

**Deliverable Note:** Students submit the completed assessment plus the two .py files. Whether working asynchronously alone or in a group setting with an instructor, they should be prepared to discuss their reasoning.

© 2026 LogosTeach - All Rights Reserved.
