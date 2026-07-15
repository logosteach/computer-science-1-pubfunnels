# Computer Lab Solutions: Smart Theme Park Ticket & Access Advisor

## Step 0: Setup & Welcome

```python
print("=== Adventure Kingdom Theme Park Ticket Advisor ===\n")
print("Welcome! Let's get you the right ticket and ride access.\n")
```

## Step 1: Gather Guest Information

```python
age = int(input("Enter guest age: "))
height = int(input("Enter height in inches: "))
has_pass = input("Do you have a Season Pass? (yes/no): ").strip().lower()

print(f"Confirmed: Age {age}, Height {height} inches, Season Pass: {has_pass}")
```

## Step 2: Ticket Price with if / elif / else

```python
if age <= 3:
    ticket_price = 0
    ticket_type = "Toddler (Free)"
elif age <= 12:
    if has_pass == "yes":
        ticket_price = 25
        ticket_type = "Child with Season Pass"
    else:
        ticket_price = 35
        ticket_type = "Child"
elif age <= 64:
    if has_pass == "yes":
        ticket_price = 40
        ticket_type = "Adult with Season Pass"
    else:
        ticket_price = 55
        ticket_type = "Adult"
else:  # age >= 65
    if has_pass == "yes":
        ticket_price = 20
        ticket_type = "Senior with Season Pass"
    else:
        ticket_price = 30
        ticket_type = "Senior"

print(f"Ticket Type: {ticket_type}")
print(f"Ticket Price: ${ticket_price}")
```

**Note on Best Practice:** The nested `if` for the pass is acceptable here because the age groups are exclusive and the pass decision is simple. An alternative flatter version using compound conditions is also fine if the student prefers it.

## Step 3: Ride Access with Ternary Operator

```python
ride_access = "Full access to all rides" if height >= 48 else "Limited access (smaller rides only)"
height_message = "Tall enough for the coaster!" if height >= 48 else "Sorry, height requirement not met."

print(f"Ride Access: {ride_access}")
print(f"Height Message: {height_message}")
```

## Step 4: Best Practices & Common Pitfalls – Clean Version

```python
day = "saturday"
is_weekend = day == "saturday" or day == "sunday"

if is_weekend:  # never write == True
    print("Weekend pricing applies!")
    special_offer = "Free cotton candy" if age < 12 else "Free popcorn"
else:
    special_offer = "None"

if age >= 65 and has_pass == "yes":
    print("Senior Season Pass holder – extra 10% off!")

print(f"Special Offer: {special_offer}")
```

**What was fixed:**
- Changed `if is_weekend = True:` → `if is_weekend:`
- Added the missing colon and fixed indentation
- Removed the unnecessary `== True`
- Kept the ternary for the offer (good use of it)
- Added a clear print for the special offer

## Step 5: Final Integration – Complete Working Program

```python
print("=== Adventure Kingdom Theme Park Ticket Advisor ===\n")
print("Welcome! Let's get you the right ticket and ride access.\n")

# --- Inputs ---
age = int(input("Enter guest age: "))
height = int(input("Enter height in inches: "))
has_pass = input("Do you have a Season Pass? (yes/no): ").strip().lower()

print(f"\nConfirmed: Age {age}, Height {height} inches, Season Pass: {has_pass}\n")

# --- Ticket Price (if/elif/else) ---
if age <= 3:
    ticket_price = 0
    ticket_type = "Toddler (Free)"
elif age <= 12:
    if has_pass == "yes":
        ticket_price = 25
        ticket_type = "Child with Season Pass"
    else:
        ticket_price = 35
        ticket_type = "Child"
elif age <= 64:
    if has_pass == "yes":
        ticket_price = 40
        ticket_type = "Adult with Season Pass"
    else:
        ticket_price = 55
        ticket_type = "Adult"
else:
    if has_pass == "yes":
        ticket_price = 20
        ticket_type = "Senior with Season Pass"
    else:
        ticket_price = 30
        ticket_type = "Senior"

print(f"Ticket Type: {ticket_type}")
print(f"Ticket Price: ${ticket_price}")

# --- Ride Access (ternary) ---
ride_access = "Full access to all rides" if height >= 48 else "Limited access (smaller rides only)"
height_message = "Tall enough for the coaster!" if height >= 48 else "Sorry, height requirement not met."

print(f"Ride Access: {ride_access}")
print(f"Height Message: {height_message}")

# --- Special Offer (cleaned best-practice code) ---
day = "saturday"
is_weekend = day == "saturday" or day == "sunday"

if is_weekend:
    print("Weekend pricing applies!")
    special_offer = "Free cotton candy" if age < 12 else "Free popcorn"
else:
    special_offer = "None"

if age >= 65 and has_pass == "yes":
    print("Senior Season Pass holder – extra 10% off!")

print(f"Special Offer: {special_offer}")

# --- Final Summary ---
print("\n========== YOUR ADVENTURE KINGDOM SUMMARY ==========")
print(f"Ticket: {ticket_type} - ${ticket_price}")
print(f"Access: {ride_access}")
print(f"Offer: {special_offer}")
closing = "Have a fantastic day, Season Pass holder!" if has_pass == "yes" else "Enjoy your visit!"
print(closing)
print("===================================================")
```

## Bonus Challenge Sample Solutions

### Dynamic day of the week
```python
day = input("What day is it? ").strip().lower()
is_weekend = day in ("saturday", "sunday")
```

### Extra senior ternary
```python
senior_bonus = " + Senior Pass bonus!" if (age >= 65 and has_pass == "yes") else ""
print(f"Special Offer: {special_offer}{senior_bonus}")
```

### Simple debug mode
```python
print(f"[DEBUG] age <= 3? {age <= 3}")
print(f"[DEBUG] age <= 12? {age <= 12}")
print(f"[DEBUG] height >= 48? {height >= 48}")
print(f"[DEBUG] has_pass == 'yes'? {has_pass == 'yes'}")
print(f"[DEBUG] is_weekend? {is_weekend}")
```

---

© LogosTeach 2026 - All Rights Reserved.

> Labs, Practice Files and Assessments are developed in collaboration with the Grok AI assistant under instructor supervision and review.
