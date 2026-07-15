"""
Practice File: Common Mistakes with Conditional Statements

Learning Objectives:
- Identify common mistakes when working with conditionals (= vs ==, missing colons, incorrect indentation).
- Debug conditional logic effectively.
- Apply best practices for writing clear and maintainable if statements.
- Write readable conditional code that is easy to understand and modify.
- Recognize that just as clear thinking leads to wise living, writing clear conditional logic leads to reliable and trustworthy programs (Proverbs 4:23; 1 Corinthians 14:40).

Instructions for the Student:
1. Read each section carefully. The code contains intentional mistakes.
2. Predict what error or unexpected behavior will occur BEFORE running the code.
3. Fix every mistake so the program runs correctly and produces the expected output.
4. After fixing, run the program and test it with different values.
5. Complete the reflection questions at the end (write answers as comments).
6. Pay special attention to the "Best Practices" section — rewrite the code to make it clearer.

Remember: Clear thinking leads to wise living, and clear conditional logic leads to reliable programs.
"""

# Students use direct input() calls for pauses between sections.


print("=== Practice: Common Mistakes with Conditional Statements ===")
print("Your mission: Find and fix every bug so this program runs correctly!\n")


# ============================================================
# Section 1: = vs ==  (Assignment vs Comparison)
# ============================================================
print("--- Section 1: Assignment (=) vs Equality (==) ---")
print("BUG: Using = instead of == causes a SyntaxError.")
print("Fix the condition so it correctly checks if the age is exactly 18.\n")

# TODO: Fix the mistake below
age = 18
if age = 18:          # <-- This is wrong! Change = to ==
    print("You are exactly 18 years old.")
else:
    print("You are not exactly 18.")

print("Expected output when fixed: You are exactly 18 years old.")
input("\n>>> Press Enter after you have fixed this section and understand it...\n")


# ============================================================
# Section 2: Missing Colon
# ============================================================
print("\n--- Section 2: Missing Colon ---")
print("BUG: Every if / elif / else line must end with a colon (:).")
print("Add the missing colon so the code runs.\n")

# TODO: Fix the missing colon(s)
score = 85
if score >= 90
    print("You earned an A!")
elif score >= 80
    print("You earned a B!")
else
    print("Keep working hard!")

print("Expected output when fixed: You earned a B!")
input("\n>>> Press Enter after you have fixed this section and understand it...\n")


# ============================================================
# Section 3: Incorrect Indentation
# ============================================================
print("\n--- Section 3: Incorrect Indentation ---")
print("BUG: Python requires consistent indentation (usually 4 spaces) for code blocks.")
print("Fix the indentation so both print statements are inside the if block.\n")

# TODO: Fix the indentation
temperature = 75
if temperature > 70:
print("It's warm outside.")          # <-- Needs to be indented
    print("You might want shorts.")  # <-- Inconsistent indentation

print("Expected output when fixed:")
print("It's warm outside.")
print("You might want shorts.")
input("\n>>> Press Enter after you have fixed this section and understand it...\n")


# ============================================================
# Section 4: Debugging Conditional Logic
# ============================================================
print("\n--- Section 4: Debugging Conditional Logic ---")
print("This section has correct syntax but the logic is wrong.")
print("A student who is 16 and has permission should get 'Access denied - too young.'")
print("Currently the logic is inverted. Use print statements to trace the flow, then fix it.\n")

# TODO: Fix the logic so the correct message is printed for age=16
# The intended rule is: only adults (age >= 18) with permission get full access.
# Currently the outer if is inverted — correct it so age 16 produces the "too young" message.
age = 16
has_permission = True

print(f"DEBUG: Checking access for age={age}, has_permission={has_permission}")

# BUG: The outer condition is inverted. Change it so that age >= 18 means "Age requirement met"
if age < 18:
    print("  Outer: Age requirement met.")
    if has_permission:
        print("    Inner: Permission granted.")
        print(">>> RESULT: Full access approved.")
    else:
        print("    Inner: No permission.")
        print(">>> RESULT: Access denied - need permission.")
else:
    print("  Outer: Age requirement NOT met.")
    print(">>> RESULT: Access denied - too young.")

# After you fix it, the output for age=16 should be:
# DEBUG: Checking access for age=16, has_permission=True
#   Outer: Age requirement NOT met.
# >>> RESULT: Access denied - too young.
input("\n>>> Press Enter after you have fixed this section and understand it...\n")


# ============================================================
# Section 5: Best Practices Challenge - Make it Readable
# ============================================================
print("\n--- Section 5: Best Practices for Clear Conditionals ---")
print("The code below works but is hard to read and maintain.")
print("Rewrite it following best practices:")
print("  - Use descriptive boolean variables")
print("  - Keep conditions simple")
print("  - Avoid comparing booleans with == True / == False")
print("  - Make the intent obvious\n")

# TODO: Rewrite this entire block using best practices
# Original (messy) version — replace it with a clean version
age = 20
has_id = True
has_passport = False
is_banned = False

if age>=18 and (has_id==True or has_passport==True) and not (is_banned==True):
    print("Access granted")
else:
    print("Access denied")

print("\nAfter rewriting, the program should still print 'Access granted' for these values.")
print("But the code should be much easier for another programmer (or future you) to understand.")
input("\n>>> Press Enter after you have fixed this section and understand it...\n")


# ============================================================
# Section 6: Your Own Debug Challenge
# ============================================================
print("\n--- Section 6: Put It All Together ---")
print("Below is a small program with THREE different kinds of mistakes.")
print("Find and fix all of them so the program correctly greets the user.\n")

# TODO: Fix all mistakes in this section
name = input("Enter your name: ").strip()
age = int(input("Enter your age: "))

if name = "":                     # Mistake 1: = instead of ==
print("Hello, stranger!")         # Mistake 2: missing indentation
elif age < 13
    print(f"Hi {name}! You are a young learner.")  # Mistake 3: missing colon
else:
    print(f"Welcome, {name}! Glad you are learning Python.")

print("\nWhen fixed, test with different names and ages.")
input("\n>>> Press Enter after you have fixed this section and understand it...\n")


# ============================================================
# Reflection Questions
# ============================================================
print("\n=== Final Reflection ===")
print("Answer the following questions in comments below (or in your notebook).")
print("These help you connect programming skill with wise living.\n")

"""
1. Which common mistake ( = vs ==, missing colon, indentation) was hardest for you to spot? Why?

2. How did adding print() statements (debugging) help you understand the flow of Section 4?

3. In Section 5, how did breaking the condition into named boolean variables make the code clearer?

4. Proverbs 4:23 (NKJV) says: “Keep your heart with all diligence, For out of it spring the issues of life.”
   How does guarding the clarity of our thinking (and our code) affect the reliability of what we produce?

5. 1 Corinthians 14:40 (NKJV) says: “Let all things be done decently and in order.”
   How can writing clear, well-ordered conditional logic be an act of faithfulness in our work?

6. What is one habit you will form so that your future if-statements are always clear and trustworthy?
"""

print("Great work! You have practiced identifying mistakes, debugging logic,")
print("and writing maintainable conditionals. Keep your code (and your thinking) clear!")

# Copyright 2026 LogosTeach - All Rights Reserved

# Labs, Practice Files and Assessments are developed in collaboration with the Grok AI assistant under instructor supervision and review.