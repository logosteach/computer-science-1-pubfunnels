# Practice: Logical Operators and Compound Conditionals
#
# Learning Objectives:
# - Understand and practice the logical operators: and, or, not, and XOR
# - Learn how to build and evaluate compound conditional expressions
# - Apply logical operators to real-world decision-making scenarios
# - Practice using these operators in if statements and expressions
#
# Instructions:
# 1. Read each comment section carefully.
# 2. Run the code to see the output.
# 3. Modify the variables and experiment with different values.
# 4. Add your own examples in the "Your Turn" sections.
#
# Remember: Logical operators return boolean values (True or False).

# Real-world illustration: Deciding whether to go for a hike
# You might check: (weather is good) AND (you have time) AND (trail is open)

print("=== Logical Operators Practice ===")

# Section 1: The 'and' operator (both conditions must be True)
print("\n1. AND Operator (both must be True):")

has_ticket = True
has_id = True
can_enter = has_ticket and has_id
print(f"Has ticket: {has_ticket}, Has ID: {has_id} → Can enter: {can_enter}")

# Real-world: Buying a restricted item (age AND money)
age = 18
has_money = True
can_buy = (age >= 18) and has_money
print(f"Age {age} and has money: {can_buy}")

# Your Turn: Change the values above and predict the result before running

# Section 2: The 'or' operator (at least one condition must be True)
print("\n2. OR Operator (at least one must be True):")

is_raining = False
has_umbrella = True
stay_dry = is_raining or has_umbrella  # Note: stays dry if either is true
print(f"Is raining: {is_raining}, Has umbrella: {has_umbrella} → Stay dry: {stay_dry}")

# Real-world: Can I watch TV? (finished homework OR it's the weekend)
homework_done = False
is_weekend = True
can_watch_tv = homework_done or is_weekend
print(
    f"Homework done: {homework_done} OR weekend: {is_weekend} → Can watch: {can_watch_tv}"
)

# Section 3: The 'not' operator (reverses the boolean value)
print("\n3. NOT Operator (reverses True/False):")

is_cold = True
should_wear_jacket = not is_cold  # False if it is cold? Wait, logic check!
print(f"Is cold: {is_cold} → Should wear jacket? Let's fix logic: {not False}")

# Better real-world example
lights_on = False
is_dark = not lights_on
print(f"Lights on: {lights_on} → Is dark: {is_dark}")

# Section 4: XOR (exclusive or) - True only if exactly one is True
# Python uses != for boolean XOR or ^ for integers/booleans
print("\n4. XOR (exactly one condition True):")

wants_cake = True
wants_ice_cream = False
# Using != for logical XOR
exclusive_treat = wants_cake != wants_ice_cream
print(
    f"Wants cake: {wants_cake}, Wants ice cream: {wants_ice_cream} → Exactly one treat: {exclusive_treat}"
)

# Alternative with bitwise ^ (works on bools too)
print(f"Using ^ : {(wants_cake ^ wants_ice_cream)}")

# Real-world: Choosing between two mutually exclusive options
study_math = True
study_history = False
focus_on_one = study_math != study_history
print(
    f"Study math: {study_math} XOR study history: {study_history} → Focus on one: {focus_on_one}"
)

# Section 5: Compound Conditional Expressions
print("\n5. Compound Conditionals:")

# Combining operators with parentheses for clarity
temperature = 75
is_sunny = True
is_weekend = True

# Real-world: Perfect beach day conditions
perfect_beach_day = (temperature > 70 and is_sunny) and is_weekend
print(f"Temp: {temperature}°F, Sunny: {is_sunny}, Weekend: {is_weekend}")
print(f"Perfect beach day? {perfect_beach_day}")

# More complex example with NOT
user_logged_in = False
has_permission = True
can_access = (user_logged_in and has_permission) or (
    not user_logged_in and False
)  # Simplified
print(
    f"Logged in: {user_logged_in}, Has permission: {has_permission} → Can access: {can_access}"
)

# Section 6: Practice with if statements
print("\n6. Using Logical Operators in Decisions:")

score = 85
attendance = 90
passed_class = (score >= 60) and (attendance >= 80)
if passed_class:
    print("Congratulations! You passed the class.")
else:
    print("Keep working on it!")

# Your Turn: Create your own compound condition
# Example idea: Should I take an umbrella? (raining or forecast_rain) and not (have_car)

# Experiment here:
# raining = True
# forecast_rain = False
# have_car = False
# take_umbrella = ...

# End of Practice File
# Copyright 2026 LogosTeach - All Rights Reserved
