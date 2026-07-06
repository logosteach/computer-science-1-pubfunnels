# Computer Lab Solutions: Helping Christine with VBS Registration Decisions

## Step 0: Setup
```python
print("=== VBS Registration Helper for Christine ===\n")
print("Welcome! Let's make sure every child is safe and ready for a great VBS.\n")
```

## Step 1: Age Check with if
```python
age = int(input("Enter the student's age: "))

if age >= 5 and age <= 11:
    print("Great! This student is eligible for VBS.")
else:
    print("Sorry, this student is outside the 5-11 age range for VBS.")
```

## Step 2: Multi-way Decisions - Allergies & Special Needs
```python
print("\n--- Safety & Support Information ---")
has_allergy = input("Does the student have any allergies (e.g. peanuts)? (yes/no): ").strip().lower()
special_needs = input("Does the student have any special learning needs? (yes/no): ").strip().lower()

if has_allergy == "yes" and special_needs == "yes":
    print("Alert: Provide full allergy info and assign extra volunteer support.")
elif has_allergy == "yes":
    print("Alert: Note peanut/other allergy for snack and craft planning.")
elif special_needs == "yes":
    print("Note: Student may need extra attention or modified activities.")
else:
    print("Student has no reported allergies or special needs.")
```

## Step 3: Overall VBS Planning Check
```python
print("\n--- Planning Overview ---")
num_students = int(input("Estimated number of students: "))
volunteers = 10

if num_students < 30:
    print("Low attendance - consider extra promotion.")
if num_students > 80:
    print("High attendance - may need more volunteers or space.")
if volunteers >= 10:
    print("Good volunteer coverage for this size group.")
```

## Full Combined Solution (Bonus)
```python
# Full VBS Registration Helper
print("=== VBS Registration Helper for Christine ===\n")

age = int(input("Enter the student's age: "))
if age >= 5 and age <= 11:
    print("Great! This student is eligible for VBS.")
else:
    print("Sorry, this student is outside the 5-11 age range for VBS.")

print("\n--- Safety & Support Information ---")
has_allergy = input("Does the student have any allergies (e.g. peanuts)? (yes/no): ").strip().lower()
special_needs = input("Does the student have any special learning needs? (yes/no): ").strip().lower()

if has_allergy == "yes" and special_needs == "yes":
    print("Alert: Provide full allergy info and assign extra volunteer support.")
elif has_allergy == "yes":
    print("Alert: Note peanut/other allergy for snack and craft planning.")
elif special_needs == "yes":
    print("Note: Student may need extra attention or modified activities.")
else:
    print("Student has no reported allergies or special needs.")

print("\n--- Planning Overview ---")
num_students = int(input("Estimated number of students: "))
volunteers = 10

if num_students < 30:
    print("Low attendance - consider extra promotion.")
if num_students > 80:
    print("High attendance - may need more volunteers or space.")
if volunteers >= 10:
    print("Good volunteer coverage for this size group.")

print("\nThank you for helping make VBS a blessing!")
```

## Lab Reflection Answers
1. Chained `if-elif-else` stops at the first True condition. Independent `if` statements check every condition.
2. Clear conditional logic helps Christine serve safely and effectively, reflecting wise stewardship.
3. Just as the code requires clear decisions, we are called to choose God’s way decisively each day.

© 2026 LogosTeach - All Rights Reserved.
