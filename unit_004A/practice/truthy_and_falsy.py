"""
Practice File: Truthy and Falsy Values in Python

Learning Objectives:
- Explain the concept of truthy and falsy values in Python.
- Identify which values evaluate to True and which evaluate to False in a Boolean context.
- Use implicit Boolean checking (e.g., if name: instead of if name != "").
- Understand the difference between explicit == True and implicit truthy evaluation.
- Reflect on the fact that God sees things perfectly as they truly are. Nothing is hidden from His sight.
  From our perspective, truth can seem relative sometimes, and uncertain. We are prone to think that God
  Himself thinks and sees things this way as well. Yet, in Christ Jesus we have direct access to our
  Heavenly Father. He is teaching us, training us in godliness in Christ Jesus so that the falsehoods
  of the world will become clearer, and we will be prepared for every good work in Christ Jesus.
  (Romans 12:2, Titus 2:11-12, 1 John 2:17 NKJV)

Instructions for the Student:
1. Run this file multiple times and try different inputs.
2. Predict what each section will print BEFORE running it.
3. Modify the code where indicated (look for TODO comments) and observe the results.
4. Pay special attention to surprising cases (empty strings, zero, empty lists, etc.).
5. Complete the reflection questions at the end.
"""


def pause():
    """Pause execution until the user presses Enter."""
    input("\n>>> Press Enter to continue to the next section...\n")


print("=== Truthy and Falsy Values Practice ===\n")
print(
    "Python evaluates almost every value as either 'truthy' (acts like True) or 'falsy' (acts like False) in if statements and Boolean contexts."
)
print("Let's explore this together!\n")

# ============================================================
# Section 1: Exploring Common Values with bool()
# ============================================================
print("--- Section 1: Using bool() to see truthy/falsy ---")

# Try changing these values and re-running the script
test_values = [
    True,
    False,
    None,
    0,
    0.0,
    1,
    -5,
    3.14,
    "",
    "hello",
    "0",  # string containing zero
    [],
    [1, 2, 3],
    {},
    {"key": "value"},
    set(),
    (0,),  # tuple with one element
]

for value in test_values:
    print(f"bool({repr(value):<20}) → {bool(value)}")

print(
    "\nObservation: Which values surprised you? Why do you think empty collections and zero are falsy?"
)

pause()

# ============================================================
# Section 2: Implicit Boolean Checking (Pythonic Style)
# ============================================================
print("\n--- Section 2: Implicit vs Explicit Checking ---")

# Example 1: Checking a name
name = input("Enter a name (press Enter for empty): ")

# Explicit way (works but less Pythonic)
if name != "":
    print(f"  Explicit check: Hello, {name}!")
else:
    print("  Explicit check: Name is empty.")

# Implicit / Truthy way (recommended)
if name:
    print(f"  Implicit check: Hello, {name}!")
else:
    print("  Implicit check: Name is empty.")

print(
    "\nBoth produce the same result here, but the implicit version is cleaner and more Pythonic."
)

pause()

# ============================================================
# Section 3: Practice Challenge - Shopping Cart
# ============================================================
print("\n--- Section 3: Practice Challenge ---")
print(
    "Complete the code below so it correctly handles an empty cart vs one with items."
)

# TODO: Change this list to test different scenarios (empty, one item, multiple items)
cart = []

if cart:  # This is the implicit/truthy check
    print(f"Your cart has {len(cart)} item(s).")
    print("Thank you for shopping with us!")
else:
    print("Your cart is empty. Please add some items.")

# Try changing the line above to: cart = ["apple", "banana"]
# What happens? Why does an empty list evaluate to False?

pause()

# ============================================================
# Section 4: Numbers and the Zero Gotcha
# ============================================================
print("\n--- Section 4: Careful with Numbers ---")

score = 0  # Change this to 85, -3, or 0 and observe

if score:
    print(f"Great job! Your score is {score}.")
else:
    print("No score recorded yet (or score is zero).")

print(
    "\nNote: 0 is falsy in Python. This can be surprising when 0 is a valid value (like a score of zero)."
)
print(
    "In such cases, you might prefer an explicit check like: if score is not None or if score >= 0"
)

pause()

# ============================================================
# Section 5: Explicit == True vs Implicit (Avoid this pattern)
# ============================================================
print("\n--- Section 5: Explicit vs Implicit Comparison ---")

is_active = 1  # This is truthy but NOT the boolean True
is_logged_in = True

print("Testing with 'is_active = 1' (truthy but not exactly True):")

if is_active == True:
    print("  Using == True: Detected as active")
else:
    print("  Using == True: Not detected")

if is_active:
    print("  Using implicit truthy: Detected as active (recommended)")
else:
    print("  Using implicit truthy: Not detected")

print(
    "\nLesson: Prefer the implicit version in most cases. It is cleaner and works for all truthy values."
)

pause()

# ============================================================
# Section 6: Your Turn - Write Your Own Check
# ============================================================
print("\n--- Section 6: Your Challenge ---")
print(
    "Write a short piece of code that uses implicit truthy checking to validate user input."
)
print("For example: Check if a username and email were provided.")

# TODO: Write your code here (uncomment and complete the lines below)
# username = input("Enter username: ").strip()
# email = input("Enter email: ").strip()
#
# if username and email:
#     print("Both fields provided - ready to register!")
# else:
#     print("Please provide both username and email.")

print("\n(After writing your code, run the script and test it with different inputs.)")

# ============================================================
# Reflection Questions (Answer in comments or your notebook)
# ============================================================
pause()

print("\n--- Final Reflection ---")
print("Answer these questions to deepen your understanding:")

"""
1. Which falsy value surprised you the most and why?

2. When would you choose an implicit truthy check over an explicit one? Give an example from this practice file.

3. Why can `if score == True:` be problematic when `score = 1` or `score = 5`?

4. How does learning to see values "as they truly are" in Python remind you of the biblical truth that God sees things perfectly as they truly are? (Romans 12:2, Titus 2:11-12, 1 John 2:17)

5. What is one way you can apply implicit Boolean checking in a real program you might write?
"""

# Try changing values throughout this file and re-running it.
# The goal is to build intuition for how Python sees "truth."

# Copyright 2026 LogosTeach - All Rights Reserved

# Labs, Practice Files and Assessments are developed in collaboration with the Grok AI assistant under instructor supervision and review.

