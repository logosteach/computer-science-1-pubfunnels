

# Computer Lab: Prayer Partners - Managing a Ministry Prayer List with Python

## Learning Objectives
By the end of this lab, you will be able to:
- Create and manage Python lists to track real-world information
- Add, access, modify, and remove items from a list
- Sort, reverse, and loop through lists efficiently
- Use lists to organize prayer needs in a Christian ministry context

## Lab Topics
- Creating and populating lists (`append`, `insert`)
- Indexing (positive & negative) and modifying elements
- Removing elements (`del`, `pop()`, `remove()`)
- Organizing lists (`sort`, `sorted`, `reverse`, `reversed`)
- Looping through lists (`for` loop and `enumerate`)

## Materials / Prior Knowledge
**You should already know:** Basic Python syntax, variables, and `print()`  
**You will need:** Python installed (no extra files required)

---

### Step 0: Setting Up Our Prayer List

```python
# Step 0: Create an empty list to hold prayer requests
prayer_list = []   # This will store names and needs

print("Prayer List initialized!")
print("Current list:", prayer_list)
```

**Question 0:** Why is it useful to start with an empty list when building something like a prayer list for your church?

### Step 1: Adding People Who Need Prayer

**Context:**  
In the Body of Christ, we are called to “bear one another’s burdens” (Galatians 6:2). Today we will build a list of people in our church family who need prayer — those who are sick, in the hospital, grieving, or facing job loss.

**Your Challenge:**
1. Add at least 5 prayer requests using `.append()`
2. Use `.insert()` to add one request at the beginning of the list (most urgent)
3. Print the list to see the order

```python
# Starter code
prayer_list = []

# Add requests using append
prayer_list.append("John - recovering from surgery")
prayer_list.append("Maria - lost her husband last week")
# TODO: Add 3 more requests using .append()

# Insert an urgent request at the front
# TODO: Use .insert(0, "message") for the most urgent person

print("Updated Prayer List:")
print(prayer_list)
```

**Expected Output / Test It:**  
```
Updated Prayer List:
['Sarah - in hospital with pneumonia', 'John - recovering from surgery', ...]
```

**Question 1:** What is the difference between `append()` and `insert()`? When would you use each one in a ministry prayer list?

### Step 2: Accessing and Updating Prayer Needs

**Context:**  
Prayer needs change over time. Someone may improve, or we may learn more details. We need to access and modify specific items in our list.

**Your Challenge:**
1. Print the person at index 2 using positive indexing
2. Print the last person using negative indexing (`-1`)
3. Update one person’s status using indexing (e.g., change “in hospital” to “home and improving”)

```python
# Starter code - assume prayer_list already exists from Step 1

print("Person at index 2:", prayer_list[2])

# TODO: Print the last person using negative index

# TODO: Modify the 3rd person (index 2) to show updated status
# Example: prayer_list[2] = "new message"

print("Updated list after modification:")
print(prayer_list)
```

**Expected Output / Test It:**  
One line will show a single person, and the final list will have an updated entry.

**Question 2:** How does negative indexing make it easier to work with the end of a list?

**Question 3:** Why is it important to be able to update items in a prayer list?

### Step 3: Removing Prayer Requests

**Context:**  
When God answers prayer (someone is healed, comforted, or finds a job), we can remove them from the active list and celebrate!

**Your Challenge:**
1. Remove one person using `del` and their index
2. Remove another using `.pop()` (from the end)
3. Remove a specific person by name using `.remove()`

```python
# Starter code
print("Before removals:", prayer_list)

# TODO: Remove the person at index 0 using del

# TODO: Pop the last person and save it in a variable called "answered"

# TODO: Remove one person by their name string using .remove()

print("After removals:", prayer_list)
print("Answered prayer:", answered)
```

**Question 4:** What is the difference between `pop()` and `remove()`?

### Step 4: Organizing the Prayer List

**Context:**  
We often want to pray for people in a specific order — maybe alphabetically or by urgency.

**Your Challenge:**
1. Sort the list alphabetically using `.sort()`
2. Create a reversed version using `reversed()` and turn it into a list
3. Print both the sorted and reversed lists

```python
# Starter code
print("Original:", prayer_list)

# TODO: Sort the list permanently with .sort()

print("Sorted:", prayer_list)

# TODO: Create a reversed version without changing the original
reversed_prayers = list(reversed(prayer_list))

print("Reversed:", reversed_prayers)
```

**Question 5:** When would you use `sorted()` instead of `.sort()`?

### Step 5: Looping Through the Prayer List (Final Integration)

**Context:**  
The most important part of a prayer list is actually praying! Let’s loop through the list to display each need clearly.

```python
# FINAL INTEGRATION CODE - Copy and run this after completing all steps

print("=== CHURCH PRAYER LIST ===\n")

# Basic for loop
for request in prayer_list:
    print("🙏 Pray for:", request)

print("\n--- With Numbers (using enumerate) ---")

# TODO: Use enumerate to number each request
# for index, request in enumerate(prayer_list):
#     print(f"{index+1}. {request}")
```

**Expected Output / Test It:**  
A nicely formatted numbered prayer list.

**Question 6:** How does `enumerate()` make the output more useful for a ministry team?

---

### Lab Reflection (Answer in your notebook)

1. Question 0  
2. Question 1  
3. Question 2  
4. Question 3  
5. Question 4  
6. Question 5  
7. Question 6  

### Bonus Challenge (Extra Credit – 5–10 minutes)

**Context:**  
Create a short “Prayer Update Report” for the church leadership.

**Your Task:**
- Create a new list called `urgent_prayers`
- Add the first 3 items from `prayer_list` into it
- Print a report that says “Top Urgent Prayers for this Week:” followed by the numbered urgent list

---

You’re done!  
You just used Python lists to organize and manage real prayer needs in the Body of Christ — showing that we really are responsible to “carry each other’s burdens.”

Save your file as `prayer_list_lab.py` and be ready to discuss your answers (and maybe share one prayer request) in class!

&copy; LogosTeach 2026 - All Rights Reserved
