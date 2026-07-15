"""
Practice File: Ternary Operator - Converting if/else to Ternary and Vice Versa

Learning Objectives:
- Write concise conditional expressions using the ternary operator.
- Convert simple if-else statements into ternary form and vice versa.
- Understand when ternary expressions improve readability and when they reduce it.
- Use ternary conditionals appropriately in their code.
- Reflect on how concise, clear communication reflects the gospel — direct, truthful, and full of grace (Colossians 4:6).

Instructions for the Student:
1. Work through each section carefully.
2. Complete every TODO by writing the requested code (ternary or full if-else).
3. Run the program after each section and check that the output matches the expected result.
4. Pay attention to the comments that discuss readability.
5. At the end, answer the reflection questions in comments.
6. Experiment by changing the test values to see different branches.

Remember: Clear and concise code (like clear speech) helps others understand your intent quickly and accurately.
"""

# NOTE: No functions used here (students have not learned them yet).
# Use direct input() calls for any pauses.

print("=== Practice: Ternary Operator Conversions ===")
print(
    "Your mission: Convert between if-else and ternary forms, then decide when each is best!\n"
)


# ============================================================
# Section 1: Convert if-else to Ternary
# ============================================================
print("--- Section 1: Convert Simple if-else to Ternary ---")
print("Rewrite each full if-else as a single ternary expression.")
print("Keep the same variable names and logic.\n")

# Example (already done for you)
age = 20
# Original if-else:
# if age >= 18:
#     status = "Adult"
# else:
#     status = "Minor"
status = "Adult" if age >= 18 else "Minor"
print(f"Example: age={age} → status = {status}")

# TODO 1: Convert this if-else into a ternary
score = 72
# Original:
# if score >= 60:
#     result = "Pass"
# else:
#     result = "Fail"
# Write the ternary version below (it should assign to result):
result = None  # <-- replace None with your ternary expression

print(f"TODO 1: score={score} → result = {result}")
print("Expected: Pass\n")

# TODO 2: Convert this if-else into a ternary
temperature = 45
# Original:
# if temperature > 70:
#     clothing = "shorts"
# else:
#     clothing = "jacket"
# Write the ternary version below:
clothing = None  # <-- replace None with your ternary expression

print(f"TODO 2: temperature={temperature} → clothing = {clothing}")
print("Expected: jacket\n")

# TODO 3: Convert this if-else into a ternary
is_logged_in = True
# Original:
# if is_logged_in:
#     message = "Welcome back!"
# else:
#     message = "Please log in."
# Write the ternary version below:
message = None  # <-- replace None with your ternary expression

print(f"TODO 3: is_logged_in={is_logged_in} → message = {message}")
print("Expected: Welcome back!")
input("\n>>> Press Enter after you have completed Section 1...\n")


# ============================================================
# Section 2: Convert Ternary to Full if-else
# ============================================================
print("\n--- Section 2: Expand Ternary into Full if-else ---")
print("Rewrite each ternary as a clear multi-line if-else block.")
print("This helps you see the structure and practice readability.\n")

# Example (already done)
points = 85
# Original ternary: grade = "A" if points >= 90 else "B"
if points >= 90:
    grade = "A"
else:
    grade = "B"
print(f"Example: points={points} → grade = {grade}")

# TODO 4: Expand this ternary into a full if-else
has_permission = False
# Original ternary: access = "granted" if has_permission else "denied"
# Write the full if-else below (it should assign to access):
access = None  # <-- replace with full if-else that sets access

print(f"TODO 4: has_permission={has_permission} → access = {access}")
print("Expected: denied\n")

# TODO 5: Expand this ternary into a full if-else
hours_studied = 3
# Original ternary: effort = "strong" if hours_studied >= 5 else "needs improvement"
# Write the full if-else below:
effort = None  # <-- replace with full if-else that sets effort

print(f"TODO 5: hours_studied={hours_studied} → effort = {effort}")
print("Expected: needs improvement\n")

# TODO 6: Expand this ternary into a full if-else
is_weekend = True
# Original ternary: activity = "rest and worship" if is_weekend else "work diligently"
# Write the full if-else below:
activity = None  # <-- replace with full if-else that sets activity

print(f"TODO 6: is_weekend={is_weekend} → activity = {activity}")
print("Expected: rest and worship")
input("\n>>> Press Enter after you have completed Section 2...\n")


