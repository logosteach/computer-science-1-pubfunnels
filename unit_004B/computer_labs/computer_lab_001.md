# Computer Lab: Loops for Ministry

## Learning Objectives
By the end of this lab, you will be able to:
- Use `for` loops with `range()` and lists to repeat actions efficiently.
- Use `while` loops with conditions to handle unknown numbers of repetitions.
- Apply `break`, `continue`, and nested loops in practical programs.
- Understand when to choose a `for` loop versus a `while` loop.

## Lab Topics
- `for` loops and `range()`
- Looping through lists
- `while` loops with user input
- `break` and `continue`
- Nested loops

## Materials / Prior Knowledge
**You should already know:** Basic Python syntax, variables, `input()`, and `print()`.  
**You will need:** Python installed (or Replit / online editor).

---

### Step 0: Setup
```python
# Welcome to Loops for Ministry!
print("Ready to serve through code! ✝️")
```

**Question 0:**  
Why do you think loops are especially useful in ministry contexts (volunteers, prayer requests, camp check-ins, etc.)?

### Step 1: For Loops – Serving Seniors and Children
**Context:**  
Your church is hosting a luncheon for seniors and a kids ministry program. You need an efficient way to welcome people.

**Your Challenge:**
1. Use `range()` to print a welcome message for 12 seniors.
2. Modify it to use the loop variable and assign numbered seats.
3. Create a list of 5 children’s names and greet each one with a `for` loop.
4. Use `range()` with a step value to print every other number from 0 to 20.

```python
# Step 1 starter code
for i in range(12):
    print("Welcome, friend!")
```

**Thought Questions:**
- How might using a `for` loop help you organize volunteers more efficiently at a church event?
- What’s something in your ministry that could be automated using a `for` loop and a list?

### Step 2: While Loops – Prayer Request Counter
**Context:**  
Your prayer team wants to collect requests during a ministry time. The number of requests is unknown.

**Your Challenge:**  
Create a prayer request counter that keeps asking for new requests while the user says "yes".

```python
# Step 2 starter code
prayers = 0
more = "yes"

while more.lower() == "yes":
    request = input("Enter a prayer request: ")
    prayers += 1
    more = input("Would you like to add another prayer request? (yes/no): ")

print("Thank you! We will pray for", prayers, "requests.")
print("May the Lord bless and keep you. (Numbers 6:24-26)")
```

**Thought Questions:**
- How is a `while` loop different from a `for` loop in the way it decides when to stop?
- Can you think of a real-life ministry situation where you would need a `while` loop instead of a `for` loop?

### Step 3: Challenge – Camp Ministry Check-In System
**Context:**  
You are building a check-in system for your church’s summer camp ministry.

**Your Challenge:**
Create a program that:
- Uses a **for** loop to go through a list of campers.
- Uses a **nested loop** to print a simple pattern of stars (or crosses) for each camper’s cabin number.
- Uses a **while** loop with `break` to collect prayer requests until the user types “done”.

```python
# Step 3 starter code
campers = ["Emma", "Noah", "Olivia", "Liam", "Sophia"]
# TODO: Complete the challenge
```

**Thought Questions:**
- How did adding a nested loop change what your program was able to do?
- Which concept from today do you think you’ll use most in your future programming, and why?

---

### Lab Reflection
Answer the questions above in your notebook or submission.

### Bonus Challenge
Add the `else` clause and `continue` to the prayer counter.

---

You just learned how to use loops to serve more effectively in ministry through code!  

Save your file as `loops_for_ministry_lab.py`

&copy; LogosTeach 2026
