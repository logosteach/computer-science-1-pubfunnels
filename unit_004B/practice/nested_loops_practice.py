# nested_loops_practice.py
# Practice with Nested Loops (loops inside loops)
# Learning from a position of rest in Christ

print("=== Practice: Nested Loops ===\n")

# Example 1: Simple nested for loops - Building a grid
print("Example 1: Nested for loops - Creating a small grid")
for row in range(1, 4):  # outer loop: rows
    for col in range(1, 5):  # inner loop: columns
        print(f"({row},{col})", end="  ")  # end=" " keeps it on same line
    print()  # new line after each row
print("Grid complete!\n")

# Example 2: Multiplication table
print("Example 2: Multiplication Table (5x5)")
for outer in range(1, 6):
    for inner in range(1, 6):
        product = outer * inner
        print(f"{outer} x {inner} = {product:2d}", end="   ")
    print()  # new line after inner loop finishes
print("Multiplication table complete.\n")

# Example 3: Nested while loops
print("Example 3: Nested while loops")
outer_count = 1
while outer_count <= 3:
    print(f"   Outer loop level: {outer_count}")
    inner_count = 1
    while inner_count <= 4:
        print(f"      Inner loop: {inner_count}")
        inner_count += 1
    outer_count += 1
print("Nested while loops finished.\n")

# Example 4: Nested loops with break and continue
print("Example 4: Nested loops with break and continue")
for i in range(1, 6):
    print(f"Row {i}: ", end="")
    for j in range(1, 10):
        if j == 7:
            print("... skipping rest of row")
            break  # breaks only the inner loop
        if j % 2 == 0:
            continue  # skips even numbers in inner loop
        print(j, end=" ")
    print()
print("Example with break/continue finished.\n")

# Copyright (c) 2026 LogosTeach - All rights reserved.
