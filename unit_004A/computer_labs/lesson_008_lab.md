# Computer Lab: Smart Theme Park Ticket & Access Advisor

## Learning Objectives

By the end of this lab, you will be able to:
- Write clear multi-way decisions using `if`/`elif`/`else` chains.
- Convert simple `if`/`else` logic into ternary expressions (and know when not to).
- Apply best practices for readable conditionals (order of tests, clear variable names, avoid deep nesting when `elif` works better, never write `== True`).
- Identify and fix common pitfalls (`=` vs `==`, missing colons, bad indentation, unreachable code).
- Combine user input, comparisons, compound conditions, and ternary operators into one working program.
- Reflect on how wise, ordered decision-making in code mirrors the call to do all things “decently and in order” and to choose the path of wisdom (1 Corinthians 14:40; Proverbs 4:26-27 NKJV).

## Lab Topics

- `if` / `elif` / `else` multi-branch logic
- Ternary conditional expressions
- Best practices for clear, maintainable conditionals
- Common pitfalls and how to avoid them
- Real-world decision making with multiple factors
- Testing every important branch

## Materials / Prior Knowledge

**You should already know:** Variables, `input()`, `print()`, f-strings, comparison operators, compound conditions (`and`/`or`/`not`), basic `if`/`elif`/`else`, nested `if`, truthy/falsy values, and the ternary operator.  
**You will need:** A Python editor (IDLE or VS Code) and about 30–40 minutes of focused work.  
**Remember:** You have **not** learned functions yet — do **not** create any `def` statements. Keep everything at the top level.

---

### Lab Scenario

You have been hired by **Adventure Kingdom Theme Park** to build a smart ticket & access advisor for the front gate.

The system must decide:

1. **Ticket Price** based on age group and whether the guest has a Season Pass.
2. **Ride Access** based on height (for the big roller coasters).
3. **Special Offers** using a quick ternary decision.
4. **Final Message** that combines everything cleanly.

The park wants the code to be **easy to read and maintain** (best practices) and free of the common mistakes that confuse new programmers.

---

### Step 0: Setup & Welcome (2 minutes)

Copy this starter code into a new file named `theme_park_lab.py`:

```python
print("=== Adventure Kingdom Theme Park Ticket Advisor ===\n")
print("Welcome! Let's get you the right ticket and ride access.\n")

# You will add more variables and logic below this line.
```

**Question 0:** Why do we start with clear print statements and a blank line? How does this help the user (and future programmers reading your code)?

---

### Step 1: Gather Guest Information (5 minutes)

**Context:**  
The system needs three pieces of information from every guest.

**Your Challenge:**

1. Ask for the guest’s **age** (integer).
2. Ask for the guest’s **height in inches** (integer).
3. Ask if they have a **Season Pass** (`yes` or `no`). Store the answer in a variable called `has_pass` after converting it to lowercase and stripping whitespace.
4. Print a short confirmation of the three values using an f-string.

```python
# Step 1 starter – complete the missing pieces
age = int(input("Enter guest age: "))
height = int(input("Enter height in inches: "))
has_pass = input("Do you have a Season Pass? (yes/no): ").strip().lower()

# TODO: Print a confirmation message with all three values
```

**Expected Output / Test It:**  
```
Enter guest age: 12
Enter height in inches: 52
Do you have a Season Pass? (yes/no): yes
Confirmed: Age 12, Height 52 inches, Season Pass: yes
```

**Question 1:** Why do we use `.strip().lower()` on the Season Pass answer? What common pitfall does this prevent?

---

### Step 2: Ticket Price with if / elif / else (8 minutes)

**Context:**  
Ticket prices are:

- Age 0–3: Free (Toddler)
- Age 4–12: Child price $35 (or $25 with Season Pass)
- Age 13–64: Adult price $55 (or $40 with Season Pass)
- Age 65+: Senior price $30 (or $20 with Season Pass)

**Your Challenge:**

Write a clean `if` / `elif` / `else` chain that:

1. Determines the **base category** and the **final price**.
2. Stores the final price in a variable called `ticket_price`.
3. Stores a short description (e.g., “Child with Season Pass”) in a variable called `ticket_type`.
4. Prints both values clearly.

**Best Practice Reminder:** Order your conditions from most specific or most common first, and use `elif` so only one branch runs. Do **not** nest extra `if`s here when `elif` is clearer.

