"""
Practice File: Nested if/else Statements

Learning Objectives:
- Create and trace nested if statements (if inside another if).
- Understand when nested conditionals are useful versus when compound conditions are better.
- Avoid overly complex nesting that makes code hard to read.
- Debug nested conditional logic by using print() statements and testing different input values.
- Reflect on how nested decisions remind us that God often works through layers of circumstances
  while still guiding us with clarity and purpose (Proverbs 16:9; Romans 8:28 NKJV).

Instructions for the Student:
1. Run this program multiple times.
2. Enter different values for age, has_permission, and has_medical_form when prompted.
3. Try to reach EVERY possible branch of the nested logic.
4. Use the print() statements already provided (and add more if needed) to help you trace
   which path the program takes.
5. After you can reliably reach every branch, try rewriting one of the nested structures
   using a compound condition (and/or) and compare readability.
"""

# ============================================================
# Nested if/else Practice - Youth Group Overnight Camp Registration
# ============================================================

print("=== Youth Group Overnight Camp Registration Checker ===")
print("Enter different values to explore every possible path!\n")

# Get inputs from the student
age = int(input("Enter the student's age: "))
has_permission = (
    input("Has the parent/guardian signed the permission form? (yes/no): ")
    .lower()
    .strip()
)
has_medical_form = (
    input("Has the medical form been completed and turned in? (yes/no): ")
    .lower()
    .strip()
)

print("\n--- Tracing the decision process ---")

# Outer decision: Age requirement for overnight camp
if age >= 12:
    print("Outer branch: Student is 12 or older (age requirement met).")

    # Nested decision: Parental permission form
    if has_permission == "yes":
        print("  Inner branch: Parental permission form is signed.")

        # Innermost decision: Medical form
        if has_medical_form == "yes":
            print("    Innermost branch: Medical form is complete.")
            print(
                ">>> RESULT: Approved! Student is fully registered for the overnight camp."
            )
        else:
            print("    Innermost branch: Medical form is missing.")
            print(
                ">>> RESULT: Almost ready — please submit the completed medical form."
            )
    else:
        print("  Inner branch: Parental permission form is missing.")
        print(
            ">>> RESULT: Permission form required. Please have a parent/guardian sign it."
        )

else:
    print("Outer branch: Student is under 12.")

    # Nested decision for younger students
    if has_permission == "yes":
        print("  Inner branch: Permission form is signed, but student is too young.")
        if has_medical_form == "yes":
            print("    Innermost branch: Medical form is also complete.")
            print(
                ">>> RESULT: Age requirement not met. Overnight camp is for ages 12 and up."
            )
        else:
            print("    Innermost branch: Medical form is also missing.")
            print(
                ">>> RESULT: Student is too young and missing forms. Please wait until age 12."
            )
    else:
        print("  Inner branch: No permission form and under age.")
        print(">>> RESULT: Student must be at least 12 and have all forms completed.")

print("\n--- End of program ---")
print(
    "Challenge: Change the values and re-run until you have seen every possible message above."
)
print("Then try converting one nested block into a flatter version using 'and' / 'or'.")

# ============================================================
# Reflection (optional for student to type answers)
# ============================================================
# How did using print() statements help you understand the flow?
# When would a compound condition (and/or) have been clearer than nesting?
# How does careful, layered decision-making in code remind you of Proverbs 16:9
# and Romans 8:28?

# Copyright 2026 LogosTeach - All Rights Reserved

# Labs, Practice Files and Assessments are developed in collaboration with the Grok AI assistant under instructor supervision and review.
