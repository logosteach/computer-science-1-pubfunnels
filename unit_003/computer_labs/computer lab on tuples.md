# Computer Lab: Tuples

## Learning Objectives

By the end of this lab, you will be able to:

- Create tuples in different ways (including single-element and empty tuples)
- Unpack tuples
- Use indexing and slicing (positive and negative)
- Loop through tuples with for, enumerate() and zip()
- Sort a tuple and convert the sorted list back to a tuple().

## Scenario

Jordan owns **Jordan's Ready-Mix Concrete**. He uses Python to help manage his business. Today he needs to work with immutable data -- things that should **never change** after they are recorded (like a delivered concrete mix recipe, a customer order that's already poured, or fixed delivery routes).

He has decided to use **tuples** for this data.

## Materials / Prior Knowledge

**You should already have/know:** Python and VS Code installed on your computer. Knowledge of Python lists.

---

### Step 0: Various Mixes of Cement.

```python
# Standard All-Purpose Mix, Good for sidewalks, driveways, patios
# (cement, sand, gravel ,water)
standard_mix = (400, 800, 1200, 220) # in pounds, 1:2:3 ratio for first three elements

# High Strength Mix, For footings, foundations, or load-bearing work)
# (cement, sand, gravel ,water)
high_strength = (500, 750, 1250, 225) # Higher cement content

# Light-Duty Mix, for non-structural work like garden paths or fence posts
# (cement, sand, gravel ,water)
light_duty = (300, 900, 1500, 210) # 1:3:5: ratio

# Pending-mix
pending_mix = tuple() # An order that has not been made yet.
```

**Question 0:** What makes a tuple the best data structure for these three different types of concrete mixes?

### Step 1: Extract the amounts using unpacking

**Context:**  
Jordan needs to print out the amounts (in pounds) for the standard mix. He will do with with unpacking.

`Example: x, y, z = my_tuple`

**Your Challenge:**  
Extract each of the four parts of the `standard_mix` tuple into variables with the appropriate names, then make a print statement that shows each substance name and the weight of it in pounds.

```python
cement, sand, gravel ,water = # ?????
# print statement goes here...
```

**Expected Output / Test It:**  

```console
*** Standard Mix ***
Cement: 400 lbs.
Sand: 800 lbs.
Gravel: 1200 lbs.
Water: 220.
********************
```

**Question 1:** How is unpacking a cleaner method for extracting values from a tuple?

**Question 2:** Why has Jordan chosen a tuple instead of a list or set for his mix ratios?

### Step 2: Extracting a value with a negative index.

**Context:**  

The way in which Jordan has written his code, negative indices make more sense. He wants to extract the sand amount (in pounds) using a negative index, regardless of the type of mix he is using.

**Your Challenge:**  

Write a one line Python print statement that will always print the sand amount of each mix (in pounds) using a negative index.

```python
# print statement goes here
# Hint: \n \t and string multipliers like '*'*5 might be useful.
```

**Expected Output / Test It:**  

```console
***** Sand Amounts *****
Standard Mix: 800 lbs.
High Strength: 750 lbs.
Light Duty: 900 lbs.
************************
```

**Question 3:** <Question>

**Question 4:** <Question>

*(Continue adding Step 3, Step 4, … as needed. Usually 3–5 total learning steps work best for the time limit.)*

### Step N: <Final Integration / Wrap-up Topic>

**Context:**  
<Explain how this step ties everything together.>

**Your Challenge:**  
<Instructions for the final activity.>

```python
# Final starter code template (if needed)
```

**Expected Output / Test It:**  
```
<Example output>
```

**Question X:** <Wrap-up thinking question.>

---

### Final Integration Code
Copy and run this block after you’ve completed Steps 1–N. It uses all the concepts and variables from the lab.

```python
# Final wrap-up code (provide a meaningful, complete block here)
# Add comments to help students understand how everything connects.
```

---

### Lab Reflection (Answer in your notebook)

1. <Copy Question 1 or first question here>
2. <Copy Question 2 here>
3. <Copy Question 3 here>
4. ...
   
*(List every Question that appeared in the lab so students have a clean checklist.)*

### Bonus Challenge (Extra Credit – 5–10 minutes)

**Context:**  
<Brief context.>

**Your Task:**  
<More advanced instructions that extend the main lab.>

---

You’re done!  
You just <short motivational summary of what they accomplished>.  

Save your file as `<lab_topic>_lab.py` and be ready to discuss your answers in class!

&copy; LogosTeach 2026 - All Rights Reserved. 