```python
# Step 2 – write your if/elif/else chain here
# Example skeleton (replace with real logic):
# if age <= 3:
#     ticket_price = 0
#     ticket_type = "Toddler (Free)"
# elif ...
```

**Expected Output / Test It (try all four age groups both with and without pass):**  
```
Ticket Type: Child with Season Pass
Ticket Price: $25
```

**Question 2:** Why is using `elif` better than writing four completely separate `if` statements for the age groups?

---

### Step 3: Ride Access with Ternary Operator (5 minutes)

**Context:**  
The main roller coaster requires a minimum height of **48 inches**. Guests under 48 inches may still ride smaller attractions.

**Your Challenge:**

1. Use a **ternary expression** to set a variable `ride_access` to either `"Full access to all rides"` or `"Limited access (smaller rides only)"`.
2. Use **another ternary** to set a short message `height_message` that says either “Tall enough for the coaster!” or “Sorry, height requirement not met.”.
3. Print both results.

```python
# Step 3 – use ternary operators (no if/else blocks here)
# Example form: variable = value_if_true if condition else value_if_false

ride_access = "Full access to all rides" if height >= 48 else "Limited access (smaller rides only)"
# TODO: Create height_message with a ternary
```

**Expected Output / Test It:**  
```
Ride Access: Full access to all rides
Height Message: Tall enough for the coaster!
```

**Question 3:** When is a ternary expression a good idea? When would a full `if`/`else` block be clearer and safer?

---

### Step 4: Best Practices & Common Pitfalls Fix-It (7 minutes)

**Context:**  
A junior programmer left some messy code. You must clean it up using the best practices and pitfall knowledge you have learned.

**Your Challenge:**

Look at the buggy / messy code below. Fix every problem so it becomes clean, correct, and follows best practices.

**Buggy Code (copy it first, then fix):**

```python
# BUGS TO FIX – rewrite this entire block cleanly
day = "saturday"
is_weekend = day == "saturday" or day == "sunday"
if is_weekend = True:          # pitfall 1
print("Weekend pricing applies!")   # pitfall 2
    special_offer = "Free cotton candy" if age < 12 else "Free popcorn"   # ok-ish but can be improved
else
    special_offer = "None"     # pitfall 3
if age >= 65 and has_pass:     # this is fine but order could be better elsewhere
    print("Senior Season Pass holder – extra 10% off!")
```

**What to fix / improve:**

1. `=` vs `==` mistake.
2. Missing colon and indentation.
3. Writing `== True` (never needed).
4. Make the weekend check clearer and more Pythonic if possible.
5. Keep the ternary for the special offer, but make sure the whole block is readable.
6. Add a clear final print of the special offer.

After you fix it, the program should run without errors and print sensible messages.

**Question 4:** List the three most common conditional pitfalls you just fixed. Why does each one cause problems?

---

### Step 5: Final Integration – Complete Advisor (8 minutes)

**Context:**  
Now put everything together into one smooth program.

**Your Challenge:**

1. Keep the input section from Step 1.
2. Keep (or improve) the ticket price logic from Step 2.
3. Keep the ternary ride access from Step 3.
4. Include the cleaned-up special offer logic from Step 4 (you can hard-code `day = "saturday"` or ask for the day if you want).
5. At the very end, print a nice summary that includes:
   - Ticket type and price
   - Ride access
   - Special offer
   - A friendly closing message that uses a ternary for the closing greeting (e.g., “Have a fantastic day!” if they have a pass, otherwise “Enjoy your visit!”).

**Final Integration Code skeleton (expand it):**

```python
print("=== Adventure Kingdom Theme Park Ticket Advisor ===\n")

# --- Inputs ---
age = int(input("Enter guest age: "))
height = int(input("Enter height in inches: "))
has_pass = input("Do you have a Season Pass? (yes/no): ").strip().lower()

print(f"\nConfirmed: Age {age}, Height {height} inches, Season Pass: {has_pass}\n")

# --- Ticket Price (if/elif/else) ---
# your logic here...

# --- Ride Access (ternary) ---
# your ternary here...

# --- Special Offer (cleaned best-practice code) ---
# your fixed code here...

# --- Final Summary ---
print("\n========== YOUR ADVENTURE KINGDOM SUMMARY ==========")
# print ticket_type, ticket_price, ride_access, special_offer
# final greeting using a ternary
print("===================================================")
```

