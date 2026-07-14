# Computer Lab: Remote Security Facility Access Control

## Learning Objectives

By the end of this lab, you will be able to:
- Create and trace nested `if` statements (an `if` inside another `if`).
- Design multi-level decision logic based on multiple conditions.
- Decide when nested conditionals are useful versus when compound conditions (`and`/`or`) are better.
- Avoid overly complex nesting that makes code hard to read.
- Debug nested conditional logic by testing different input combinations.
- Reflect on how nested decisions remind us that God often works through layers of circumstances while still guiding us with clarity and purpose (Proverbs 16:9; Romans 8:28 NKJV).

## Lab Topics

- Nested `if`/`else` structures
- User input for multiple conditions
- Multi-level access control logic
- Testing all possible branches
- Independent problem-solving

## Materials / Prior Knowledge

**You should already know:** Variables, `input()`, `print()`, basic `if`/`elif`/`else`, comparison operators, and how to use nested conditionals.  
**You will need:** A Python editor and approximately 20–30 minutes of focused work.

---

### Lab Scenario

You have been hired to work in a remote security facility. Access is controlled by special key cards:

- **Key Card A** – Gets you through the main gate only (entrance privileges to the facility, but no access to any levels).
- **Key Card B** – Gives you access to Levels 1 and 2.
- **Key Card C** – Gives you access to Levels 1 through 4.
- **Key Card D** – (Very rare) Gives you access to all levels.

A person can carry **at most two** key cards at the same time.

**Your job:** Write a complete program that:
1. Asks the user which key cards they currently have (they may have 0, 1, or 2 cards).
2. Uses **nested** `if`/`else` logic to determine and clearly report the exact type of access the person has.
3. Handles every realistic combination of cards correctly.

---

### Your Independent Challenge (20–30 minutes)

Write the entire program from scratch. There is very little starter code on purpose — this lab is designed to test your independent coding skills.

**Requirements:**

1. Prompt the user for the first key card they have (A, B, C, D, or “none”).
2. Prompt the user for a second key card they have (A, B, C, D, or “none”). Remember they can have at most two cards.
3. Use nested `if`/`else` statements to evaluate the combination of cards and decide the highest level of access granted.
4. Print a clear, user-friendly message describing exactly what access the person has.
5. Your nested logic must be able to reach every meaningful branch by changing the inputs.
6. Include helpful `print()` tracing statements (or comments) so you (and your instructor) can follow the decision path.
7. Make your code readable — avoid unnecessary deep nesting if a cleaner structure works.

**Suggested Access Rules (you may refine these as long as they make sense):**

- Only A → Gate access only
- B (with or without A) → Levels 1–2
- C (with or without A or B) → Levels 1–4
- D (with any other card or alone) → Full access to all levels
- No cards → Access denied
- Invalid combinations should be handled gracefully

**Starter skeleton (optional – delete or modify as needed):**

```python
print("=== Remote Security Facility Access Control ===\n")

# Get card inputs from the user
card1 = input("Enter first key card (A/B/C/D/none): ").strip().upper()
card2 = input("Enter second key card (A/B/C/D/none): ").strip().upper()

print("\n--- Evaluating access privileges ---")

# Write your nested if/else logic below this line
# Hint: Start with the highest privilege cards first (D), then C, then B, etc.

# Your nested decision structure goes here...

print("\n--- End of access check ---")
```

**Expected Behavior Examples (test these carefully):**

```
Input: A and none
→ Gate access only

Input: B and A
→ Access to Levels 1 and 2

Input: C and none
→ Access to Levels 1 through 4

Input: D and B
→ Full access to all levels

Input: none and none
→ Access denied
```

---

### Testing Checklist

Before you finish, make sure you can reach **all major branches** by changing the two card inputs. Test at least these combinations:

- [ ] No cards
- [ ] Only A
- [ ] Only B
- [ ] Only C
- [ ] Only D
- [ ] A + B
- [ ] A + C
- [ ] B + C
- [ ] Any card + D
- [ ] Two of the same card (e.g., B and B)

---

### Lab Reflection (Answer in your notebook or at the bottom of your .py file)

1. Why did you choose nested `if` statements for this problem instead of (or in addition to) compound conditions?
2. How did you decide the order of your nested conditions? Why does order matter?
3. What was the most challenging combination of cards to handle correctly?
4. How does careful, layered decision-making in this security system remind you of Proverbs 16:9 and Romans 8:28?

---

### Bonus Challenge (if you finish early – 5–10 minutes)

- Allow the user to enter cards in any order and still get the correct highest access level.
- Add a simple “security log” that records which path the nested logic took (using `print()` statements).
- Refactor one part of your nested logic into a flatter version using `and`/`or` and compare readability.

---

You’re done!  
You just independently designed and built a multi-level security access program using nested conditionals — a real-world skill that requires clear, careful, and intentional decision-making.

Save your file as `security_facility_lab.py` and be ready to demonstrate your program and discuss your design choices.

© LogosTeach 2026 - All Rights Reserved.

Labs, Practice Files and Assessments are developed in collaboration with the Grok AI assistant under instructor supervision and review.
