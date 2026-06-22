# loop_practice_pass_else.py
# Practice: pass statement and else clause in loops
# Learning from a position of rest in Christ

print("=== Practice: pass and else in Loops ===\n")

# ====================
# 1. The pass statement
# ====================
print("Example 1: Using 'pass' as a placeholder")

for number in range(1, 6):
    if number == 3:
        print("   Found 3 - doing nothing special yet...")
        pass  # pass does nothing - useful placeholder for future code
    else:
        print("   Processing number:", number)

print("Loop completed with pass.\n")

# Another pass example
print("Example 2: pass in a while loop")
count = 1
while count <= 5:
    if count == 4:
        print("   At 4 - placeholder for later code.")
        pass
    else:
        print("   Counting:", count)
    count += 1
print("While loop finished.\n")

# =========================
# 2. The else clause with loops
# =========================
print("Example 3: for loop with else")
print("The else runs if the loop completes normally (no break)")

for number in range(1, 10):
    print("   Checking:", number)
    if number == 7:
        print("   Found 7 - breaking!")
        break
else:
    # This else only runs if we NEVER hit break
    print("   Loop finished normally - no break occurred.")

print("End of for-else example.\n")

# While loop with else
print("Example 4: while loop with else")
attempt = 1
max_attempts = 5

while attempt <= max_attempts:
    print(f"   Attempt {attempt}")
    if attempt == 3:
        print("   Success on attempt 3!")
        break  # Comment this break out to see the else run
    attempt += 1
else:
    print("   Loop ended normally - no success found within attempts.")

print("End of while-else example.\n")

# ====================
# Practice Section
# ====================
print("=== Now it's your turn! ===")
print("1. Modify the first loop: Use pass when number is even.")
print("2. Create a for loop that searches for a number.")
print("   Add an else clause that prints 'Number not found' if no break occurred.")
print("3. Try a while loop with else that counts until 10 but breaks early.")

print("\nKey Concepts:")
print("- pass: Does nothing. Great placeholder while planning code.")
print("- else with loops: Runs only if the loop finished without a break.")
print("This shows God's faithfulness - He completes what He starts!")

# Bonus challenge idea:
# Write code that loops through numbers 1-20.
# Use pass for multiples of 3, break on 15, and else if never reached.

# Copyright (c) 2026 LogosTeach - All Rights Reserved
