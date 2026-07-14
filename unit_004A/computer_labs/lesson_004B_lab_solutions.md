# Computer Lab Solutions: Remote Security Facility Access Control

## Learning Objectives (Recap)

By the end of this lab, students will be able to:
- Create and trace nested `if` statements.
- Design multi-level decision logic based on multiple conditions.
- Decide when nested conditionals are useful versus compound conditions.
- Avoid overly complex nesting.
- Debug nested logic by testing different input combinations.
- Reflect on layered decision-making in light of Proverbs 16:9 and Romans 8:28 (NKJV).

---

## Important Access Rule (Clarified)

**Key Card A is required to enter the facility at all.**  
Even if a person has Key Card B, C, or D, **without Key Card A they cannot enter the facility**.  
Higher cards only grant level access *after* the gate has been passed with Card A.

---

## Complete Working Solution (Nested Style)

```python
print("=== Remote Security Facility Access Control ===\n")

# Get card inputs from the user
card1 = input("Enter first key card (A/B/C/D/none): ").strip().upper()
card2 = input("Enter second key card (A/B/C/D/none): ").strip().upper()

print("\n--- Evaluating access privileges ---")

# Normalize "none" and empty inputs
if card1 == "" or card1 == "NONE":
    card1 = "NONE"
if card2 == "" or card2 == "NONE":
    card2 = "NONE"

# Determine which cards the person actually holds
has_A = card1 == "A" or card2 == "A"
has_B = card1 == "B" or card2 == "B"
has_C = card1 == "C" or card2 == "C"
has_D = card1 == "D" or card2 == "D"

# Outer decision: Must have Key Card A to enter the facility
if has_A:
    print("Outer: Key Card A detected — gate access granted.")
    
    # Nested decisions for level access (only evaluated if A is present)
    if has_D:
        print("  Inner: Key Card D also present.")
        print(">>> RESULT: Full access granted to ALL levels.")
    else:
        print("  Inner: No Key Card D.")
        if has_C:
            print("    Innermost: Key Card C present.")
            print(">>> RESULT: Access granted to Levels 1 through 4.")
        else:
            print("    Innermost: No Key Card C.")
            if has_B:
                print("      Deepest: Key Card B present.")
                print(">>> RESULT: Access granted to Levels 1 and 2.")
            else:
                print("      Deepest: Only Key Card A.")
                print(">>> RESULT: Gate access only. No level privileges.")
else:
    # No Key Card A — cannot enter the facility at all
    print("Outer: No Key Card A detected.")
    if has_B or has_C or has_D:
        print("  Inner: Higher card(s) present, but without A they are useless.")
        print(">>> RESULT: Access DENIED. You cannot even enter the facility without Key Card A.")
    else:
        print("  Inner: No valid cards at all.")
        print(">>> RESULT: Access DENIED. Please obtain proper key cards (starting with A).")

print("\n--- End of access check ---")
```

---

## Alternative Cleaner Nested Solution (Recommended)

This version keeps the nesting clear and prioritizes the gate requirement first:

```python
print("=== Remote Security Facility Access Control ===\n")

card1 = input("Enter first key card (A/B/C/D/none): ").strip().upper()
card2 = input("Enter second key card (A/B/C/D/none): ").strip().upper()

print("\n--- Evaluating access privileges ---")

has_A = card1 == "A" or card2 == "A"
has_B = card1 == "B" or card2 == "B"
has_C = card1 == "C" or card2 == "C"
has_D = card1 == "D" or card2 == "D"

if not has_A:
    print("Outer: Missing required Key Card A.")
    print(">>> RESULT: Access DENIED. You cannot enter the facility without Key Card A.")
else:
    print("Outer: Key Card A present — you may enter the facility.")
    
    if has_D:
        print("  Inner: Highest privilege (D) also held.")
        print(">>> RESULT: Full access to ALL levels.")
    elif has_C:
        print("  Inner: Card C held.")
        print(">>> RESULT: Access to Levels 1 through 4.")
    elif has_B:
        print("  Inner: Card B held.")
        print(">>> RESULT: Access to Levels 1 and 2.")
    else:
        print("  Inner: Only Card A.")
        print(">>> RESULT: Gate access only. No level privileges.")

print("\n--- End of access check ---")
```

