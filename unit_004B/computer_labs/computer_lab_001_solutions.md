# Computer Lab: Loops for Ministry - **Solutions Guide**

**Teacher / Solution Version**

---

### Step 0: Setup
```python
# Welcome to Loops for Ministry!
print("Ready to serve through code! ✝️")
```

---

### Step 1: For Loops – Serving Seniors and Children

```python
# 1. Basic for loop with range()
print("=== Senior Luncheon Welcome ===")
for i in range(12):
    print("Welcome, friend! We're glad you're here.")

# 2. Using the loop variable for seat assignments
print("\n=== Assigned Seating ===")
for i in range(12):
    print(f"Seat {i+1}: Welcome, friend! We're glad you're here.")

# 3. Looping through a list of children
print("\n=== Kids Ministry Greetings ===")
children = ["Sarah", "James", "Noah", "Emma", "Liam"]
for child in children:
    print(f"Hello, {child}! Jesus loves you!")

# 4. Range with step
print("\n=== Camp Activity Groups (Every Other Number) ===")
for i in range(0, 21, 2):
    print(i)
```

---

### Step 2: While Loops – Prayer Request Counter

```python
# Step 2 Solution - Prayer Request Counter
prayers = 0
more = "yes"

while more.lower() == "yes":
    request = input("Enter a prayer request: ")
    if request.strip():          # Only count non-empty requests
        prayers += 1
    more = input("Would you like to add another prayer request? (yes/no): ")

print("\nThank you! We will pray for", prayers, "requests.")
print("May the Lord bless and keep you. (Numbers 6:24-26)")
```

---

### Step 3: Challenge – Camp Ministry Check-In System (Full Solution)

```python
# Full Camp Ministry Check-In System
campers = ["Emma", "Noah", "Olivia", "Liam", "Sophia"]

print("=== Camp Ministry Check-In System ===\n")

# For loop through campers + Nested loop for cabin stars
for camper in campers:
    print(f"Checking in {camper}")
    
    # Nested loop: Print stars for cabin number (example: cabin 3 = ***)
    cabin_number = len(camper) % 5 + 1          # Just for demo variety
    print(f"Cabin {camper[:3]}: ", end="")
    for _ in range(cabin_number):
        print("★", end=" ")
    print("\n")

# While loop with break for prayer requests
print("=== Prayer Requests ===")
prayer_count = 0

while True:
    request = input("Enter a prayer request (or type 'done' to finish): ")
    
    if request.lower() == "done":
        break
    if request.strip() == "":          # Skip empty requests
        continue
    
    prayer_count += 1
    print(f"Recorded: {request}\n")

print(f"\nThank you! We collected {prayer_count} prayer requests.")
print("May the Lord bless and keep you. (Numbers 6:24-26)")
```

---

### Bonus Challenge (else clause + continue)

```python
# Bonus: Prayer counter with else and continue
prayers = 0
more = "yes"

while more.lower() == "yes":
    request = input("Enter a prayer request: ").strip()
    
    if not request:
        print("Empty request skipped.")
        continue                    # Skip empty input
    
    prayers += 1
    more = input("Would you like to add another? (yes/no): ").lower()

else:
    # This runs only if the loop ended normally (no break)
    print("\n=== Prayer Time Summary ===")
    print(f"We will pray for {prayers} requests.")
    print("May the Lord bless and keep you. (Numbers 6:24-26)")
```

---

**Lab Reflection Sample Answers (for teacher reference):**

1. Loops help process many people or items efficiently (volunteers, campers, prayer requests).
2. They reduce repetitive code and make programs scalable.
