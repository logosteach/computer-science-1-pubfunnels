# loop_practice_break_continue.py
# Practice with break and continue statements
# Learning from a position of rest in Christ

print("=== Practice: break and continue in Loops ===\n")

# Example 1: break - Exit the loop early
print("Example 1: Using 'break' to stop early")
for number in range(1, 11):  # numbers 1 to 10
    if number == 5:
        print("   Reached 5 - breaking out of the loop!")
        break  # Stops the loop immediately
    print("   Counting:", number)
print("Loop ended with break.\n")

# Example 2: continue - Skip the rest of the current iteration
print("Example 2: Using 'continue' to skip")
for number in range(1, 11):
    if number % 2 == 0:  # if even number
        continue  # Skip the rest of this iteration (don't print evens)
    print("   Odd number found:", number)
print("Loop finished - evens were skipped.\n")

# Example 3: Combined break and continue (with a simple menu)
print("Example 3: Interactive practice - Finding 'treasure' verses")
print("Type 'quit' to stop, 'skip' to skip a number.\n")

treasure_numbers = [3, 7, 23]  # example "special" numbers

while True:
    try:
        user_input = input("Enter a number (1-30) or 'quit': ").strip().lower()

        if user_input == "quit":
            print("Exiting the search. Well done!")
            break  # Exit the while loop

        num = int(user_input)

        if num < 1 or num > 30:
            print("   Please choose between 1 and 30.")
            continue  # Skip to next iteration

        if num in treasure_numbers:
            print(f"   Found treasure at {num}! (Like a Proverbs gem)")
            break  # Found it - end the loop

        if num % 5 == 0:
            print(f"   {num} is a multiple of 5 - skipping this one.")
            continue  # Skip printing the rest for this turn

        print(f"   Checked {num} - keep searching!")

    except ValueError:
        print("   Please enter a valid number or 'quit'.")
        continue

print("\nGreat job practicing break and continue!")
print(
    "Remember: In the Christian life, we 'break' from sin and 'continue' in grace. (See Romans 6:1-2)"
)

# Copyright (c) 2026 LogosTeach - All Rights Reserved
