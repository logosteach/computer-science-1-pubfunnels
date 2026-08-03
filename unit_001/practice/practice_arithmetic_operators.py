# =============================================================================
# Practice: Arithmetic Operators and Order of Operations
# =============================================================================
# In this file you will practice the basic math operators in Python:
#   +   Addition
#   -   Subtraction
#   *   Multiplication
#   /   Division (true division – always returns a float)
#   //  Floor division (divides and rounds down to nearest integer)
#   %   Modulo (gives the remainder after division)
#   **  Exponentiation (raises a number to a power)
#
# You will also practice the ORDER OF OPERATIONS (PEMDAS):
#   1. Parentheses          ()
#   2. Exponents            **
#   3. Multiplication / Division / Floor Division / Modulo   *  /  //  %
#      (these all have the SAME priority and are evaluated LEFT TO RIGHT)
#   4. Addition / Subtraction   +  -
#      (these also have the SAME priority and are evaluated LEFT TO RIGHT)
#
# Tip: When in doubt, use parentheses to make the order clear!
# =============================================================================

print("=" * 60)
print("PART 1: Individual Operators")
print("=" * 60)

# ----- Addition (+) -----
print("\n--- Addition (+) ---")
print(5 + 3)          # 8
print(10 + (-4))      # 6   (adding a negative number)
print(2.5 + 3.7)      # 6.2

# ----- Subtraction (-) -----
print("\n--- Subtraction (-) ---")
print(10 - 4)         # 6
print(5 - 12)         # -7
print(3.5 - 1.2)      # 2.3

# ----- Multiplication (*) -----
print("\n--- Multiplication (*) ---")
print(6 * 7)          # 42
print(4 * (-3))       # -12
print(2.5 * 4)        # 10.0

# ----- True Division (/) -----
# Always returns a float, even if the result is a whole number
print("\n--- True Division (/) ---")
print(10 / 2)         # 5.0   (notice the .0 – it is a float)
print(7 / 2)          # 3.5
print(9 / 4)          # 2.25

# ----- Floor Division (//) -----
# Divides and then rounds DOWN toward negative infinity
print("\n--- Floor Division (//) ---")
print(10 // 3)        # 3     (3.333... rounded down)
print(7 // 2)         # 3
print(9 // 4)         # 2
print(-7 // 2)        # -4    (rounds toward negative infinity!)

# ----- Modulo (%) -----
# Gives the remainder after division
print("\n--- Modulo (%) ---")
print(10 % 3)         # 1     (10 = 3*3 + 1)
print(15 % 4)         # 3
print(20 % 5)         # 0     (exact multiple – no remainder)
print(7 % 2)          # 1     (useful for checking odd/even)

# ----- Exponentiation (**) -----
print("\n--- Exponentiation (**) ---")
print(2 ** 3)         # 8     (2 to the power of 3)
print(5 ** 2)         # 25
print(9 ** 0.5)       # 3.0   (square root)
print(2 ** 10)        # 1024


print("\n" + "=" * 60)
print("PART 2: Order of Operations (PEMDAS)")
print("=" * 60)

# Multiplication happens before addition
print("\n2 + 3 * 4 =", 2 + 3 * 4)          # 14  (not 20)
# Parentheses force addition first
print("(2 + 3) * 4 =", (2 + 3) * 4)      # 20

# Exponents before multiplication
print("\n2 * 3 ** 2 =", 2 * 3 ** 2)        # 18  (3**2 = 9, then 2*9)
print("(2 * 3) ** 2 =", (2 * 3) ** 2)    # 36

# Left-to-right for same-priority operators
print("\n10 - 4 - 3 =", 10 - 4 - 3)        # 3   (left to right: (10-4)-3)
print("20 / 4 / 2 =", 20 / 4 / 2)        # 2.5 (left to right)

# Floor division and modulo also follow left-to-right
print("\n17 // 5 % 3 =", 17 // 5 % 3)    # 0
# Step-by-step:
print("17 // 5 =", 17 // 5)              # 3
print("3 % 3 =", 3 % 3)                  # 0
print("So 17 // 5 % 3 =", 17 // 5 % 3)   # 0


print("\n" + "=" * 60)
print("PART 3: Practice Problems")
print("=" * 60)
print("Try to predict the answer BEFORE you run the code!")
print("Then run the file and check if you were right.\n")

# Problem 1
print("Problem 1:  5 + 2 * 3 ** 2")
print("Your prediction: ________")
print("Actual result:  ", 5 + 2 * 3 ** 2)
print()

# Problem 2
print("Problem 2:  (5 + 2) * 3 ** 2")
print("Your prediction: ________")
print("Actual result:  ", (5 + 2) * 3 ** 2)
print()

# Problem 3
print("Problem 3:  20 - 8 // 3 * 2")
print("Your prediction: ________")
print("Actual result:  ", 20 - 8 // 3 * 2)
print()

# Problem 4
print("Problem 4:  15 % 4 + 2 ** 3")
print("Your prediction: ________")
print("Actual result:  ", 15 % 4 + 2 ** 3)
print()

# Problem 5
print("Problem 5:  2 ** 3 ** 2")   # Note: ** is RIGHT-associative!
print("Your prediction: ________")
print("Actual result:  ", 2 ** 3 ** 2)
print("(Hint: 2 ** (3 ** 2) = 2 ** 9 = 512, not (2 ** 3) ** 2 = 64)")
print()

# Problem 6
print("Problem 6:  100 // 7 % 5 * 2 + 1")
print("Your prediction: ________")
print("Actual result:  ", 100 // 7 % 5 * 2 + 1)
print()


print("=" * 60)
print("PART 4: Challenge – Write your own expressions")
print("=" * 60)
print("""
Try writing 3 expressions of your own that use at least three
different operators and require careful attention to order of operations.
Print the results and add a comment explaining the order.

Example:
print(4 + 12 // 5 * 2 ** 2)   # 4 + ((12 // 5) * (2 ** 2)) = 4 + (2 * 4) = 12
""")

# Write your challenge expressions below:
# print( ... )
# print( ... )
# print( ... )


print("\n" + "=" * 60)
print("Great work! Keep practicing until the order of operations")
print("feels natural. Parentheses are your friends when you want")
print("to be absolutely clear about what happens first.")
print("=" * 60)
