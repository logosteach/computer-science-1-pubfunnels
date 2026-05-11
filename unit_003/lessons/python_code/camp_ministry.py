# BIBLE CAMP SMALL GROUP PLANNER
# Mini Project - Python Dictionaries

print("$ BIBLE CAMP SMALL GROUP PLANNER")
print("=" * 50)
print("I'm getting ready to lead my small group at Bible camp!\n")

# ======================
# STEP 1: Create the dictionary
# ======================
print("STEP 1: Creating my small group dictionary...")

small_group = {
    "Emma": "Age 9 - Loves the story of David and Goliath",
    "Noah": "Age 10 - Wants to learn about Jesus calming the storm",
    "Lily": "Age 8 - Favorite verse is John 3:16",
    "Jackson": "Age 11 - Has questions about the Trinity",
}

print(f"✅ Started with {len(small_group)} kids in my group.\n")

# ======================
# STEP 2: Add new kids
# ======================
print("STEP 2: Adding two new kids who just signed up...")

small_group["Sophia"] = "Age 9 - Loves singing worship songs"
small_group["Mason"] = "Age 10 - Wants to hear about the Good Samaritan"

print("✅ Added Sophia and Mason!")
print(f"   Now we have {len(small_group)} kids.\n")

# ======================
# STEP 3: Remove a kid
# ======================
print("STEP 3: Removing Jackson (he got moved to the older boys cabin)...")

del small_group["Jackson"]

print("✅ Removed Jackson.")
print(f"   Final group size: {len(small_group)} kids.\n")

# ======================
# STEP 4: Print nicely formatted output
# ======================
print("STEP 4: Here's my final small group roster!\n")

print("--- NAMES ONLY (keys) ---")
for name in small_group.keys():
    print(f"• {name}")

print("\n--- FULL DETAILS (using .items()) ---")
for name, info in small_group.items():
    print(f"👦 {name}")
    print(f"   {info}")
    print()

# ======================
# BONUS: Prayer List
# ======================
print("BONUS: My quick prayer list for the group:")
for name in small_group:
    print(f"🙏 Pray for {name} this week!")
