# Computer Lab: Mastering Python Dictionaries with "Christ Our Peace"

## Learning Objectives

By the end of this lab, you will be able to:

- Create and modify Python dictionaries
- Access values using keys and safely use `.get()`
- Loop through dictionaries using `.keys()`, `.values()`, and `.items()`
- Work with nested dictionaries and update dictionaries
- Apply dictionaries to organize real information

## Lab Topics

- Dictionary creation and basic operations
- Accessing and modifying data
- Looping through dictionaries
- Nested dictionaries and `.update()`

## Materials / Prior Knowledge

**You should already know:** `print()`, lists, basic `for` loops, strings, and `input()`. 

**You will need:** Python installed and VS Code

---

### Step 0: Set Up - Create a dictionary

Open your VS Code editor and create a file named `christ_our_peace_lab.py`. Then create the following dictionary in this file. Save your work.

```python
christ_our_peace = {
    "Ephesians 2:14": "For he himself is our peace...",
    "John 14:27": "Peace I leave with you; my peace I give you. ...",
    "Philippians 4:7": "And the peace of God, which transcends all understanding...",
    "Colossians 1:20": "And through him to reconcile to himself all things...",
    "Isaiah 9:6": "For to us a child is born... and he will be called ...",
    "Romans 5:1": "Therefore, since we have been justified through faith...",
}
```

### Step 1: Creating Your First Dictionary

**Context:**  
We are building a dictionary that stores Bible verses about Christ being our peace.

**Your Challenge:**

1. Use the reference (e.g. "Ephesians 2:14") as the **key** and the verse text as the **value** and make a print statement.

```python
# print statement goes here
```

**Expected Output / Test It:**

```console
Ephesians 2:14 says, "For he himself is our peace..."
```

**Question 1:** What is the difference between a list and a dictionary?

### Step 2: Accessing and Safely Getting Values

**Context:**  
Sometimes a key might not exist yet. We need to access data safely.

**Your Challenge:**

Try the following code block for yourself.

1. Print the verse for `"John 14:27"`.
2. Use `.get()` to safely get the verse for `"Philippians 4:6"` (which doesn't exist yet) and give a default message.

```python
print("\n--- Step 2: Accessing Values ---")
# Your code here

verse = christ_our_peace["John 14:27"]          # direct access
safe_verse = christ_our_peace.get("Philippians 4:6", "Verse not found yet.")
print(safe_verse)
```

Expected Output

```console
John 14:27: Peace I leave with you, my peace I give you...
Verse not found yet.
```

**Question 2:** What error occurs if you use square brackets `[]` on a key that doesn't exist?

### Step 3: Looping Through the Dictionary

**Context:**  
We want to display all the verses nicely.

**Your Challenge:**

1. Loop through and print **only the references** (keys).
2. Loop through and print **reference + verse** using `.items()`.

Expected Output

```console
# Only References
Ephesians 2:14
John 14:27
Philippians 4:7
Colossians 1:20
Isaiah 9:6
Romans 5:1

# References with the Verse
"Ephesians 2:14": "For he himself is our peace...",
"John 14:27": "Peace I leave with you; my peace I give you. ...",
"Philippians 4:7": "And the peace of God, which transcends all understanding...",
"Colossians 1:20": "And through him to reconcile to himself all things...",
"Isaiah 9:6": "For to us a child is born... and he will be called ...",
"Romans 5:1": "Therefore, since we have been justified through faith..."
```

**Question 3:** Which looping method is best when you need both the key and the value?

### Step 4: Nested Dictionaries & Updating

**Context:**  
We want to add more details about each verse (theme, keywords, etc.).

**Your Challenge:**

1. Add a new entry using `.update()`.
2. Use the given nested dictionary below for one verse with extra information.

```python
print("\n--- Step 4: Updating and Nesting ---")

new_verses = {
    # you type in the verse keys and values here
}

# update() code goes here

# Nested dictionary example
christ_our_peace["Ephesians 2:14"] = {
    "text": "For he himself is our peace...",
    "theme": "Unity and Reconciliation",
    "key_word": "barrier"
}

print("Updated count:", len(christ_our_peace))
```

**Question 4:** What happens to duplicate keys when you use `.update()`?

### Final Integration Code

```python
for ref, data in christ_our_peace.items():
    if isinstance(data, dict):           # nested case
        print(f"\n{ref}")
        print(f"   {data['text']}")
        print(f"   Theme: {data['theme']}")
    else:
        print(f"\n{ref}")
        print(f"   {data}")

print(f"\nTotal verses stored: {len(christ_our_peace)}")
print("Christ Himself is our peace! 🕊️")
```

---

### Lab Reflection (Answer in your notebook)

1. What is one advantage of using a dictionary over a list?
2. What error can occur with square bracket access, and how do you prevent it?
3. Why is `.items()` often the most useful when looping?
4. What happens when `.update()` finds a duplicate key?
5. How did nesting help organize more complex data?

### Bonus Challenge (Extra Credit)

Add at least **two more nested verses** and write code that lets the user type a reference and displays the full information (including nested fields) using `.get()`.

---

**You’re done!**  

You just built a powerful, well-organized dictionary about Christ our Peace using everything you’ve learned.  

Save your file as `christ_our_peace_lab.py` and be ready to discuss your reflections in class!

&copy; LogosTeach 2026 - All Rights Reserved.
