# 1. Create and understand nested for and while loops
for outer in range(3):  # Outer loop
    for inner in range(4):  # Inner loop
        print(f"({outer}, {inner})", end=" ")
    print()  # New line after inner loop
