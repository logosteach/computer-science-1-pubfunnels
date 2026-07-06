# Practice File: Short-Circuit Evaluation in Python
#
# Objectives:
# By the end of this practice file, you will be able to:
# - Explain how Python uses short-circuit evaluation with 'and' and 'or'.
# - Predict when Python will stop evaluating parts of a compound condition.
# - Use short-circuit evaluation to write safer and more efficient code.
# - Avoid potential errors (such as division by zero) by understanding evaluation order.
#
# Work through each section. Read the comments carefully and complete the TODOs.
# Test your code by running it frequently.

print("=== Short-Circuit Evaluation Practice ===\n")

# ============================================
# Section 1: Short-Circuit with 'and'
# ============================================

print("--- Section 1: 'and' Operator ---\n")

# With 'and', Python stops as soon as it finds a False value
x = 5
y = 10

result = (x > 10) and (y > 5)
print(f"Result of (x > 10) and (y > 5): {result}")
print("Python did NOT check y > 5 because x > 10 was already False.\n")

# TODO 1: Change the value of x so that both conditions are checked.
# Then run the code and observe the output.


# ============================================
# Section 2: Short-Circuit with 'or'
# ============================================

print("--- Section 2: 'or' Operator ---\n")

age = 17
has_permission = True

can_enter = (age >= 18) or has_permission
print(f"Can enter? {can_enter}")
print("Python stopped after checking has_permission because it was True.\n")

# TODO 2: Change has_permission to False.
# What happens now? Does Python check the age condition?


# ============================================
# Section 3: Using Short-Circuit to Avoid Errors
# ============================================

print("--- Section 3: Avoiding Errors ---\n")

username = ""

# This is safe because of short-circuit evaluation
if username and len(username) > 5:
    print("Username is long enough")
else:
    print("Username is missing or too short")

print("Because username is empty, Python never ran len(username).\n")

# TODO 3: Change username to a string with 3 characters.
# What happens? Why?


# ============================================
# Section 4: Preventing Division by Zero
# ============================================

print("--- Section 4: Safe Division ---\n")

numerator = 20
denominator = 0

# Safe check using short-circuit evaluation
if denominator != 0 and numerator / denominator > 2:
    print("Result is greater than 2")
else:
    print("Cannot divide or result is not greater than 2")

print("Python avoided the division because denominator != 0 was False.\n")

# TODO 4: Change denominator to 5.
# Run the code. Does it now attempt the division?


# ============================================
# Section 5: Order Matters
# ============================================

print("--- Section 5: Order of Conditions ---\n")

has_ticket = False
is_vip = True

# Try switching the order of these conditions and observe the difference
can_watch = has_ticket or is_vip
print(f"Can watch? {can_watch}\n")

# TODO 5: Change the order to: can_watch = is_vip or has_ticket
# Does the result change? Why or why not?


# ============================================
# Reflection Questions (Answer in your notebook)
# ============================================

print("=== Reflection Questions ===")
print("1. What does short-circuit evaluation mean?")
print("2. When using 'and', when does Python stop evaluating?")
print("3. When using 'or', when does Python stop evaluating?")
print("4. Give one real-world example where short-circuit evaluation is helpful.\n")

print(
    "Complete the TODOs above, then discuss your answers with your instructor or classmates."
)

# Copyright 2026 LogosTeach - All Rights Reserved
