# Computer Lab

## Set Unions, Intersections, Differences, and Symmetric Differences

**Step 0:** Open a new Python file or notebook cell and run this code exactly as presented.

```python
# Define our two discipleship groups
group1 = {"John", "Sarah", "Mike", "Anna", "Tom"}
group2 = {"Sarah", "Mike", "Rachel", "James", "Tom"}

print("Group 1:", group1)
print("Group 2:", group2)
print("Number of people in Group 1:", len(group1))
print("Number of people in Group 2:", len(group2))
```

**Question 1:** How many total unique people are there across both groups? (Don't calculate it yet, just write down your guess.)

### Step 1: Union

Ministry context: You want to plan a big combined retreat. You need every unique person from either group (no duplicates).

**Your Challenge:**

Write code to create a new set called `combined` that contains **all unique** members of both groups.
Use **both** the (`|`) operator and the method (`.union()`) -- run them separately and confirm they give the same result.

```python
# Your code goes here (replace comments)

# combined = ...
# combined2 = ...

print("Combined retreat attendees:", combined)
print("Using .union():", combined2)
```

Run it, then answer

**Question 2:** How many people will attend the retreat?

**Question 3:** Which two people appear in both groups (you will use this later)?

### Step 2: Intersection

Ministry context: You need leaders who are common to both groups to establish a good connection between the groups.

**Your Challenge:**

Create a set called `common_ground` that contains members that are common to **both** groups. Use both the (`|`) operator and the method (`.intersection()`) to calculate the new set.

```python
# YOUR CODE HERE

# common_ground = ...
# common_ground2 = ...

print("Joint leaders (common ground):", common_ground)
print("Using .intersection():", common_ground2)
```

Run it, then answer

**Question 4:** Who seem to be the perfect candidates from your calculation?

**Question 5:** Why does intersection automatically remove duplicates?

### Step 3: Difference

Ministry context: You find out that you need to follow up with the members that are only in group 1. They may be feeling disconnected from group 2, so you may need to follow up personally.

**Your Challenge:**

Create a set called `only_group1` that contains members that only belong to group 1. Use both the (`-`) operator and the function (`.difference()`) to calculate this set. Then **do the same** for only group 2.

```python
# YOUR CODE HERE

# only_group1 = ...
# only_group1_again = ...
# only_group2 = ...
# only_group2_again = ...

print("Only in Group 1 (follow-up needed):", only_group1)
print("Using .difference():", only_group1_again)
print("Only in Group 2:", only_group2)
print("Using .difference():", only_group2_again)
```

Run it, then answer:

**Question 6:** Who needs personal encouragement to connect with the other group?

**Question 7:** What would happen if you calculated `group2 - group1` instead?

### Step 4: Symmetric Difference (Outreach Targets)

Ministry context: These are people who are in exactly one group. Great for targeted invitations so no one feels left out.

**Your Challenge:**

Create a set called `outreach_targets` using the symmetric difference.
Use both the operator (`^`) and the method (`.symmetric_difference()`).

```python
# YOUR CODE HERE

# outreach_targets = ...
# outreach_targets2 = ...

print("People in exactly one group (outreach targets):", outreach_targets)
print("Using .symmetric_difference():", outreach_targets2)
```

Run it, then answer

**Question 8:** How many people are in exactly one group?

**Question 9:** Why is this different from the union?

### Step 5: Full Ministry Script (Put It All Together)

Copy and run this final block after you’ve completed Steps 1–4. It uses all your variables.

```python
print("=== DISCIPLESHIP MINISTRY REPORT ===")
print("Combined retreat attendees:", combined)
print("Joint leaders (common ground):", common_ground)
print("Only in Group 1 (follow-up needed):", only_group1)
print("Only in Group 2:", only_group2)
print("Outreach targets (exactly one group):", outreach_targets)
print("\nTotal unique people:", len(combined))
```

### Lab Reflection (Answer in your notebook)

1. Which operation would you use to plan a combined event? Why?
2. Which operation helps you find shared leaders?
3. In your own ministry or small group, what real sets of people could you analyze with these tools?
4. What surprised you most about how Python handles duplicates automatically?

**Bonus Challenge (Extra Credit):**

Add a third group (group3) with 3 new names (including 1 overlap with group1). Then calculate `group1` | `group2` | `group3` and `(group1 & group2) - group3`. What does the result tell you about planning a three-group event?

You’re done!
You just turned raw name lists into actionable ministry insights using only four set operations.
Save your file as `set_operations_discipleship_lab.py` and be ready to discuss your answers in the future!

&copy; LogosTeach 2026 - All Rights Reserved