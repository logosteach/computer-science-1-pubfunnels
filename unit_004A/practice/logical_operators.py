# Practice File: Logical Operators in Python (and, or, not, xor)
#
# Objectives:
# By the end of this practice file, you will be able to:
# - Use the logical operators 'and', 'or', and 'not' to combine Boolean expressions.
# - Understand and apply the bitwise XOR operator (^) for exclusive or logic.
# - Combine comparison operators with logical operators to create more complex conditions.
# - Write clear, readable code that models wise decision-making and discernment.
#
# This file gives you guided practice with short examples you can run and modify.
# Work through each section, uncomment/test the code, and answer the questions
# in your notebook.

print("=== Logical Operators Practice ===")
print("and, or, not, and XOR (^) allow us to combine conditions.\n")

# Example 1: and (both conditions must be True)
age = 17
has_permission = True

can_attend = (age >= 16) and has_permission
print(f"Age: {age}, Has permission: {has_permission}")
print(f"Can attend event? {can_attend}\n")

# Example 2: or (at least one condition must be True)
has_ticket = False
is_volunteer = True

can_enter = has_ticket or is_volunteer
print(f"Has ticket: {has_ticket}, Is volunteer: {is_volunteer}")
print(f"Can enter? {can_enter}\n")

# Example 3: not (reverses a Boolean value)
is_raining = True
should_go_out = not is_raining
print(f"Is raining: {is_raining}")
print(f"Should go outside? {should_go_out}\n")

# Example 4: XOR (^) - True if exactly one condition is True
likes_math = True
likes_programming = False

exclusive_interest = likes_math ^ likes_programming
print(f"Likes math: {likes_math}, Likes programming: {likes_programming}")
print(f"Has exactly one interest? {exclusive_interest}\n")

# Your Turn - Combine them with comparisons
score = 85
passed_quiz = score >= 70
completed_homework = True

# TODO: Create a condition for "ready for next lesson"
# Use 'and' to require both passing the quiz AND completing homework

# TODO: Use 'or' for "has extra credit or high score"

# TODO: Use 'not' to check if a student needs review

print("Modify the variables above and experiment with the operators!")

# Reflection Questions (answer in notebook):
# 1. What is the difference between 'and' and 'or'?
# 2. When would you use 'not' in a condition?
# 3. How is XOR (^) different from 'or'?

# Copyright 2026 LogosTeach - All Rights Reserved
