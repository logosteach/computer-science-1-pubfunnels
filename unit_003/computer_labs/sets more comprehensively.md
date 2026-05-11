# Computer Lab: Serving with Sets – Managing Ministry Data in Python

## Learning Objectives

By the end of this lab, you will be able to:

- Create and use sets to track unique ministry information (attendees, prayer requests, spiritual gifts)
- Add and remove elements safely from sets
- Perform set operations (union, intersection, difference) to compare ministry groups
- Use `frozenset` for unchanging ministry values
- Understand why sets are fast and when to watch out for common mistakes

## Lab Topics

- Creating and modifying sets
- Set operations (union, intersection, difference)
- `frozenset` for immutable data
- Performance benefits and real ministry applications
- Common pitfalls

## Materials / Prior Knowledge

**You should already know:** Basic lists, `for` loops, `print()`, and simple variables.  
**You will need:** Python installed (any version 3.6+), and a blank file named `ministry_sets_lab.py`

---
### Step 0: Setting Up Our Ministry Data

```python
# Ministry data we'll use throughout the lab
sunday_attendees = ["Alice", "Bob", "Charlie", "Alice", "David", "Eve"]
wed_bible_study = ["Bob", "Eve", "Frank", "Grace"]
prayer_requests = ["heal grandma", "job for Mike", "heal grandma", "church growth"]
spiritual_gifts = ["teaching", "prophecy", "serving", "teaching", "healing"]

# TODO: Convert the lists above into sets where it makes sense
# Create three sets: sunday_set, wed_set, and gifts_set

print("Setup complete - ready to work with unique ministry data!")
```

**Question 0:** Why would we want to turn these lists into sets instead of keeping them as lists?

### Step 1: Creating Sets and Removing Duplicates

**Context:**  
Your church collects attendance and prayer requests. Lists often have duplicates, but sets automatically keep only unique items.

**Your Challenge:**

1. Convert `sunday_attendees` and `prayer_requests` into sets.
2. Print the length of each set using `len()`.
3. Use `.add()` to add one new person to the Sunday set.
4. Use `.discard()` to safely remove a name that might not exist.

```python
# Starter code - fill in the blanks
sunday_set = # your code here
prayer_set = # your code here

print("Unique Sunday attendees:", sunday_set)
print("Number of unique attendees:", len(sunday_set))
print("Unique prayer topics:", prayer_set)
```

**Expected Output / Test It:**

```
Unique Sunday attendees: {'Alice', 'Bob', 'Charlie', 'David', 'Eve'}   # (order may vary)
Number of unique attendees: 5
Unique prayer topics: {'heal grandma', 'job for Mike', 'church growth'}
```

**Question 1:** What happened to the duplicate names and prayer requests?  
**Question 2:** What is the difference between `.remove()` and `.discard()`? When would you use each in a ministry app?

### Step 2: Set Operations – Comparing Ministry Groups

**Context:**  
You want to see who attended both services, who only came on Sunday, and how the groups overlap.

**Your Challenge:**

1. Use `|` (union) to combine Sunday and Wednesday attendees.
2. Use `&` (intersection) to find people who attended both.
3. Use `-` (difference) to find people who only attended Sunday.

```python
# Starter code
both_services = # union of sunday_set and wed_set
common_attendees = # intersection
only_sunday = # difference

print("All unique attendees this week:", both_services)
print("People who attended both:", common_attendees)
print("Only attended Sunday:", only_sunday)
```

**Expected Output / Test It:**

```
All unique attendees this week: {'Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace'}
People who attended both: {'Bob', 'Eve'}
Only attended Sunday: {'Alice', 'Charlie', 'David'}
```

**Question 3:** How could these operations help a pastor or ministry leader?

### Step 3: Frozen Sets and Performance

**Context:**  
Some ministry values (like core prayer focuses) should never change during the year.

**Your Challenge:**

1. Create a `frozenset` called `core_prayer_focuses` with: "evangelism", "discipleship", "worship", "missions".
2. Show that you cannot add to it (try and see what happens).
3. Time how fast a set membership test is compared to a list (use the large list provided).

```python
# Starter code
core_prayer_focuses = frozenset(["evangelism", "discipleship", "worship", "missions"])

# Try adding something (this should fail)
# core_prayer_focuses.add("healing")   # ← uncomment to see error

# Performance demo (already set up for you)
large_list = ["person" + str(i) for i in range(5000)]
large_set = set(large_list)

import time
start = time.time()
"person42" in large_list
list_time = time.time() - start

start = time.time()
"person42" in large_set
set_time = time.time() - start

print(f"List time: {list_time:.5f} sec")
print(f"Set time:  {set_time:.5f} sec")
```

**Expected Output / Test It:**

```
List time: 0.00xxx sec
Set time:  0.00xxx sec   # set should be much faster
```

**Question 4:** Why would a church use a `frozenset` for core values?

### Step 4: Final Integration – Ministry Dashboard

**Context:**  
Put everything together to create a simple ministry report.

**Your Challenge:**
Combine all the sets you created earlier into one final report.

```python
# Final starter code - fill in using your variables from previous steps
all_unique_people = # union of all attendee sets
unique_prayers = # your prayer set
all_gifts = set(spiritual_gifts)   # already unique

print("=== MINISTRY REPORT ===")
print("Total unique people this week:", len(all_unique_people))
print("Shared attendees:", common_attendees)
print("Prayer needs:", unique_prayers)
print("Spiritual gifts represented:", all_gifts)
print("Core focuses (locked):", core_prayer_focuses)
```

**Expected Output / Test It:**

```
=== MINISTRY REPORT ===
Total unique people this week: 7
Shared attendees: {'Bob', 'Eve'}
Prayer needs: {'heal grandma', 'job for Mike', 'church growth'}
Spiritual gifts represented: {'teaching', 'prophecy', 'serving', 'healing'}
Core focuses (locked): frozenset({'evangelism', 'discipleship', 'worship', 'missions'})
```

**Question 5:** What is one way you could expand this lab for your own church ministry?

---
### Final Integration Code

```python
# Run this after completing all steps
sunday_set = set(sunday_attendees)
wed_set = set(wed_bible_study)
prayer_set = set(prayer_requests)
gifts_set = set(spiritual_gifts)
core_prayer_focuses = frozenset(["evangelism", "discipleship", "worship", "missions"])

all_people = sunday_set | wed_set
common = sunday_set & wed_set
only_sunday = sunday_set - wed_set

print("=== FINAL MINISTRY DASHBOARD ===")
print("Unique people:", all_people)
print("Attended both:", common)
print("Prayer topics:", prayer_set)
print("Gifts:", gifts_set)
print("Locked core focuses:", core_prayer_focuses)
```

---
### Lab Reflection (Answer in your notebook)

1. Why would we want to turn these lists into sets instead of keeping them as lists?  
2. What happened to the duplicate names and prayer requests?  
3. What is the difference between `.remove()` and `.discard()`?  
4. How could these set operations help a pastor or ministry leader?  
5. Why would a church use a `frozenset` for core values?  
6. What is one way you could expand this lab for your own church ministry?

### Bonus Challenge (Extra Credit – 5 minutes)

Create a new set called `avoid_topics` with things like "politics" and "complaints".  
Use `.isdisjoint()` to check if your `prayer_set` has nothing in common with the avoid set.  
Print a friendly message based on the result.

---
You’re done!  
You just built a practical ministry dashboard using Python sets — great work! This will help you serve your church more efficiently with clean, unique data.

Save your file as `ministry_sets_lab.py` and be ready to discuss your answers in class!

&copy; LogosTeach 2026 - All Rights Reserved.
