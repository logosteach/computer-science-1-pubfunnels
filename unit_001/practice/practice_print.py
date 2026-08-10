# =============================================================================
# Practice: The print() Function
# =============================================================================
# Learning Objectives:
#   - Use the print() function to output text, numbers, and combinations of both.
#   - Print multiple values using comma separation (works with mixed types).
#   - Concatenate strings with the + operator and convert non-strings with str().
#   - Control the ending of a print statement with the end= parameter.
#   - Use common escape characters: \n (newline), \t (tab), \\ (backslash),
#     \" (double quote), and \' (single quote).
#   - Create clear, intentional output messages.
#
# Biblical Connection:
#   Colossians 4:6 (NKJV) – “Let your speech always be with grace, seasoned
#   with salt, that you may know how you ought to answer each one.”
#   Clear, purposeful output in our programs is a small picture of the clear,
#   gracious speech God calls us to in everyday life.
#
# Instructions for the Student:
#   1. Read each section carefully.
#   2. Predict what the code will print BEFORE you run it.
#   3. Run the file and compare your predictions with the actual output.
#   4. Complete the challenges where you see TODO comments.
#   5. Experiment by changing values and re-running the file.
# =============================================================================

print("=" * 70)
print("PART 1: Basic print() and Comma Separation")
print("=" * 70)

# The simplest use of print – a single string
print("Hello, world!")

# You can print numbers directly
print(42)
print(3.14)

# Comma separation lets you print multiple items in one statement.
# Python automatically puts a space between each item.
print("Hello", "world!")
print("The answer is", 42)
print("Name:", "Hannah", "Age:", 13)

# IMPORTANT: Commas work with MIXED types (strings + numbers) without error.
print("Score:", 95, "out of", 100)
print("Pi is approximately", 3.14159)

# You can also print variables of different types with commas
name = "Daniel"
age = 14
grade = 9.5
print("Student:", name, "Age:", age, "GPA:", grade)


print("\n" + "=" * 70)
print("PART 2: Concatenation with the + Operator")
print("=" * 70)

# The + operator joins (concatenates) strings together.
# Notice there is NO automatic space – you must add it yourself if you want one.
print("Hello" + "world")          # Helloworld  (no space)
print("Hello" + " " + "world")    # Hello world (space added manually)

# You CANNOT directly add a string and a number with +
# The line below would cause a TypeError if it were not commented out:
# print("The answer is " + 42)     # TypeError: can only concatenate str (not "int") to str

# To concatenate a number (or any non-string) you must convert it with str()
print("The answer is " + str(42))
print("Score: " + str(95) + " out of " + str(100))

# Compare the two approaches side-by-side
print("\n--- Comma vs + ---")
print("Comma version :", "Age is", 14)                 # easy mixed types
print("Plus version  :", "Age is " + str(14))          # must convert number

# Tip: Use commas when you just want to display several values.
#      Use + when you need to build one single string (for example, to store it).


print("\n" + "=" * 70)
print("PART 3: Controlling the Ending with end=")
print("=" * 70)

# By default, every print() ends with a newline (\n).
# That is why each print appears on its own line.
print("This is line 1")
print("This is line 2")

# You can change (or remove) the ending character(s) with the end= parameter.
print("Hello", end="")          # no newline – next print continues on same line
print(" World!")                # continues right after "Hello"

print("Loading", end="")
print("...", end="")
print(" Done!")

# You can end with any string you like
print("First", end=" --> ")
print("Second", end=" --> ")
print("Third")

# Common pattern: print items on the same line with a custom separator-like ending
print("One", end=" | ")
print("Two", end=" | ")
print("Three")


print("\n" + "=" * 70)
print("PART 4: Escape Characters")
print("=" * 70)

# Escape characters let you include special characters inside a string.
# They begin with a backslash \

print("--- Newline \\n ---")
print("Line one\nLine two\nLine three")

print("\n--- Tab \\t ---")
print("Name:\tHannah")
print("Age:\t13")
print("Grade:\t9")

print("\n--- Backslash \\\\ ---")
# To print an actual backslash you must escape it
print("This is a backslash: \\")
print("File path example: C:\\Users\\Student\\Documents")

print("\n--- Quotes inside strings ---")
# Double quote inside a double-quoted string needs \"
print("She said, \"Hello!\"")

# Single quote inside a single-quoted string needs \'
print('It\'s a beautiful day.')

# Or just switch the outer quotes so you do not need an escape
print("It's a beautiful day.")          # outer double quotes
print('She said, "Hello!"')             # outer single quotes

print("\n--- Combining escapes ---")
print("Student:\tDaniel\nAge:\t\t14\nQuote:\t\"Keep practicing!\"")


print("\n" + "=" * 70)
print("PART 5: Practice Challenges")
print("=" * 70)
print("Predict the output, then run the file and check yourself.\n")

# Challenge 1 – Comma separation
print("Challenge 1:")
print("What will this print?")
print("Python", "is", "fun", 100)
print("Your prediction: _______________________________\n")

# Challenge 2 – + and str()
print("Challenge 2:")
print("Fix the commented line below so it prints correctly using + and str().")
# TODO: Uncomment and fix the next line
# print("My favorite number is " + 7)
print()

# Challenge 3 – end=
print("Challenge 3:")
print("Use end= so the three prints below appear on ONE line separated by ' - '")
# TODO: Add the correct end= arguments
print("Apples")
print("Bananas")
print("Cherries")
print()

# Challenge 4 – Escape characters
print("Challenge 4:")
print("Write a single print statement that produces exactly this output:")
print("""
Name:    Sarah
Age:     15
Motto:   "Never give up!"
""")
print("Your code goes here (replace the pass):")
# TODO: Write your print statement below
pass


print("\n" + "=" * 70)
print("PART 6: Put It All Together")
print("=" * 70)
print("""
Write a short program (using only print statements) that displays
a simple student report card with the following requirements:

  - Use comma separation for at least one line.
  - Use + and str() for at least one line.
  - Use end= so two pieces of information appear on the same line.
  - Use \\n and \\t to format the output neatly.
  - Include at least one escaped quote.

Example target layout (yours can vary):

=== Report Card ===
Student:  Alex Rivera
Grade:    10
Math:     92
Science:  88
Comment:  "Excellent work this semester!"
===================
""")

# TODO: Write your report-card print statements below this line



print("\n" + "=" * 70)
print("Great work!")
print("You now know how to display information clearly with print(),")
print("mix types safely, control line endings, and use escape characters.")
print("Clear output in code is a small practice of clear, purposeful")
print("communication – the kind Colossians 4:6 encourages us toward.")
print("=" * 70)

# Copyright 2026 LogosTeach - All Rights Reserved

# Labs, Practice Files and Assessments are developed in collaboration with the Grok AI assistant under instructor supervision and review.
