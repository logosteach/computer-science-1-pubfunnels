# Computer Lab: Helping Christine with VBS Registration Decisions

## Learning Objectives

By the end of this lab, you will be able to:
- Write `if`, `elif`, and `else` statements correctly.
- Create multi-way decision structures using `elif`.
- Understand the importance of proper indentation and the colon `:`.
- Control program flow based on different conditions.
- Reflect on how `if-elif-else` structures reflect the choices we make in life — choosing God’s way, our own way, or compromise (Joshua 24:15; Deuteronomy 30:19).

## Lab Topics

- Age validation for VBS
- Allergy and special needs checks
- Registration flow decisions
- Independent vs. chained conditionals

## Materials / Prior Knowledge

**You should already know:** Variables, `input()`, `print()`, and basic comparisons.  
**You will need:** Python editor.

---

### Step 0: Setup (2 minutes)

```python
print("=== VBS Registration Helper for Christine ===\n")
print("Welcome! Let's make sure every child is safe and ready for a great VBS.\n")
```

### Step 1: Age Check with if (5 minutes)

**Context:**  
Christine must ensure all students are ages 5 to 11.

**Your Challenge:**  
Write an `if` statement that welcomes the student only if they are the correct age.

```python
age = int(input("Enter the student's age: "))

if age >= 5 and age <= 11:
    print("Great! This student is eligible for VBS.")
else:
    print("Sorry, this student is outside the 5-11 age range for VBS.")
```

**Expected Output / Test It:**  

Test with ages 4, 7, 11, and 12.

**Question 1:** Why is indentation important after the colon `:`?

### Step 2: Multi-way Decisions - Allergies & Special Needs (6 minutes)

**Context:**  
Christine needs to know about allergies and special learning needs to plan safely.

**Your Challenge:**  
Create a chained `if-elif-else` structure.

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

**Expected Output / Test It:**  
Test all four combinations.

**Question 2:** How does the program decide which message to show?

### Step 3: Overall VBS Planning Check (4 minutes)

**Context:**  
Christine has 10 volunteers and hopes for 30–80 students.

**Your Challenge:**  
Use independent `if` statements for planning.

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

**Expected Output / Test It:**  
Try different student numbers.

**Question 3:** Why can multiple messages print here (independent ifs)?

---

### Lab Reflection (2–3 minutes)
1. What is the difference between chained (`elif`) and independent `if` statements?
2. How can clear conditional logic help Christine serve the children faithfully?
3. In what ways does this lab remind you of making wise choices in life (Joshua 24:15)?

### Bonus Challenge (if time)
Combine the age, allergy, and student count checks into one registration summary for Christine.

---

You’re done!  
You just created a helpful registration tool for Christine’s VBS that uses clear decision-making — just as we are called to make clear choices for God.

Save your file as `vbs_registration_lab.py`.

© 2026 LogosTeach - All Rights Reserved.