**Expected Output / Test It (example run):**  
```
=== Adventure Kingdom Theme Park Ticket Advisor ===

Enter guest age: 10
Enter height in inches: 50
Do you have a Season Pass? (yes/no): yes

Confirmed: Age 10, Height 50 inches, Season Pass: yes

Ticket Type: Child with Season Pass
Ticket Price: $25
Ride Access: Full access to all rides
Height Message: Tall enough for the coaster!
Weekend pricing applies!
Special Offer: Free cotton candy

========== YOUR ADVENTURE KINGDOM SUMMARY ==========
Ticket: Child with Season Pass - $25
Access: Full access to all rides
Offer: Free cotton candy
Have a fantastic day, Season Pass holder!
===================================================
```

**Question 5:** How did ordering your `elif` conditions carefully help prevent bugs? What would happen if the adult check came before the child check?

---

### Lab Reflection (Answer in your notebook or as comments at the bottom of your .py file)

1. Why is the order of `if` / `elif` conditions so important? Give one example from this lab.
2. When did you choose a ternary operator, and when did you stick with a full `if`/`elif`/`else`? Why?
3. Which common pitfall do you think is easiest for beginners to make, and how will you avoid it in the future?
4. How does writing clear, well-ordered conditional logic reflect the biblical call to do things “decently and in order” (1 Corinthians 14:40) and to “ponder the path of your feet” (Proverbs 4:26 NKJV)?
5. What is one best practice you will use every time you write conditionals from now on?

---

### Bonus Challenge (Extra Credit – 5–10 minutes)

- Ask the user for the current day of the week and make the weekend special offer dynamic.
- Add one more ternary that gives a different message if the guest is a senior Season Pass holder.
- Add a simple “debug mode” that prints the value of every condition (`True`/`False`) so you can see exactly which branch is taken. (Hint: you can print the conditions themselves.)

---

### Deliverable Instructions

When you finish the lab, complete the following:

1. Save your working Python file as `theme_park_lab.py`.
2. Make sure the program runs without errors for many different combinations of age, height, and pass status.
3. Test at least these key cases:
   - Toddler (age 2, any height, no pass)
   - Child with pass (age 10, height 50, yes)
   - Adult no pass (age 30, height 70, no)
   - Senior with pass (age 70, height 65, yes)
   - Child too short for coaster (age 8, height 45, no)
4. Complete the Lab Reflection questions (as comments in your file or in a notebook).
5. Be ready to demonstrate your program and discuss your design decisions with your instructor or classmates (whether you are working asynchronously alone or in a group setting).

---

### Self-Grading & Engagement Reflection  
*(This is not about points — it is about becoming more aware of how you solve problems.)*

Honestly answer the questions below. There are no right or wrong answers, only opportunities for growth.

**1. Process Awareness**  
- Did I plan the order of my conditions on paper or in comments before coding, or did I jump straight into writing?
- How many different test cases did I actually run while building the program?

**2. Branch Coverage**  
- Can I reach every major ticket type and both ride-access outcomes by changing my inputs?
- Which combination was hardest to get right? Why?

**3. Best Practices & Pitfalls**  
- Did I catch myself writing `== True` or using `=` by accident? How did I fix it?
- Is my final code easy for another student (or my future self) to read?

**4. Design Decisions**  
- Why did I put the age checks in the particular order I chose?
- If I had more time, what would I improve about readability or the final summary?

**5. Faithful Stewardship of Learning**  
- In what ways did careful, ordered decision-making in this lab remind you of walking wisely (Proverbs 4:26-27) and doing things decently and in order (1 Corinthians 14:40)?
- Did I approach this challenge with patience and a desire to truly understand, or mainly try to “get it done”?

**Final Self-Check**  
I have:  
- [ ] A working program that correctly prices tickets for all four age groups  
- [ ] Used at least two ternary expressions appropriately  
- [ ] Fixed the common pitfalls and followed best practices  
- [ ] Tested multiple realistic combinations  
- [ ] Written thoughtful answers to the reflection questions  

If you can check most of these boxes with integrity, you have meaningfully engaged the learning process. Well done!

---

You’re done!  
You just built a complete, real-world ticket advisor that uses every major tool from this unit — `if`/`elif`/`else`, ternary operators, best practices, and careful avoidance of common pitfalls. That is excellent decision-making skill!

Save your file as `theme_park_lab.py` and be ready to discuss your solutions.

© LogosTeach 2026 - All Rights Reserved.

> Labs, Practice Files and Assessments are developed in collaboration with the Grok AI assistant under instructor supervision and review.