# ============================================================
# Section 3: Decide Which Form is Better
# ============================================================
print("\n--- Section 3: Choose the Best Form (Readability) ---")
print("For each situation, decide whether a ternary or a full if-else is clearer.")
print(
    "Then write the code using the form you chose. Add a short comment explaining why.\n"
)

# Situation A: Very simple yes/no choice
print("Situation A: Choose a greeting based on whether the user is new.")
is_new_user = True
# TODO 7: Write either a ternary or full if-else (whichever you think is clearer).
# Then print the greeting. Add a comment explaining why you chose that form.
greeting = None  # <-- replace with your chosen form
print(f"  greeting = {greeting}")
# Why I chose this form:

# Situation B: Slightly more complex condition
print("\nSituation B: Decide a discount based on membership and age.")
is_member = True
age = 67
# TODO 8: Write either form. Prefer the clearer one.
# (Hint: You may create a named boolean first if it helps.)
discount = None  # <-- replace with your chosen form
print(f"  discount = {discount}")
# Why I chose this form:

# Situation C: Needs multiple statements or clear steps
print("\nSituation C: Check a score and print a detailed message (side effects).")
score = 55
# TODO 9: Here a full if-else is almost always better because we want to print different messages.
# Write a clear if-else (or if-elif-else) that prints different advice based on the score.
# (Do not use a ternary for this one — practice the multi-line form.)
print("  (Write your if-elif-else that prints advice here)")
# Why full if-else is better here:

input("\n>>> Press Enter after you have completed Section 3...\n")


# ============================================================
# Section 4: Mixed Practice Challenge
# ============================================================
print("\n--- Section 4: Mixed Conversion Challenge ---")
print("Complete the following without looking at previous answers.\n")

# TODO 10: Convert to ternary
weather = "rainy"
# Original:
# if weather == "sunny":
#     plan = "picnic"
# else:
#     plan = "indoor games"
# Write the ternary version below:
plan = None  # <-- replace with your ternary

print(f"TODO 10: weather={weather} → plan = {plan}")
print("Expected: indoor games\n")

# TODO 11: Expand to full if-else
energy = "low"
# Original ternary: mood = "rest and recharge" if energy == "low" else "be productive"
# Write the full if-else below:
mood = None  # <-- replace with full if-else that sets mood

print(f"TODO 11: energy={energy} → mood = {mood}")
print("Expected: rest and recharge\n")

# TODO 12: Your own example
print("TODO 12: Create your own simple decision.")
print("Write both a ternary version and a full if-else version of the same logic.")
print("Then print the result from both so they match.")
print(
    "Idea: decide whether a light should be 'on' or 'off' based on time of day, or invent your own."
)

time_of_day = "night"  # change this value to test different cases

# Ternary version (write it):
light = None  # <-- your ternary here

# Full if-else version (write it):
light_if = None  # <-- your if-else here (or leave as is and fill properly)

print(f"  Ternary: light = {light}")
print(f"  if-else: light_if = {light_if}")
print("  (They should match! Change time_of_day and re-run to test.)")

input("\n>>> Press Enter after you have completed Section 4...\n")


# ============================================================
# Reflection Questions
# ============================================================
print("\n=== Final Reflection ===")
print("Answer these questions as comments below (or in your notebook).")
print("These help connect programming skill with wise living.\n")

"""
1. Which conversion direction (if-else → ternary or ternary → if-else) felt easier? Why?

2. Give one example from this practice file where the ternary form was clearly better, and one where the full if-else was clearly better. Explain your reasoning.

3. How can you quickly decide whether a ternary will improve or reduce readability?

4. Colossians 4:6 (NKJV) says: “Let your speech always be with grace, seasoned with salt, that you may know how you ought to answer each one.”
   How does writing clear, concise conditional expressions (whether ternary or if-else) reflect this call to graceful, purposeful communication?

5. What is one habit you will form so that you choose the right form (ternary or full if-else) for the situation?
"""

print(
    "Great work! You now have practical experience converting between if-else and ternary forms"
)
print(
    "and deciding when each is most appropriate. Keep your code (and your words) clear and gracious!"
)

# Copyright 2026 LogosTeach - All Rights Reserved

# Labs, Practice Files and Assessments are developed in collaboration with the Grok AI assistant under instructor supervision and review.