---

## Sample Test Outputs

**Test 1 – Only A**
```
Enter first key card (A/B/C/D/none): A
Enter second key card (A/B/C/D/none): none

--- Evaluating access privileges ---
Outer: Key Card A present — you may enter the facility.
  Inner: Only Card A.
>>> RESULT: Gate access only. No level privileges.
```

**Test 2 – B + A (correct combination)**
```
Enter first key card (A/B/C/D/none): B
Enter second key card (A/B/C/D/none): A

--- Evaluating access privileges ---
Outer: Key Card A present — you may enter the facility.
  Inner: Card B held.
>>> RESULT: Access to Levels 1 and 2.
```

**Test 3 – C only (NO A) — DENIED**
```
Enter first key card (A/B/C/D/none): C
Enter second key card (A/B/C/D/none): none

--- Evaluating access privileges ---
Outer: Missing required Key Card A.
>>> RESULT: Access DENIED. You cannot enter the facility without Key Card A.
```

**Test 4 – D + B (NO A) — DENIED**
```
Enter first key card (A/B/C/D/none): D
Enter second key card (A/B/C/D/none): B

--- Evaluating access privileges ---
Outer: Missing required Key Card A.
>>> RESULT: Access DENIED. You cannot enter the facility without Key Card A.
```

**Test 5 – D + A (full access)**
```
Enter first key card (A/B/C/D/none): D
Enter second key card (A/B/C/D/none): A

--- Evaluating access privileges ---
Outer: Key Card A present — you may enter the facility.
  Inner: Highest privilege (D) also held.
>>> RESULT: Full access to ALL levels.
```

**Test 6 – No cards**
```
Enter first key card (A/B/C/D/none): none
Enter second key card (A/B/C/D/none): none

--- Evaluating access privileges ---
Outer: Missing required Key Card A.
>>> RESULT: Access DENIED. You cannot enter the facility without Key Card A.
```

---

## Lab Reflection – Sample Answers

1. **Why nested `if` statements?**  
   Nested conditionals naturally model the real-world rule: first check for gate entry (Card A), then (only if entry is allowed) check for higher-level privileges. This layered approach matches the facility’s security protocol perfectly.

2. **Why does order matter?**  
   We must check for the presence of Card A first. Higher cards (B–D) are useless without A. Checking levels before the gate would incorrectly grant access to people who cannot even enter the facility.

3. **Most challenging combination?**  
   The cases of B, C, or D *without* A. Students often forget that higher cards still require the gate card and may incorrectly grant level access. Testing these “almost but not quite” cases is essential.

4. **Biblical connection**  
   Just as the security system requires a foundational key (A) before any higher privileges can be used, God often works through layered circumstances in our lives (Proverbs 16:9). Yet He always provides clear purpose and direction (Romans 8:28). Clear nested logic mirrors careful, ordered decision-making under God’s sovereign guidance.

---

## Instructor Notes

- This is an independent challenge lab. Expect a wide variety of solutions.
- **Critical rule to enforce:** Without Key Card A, access is completely denied — even if B, C, or D is present.
- Look for:
  - Outer check for presence of A (gate)
  - Nested level checks only when A is true
  - Correct handling of “higher cards without A”
  - Ability to handle 0, 1, or 2 cards
  - Readable nesting (ideally no more than 3 levels deep)
  - Presence of tracing print statements
- Common student mistakes:
  - Granting level access when A is missing
  - Checking higher cards before the gate requirement
  - Forgetting to normalize input (`.strip().upper()`)
  - Overly deep or duplicated nesting
  - Not testing the “B/C/D without A” denial cases

---

You’re done reviewing the solutions!

Save this file as `nested_if_security_lab_solutions.md`.

© LogosTeach 2026 - All Rights Reserved.

Labs, Practice Files and Assessments are developed in collaboration with the Grok AI assistant under instructor supervision and review.
