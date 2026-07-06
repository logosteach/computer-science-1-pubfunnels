# Computer Lab: Comparison Operators in Python
#
# Objectives:
# By the end of this lab, you will be able to:
# - Use the comparison operators <, >, <=, >=, ==, and != correctly.
# - Understand that comparisons return Boolean values (True or False).
# - Apply comparisons in simple real-world scenarios that require discernment.
# - Combine comparisons with variables to make logical decisions.
#
# Complete the TODO sections. Run the code frequently to test your work.
# Answer the reflection questions in your notebook.

print("=== Comparison Operators Lab ===\n")

# Step 0: Setup
age = 17
min_age = 18

# Step 1: Basic Numerical Comparisons
can_enter = age >= min_age   # TODO: Change to test different ages
is_younger = age < min_age

print(f"Age: {age}")
print(f"Can enter event (age >= {min_age})? {can_enter}")
print(f"Is younger than {min_age}? {is_younger}\n")

# Step 2: Equality and Inequality
correct_answer = 42
user_guess = 42   # TODO: Try changing this value

print(f"User guess: {user_guess}")
print(f"Guess is correct (==)? {user_guess == correct_answer}")
print(f"Guess is wrong (!=)? {user_guess != correct_answer}\n")

# Step 3: Range Check with <= and >=
temp = 72
min_comfort = 65
max_comfort = 78

is_comfortable = (temp >= min_comfort) and (temp <= max_comfort)
print(f"Temperature: {temp}°F")
print(f"Comfortable range ({min_comfort}-{max_comfort})? {is_comfortable}\n")

# Final Integration
score = 85
passing = 70

print("=== Grade Check ===")
print(f"Score: {score}")
print(f"Passing (>= {passing})? {score >= passing}")
print(f"Perfect score (== 100)? {score == 100}")
print(f"Needs improvement (!= 100)? {score != 100}")

# Reflection Questions (notebook):
# 1. What is the difference between = and == ?
# 2. What happens when you change the variable values?
# 3. Where else in life do we make comparisons like this?

# Copyright 2026 LogosTeach - All Rights Reserved