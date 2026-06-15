# 3. Trace the execution of nested loops (outer vs inner)
for outer in range(1, 4):
    print(f"Outer loop: {outer}")
    for inner in range(1, 3):
        print(f"   Inner loop: {inner} (inside outer {outer})")
    print("--- Finished inner loop ---")
