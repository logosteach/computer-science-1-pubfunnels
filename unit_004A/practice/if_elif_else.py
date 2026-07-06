# =====================================================
# Python with a Worldview - Conditional Decisions Practice
# Lesson: if, elif, and else Statements
# =====================================================

print("=== Faith Decisions Practice Lab ===\n")

# Step 1: Basic if statement
# Objective: Write if statements correctly with proper : and indentation
age = int(input("Enter your age: "))

if age >= 18:
    print("You are old enough to make important decisions.")
# Add your own if statement below for a different condition


# Step 2: Multi-way decisions with elif and else
# Objective: Create multi-way decision structures
print("\n--- Life Path Choice ---")
path = input("Choose a path (God's way / own way / compromise): ").strip()

if path == "God's way":
    print("Blessed is the one who walks in obedience to the Lord. (Joshua 24:15)")
elif path == "own way":
    print("There are consequences when we go our own way.")
else:
    print("Compromise leads to instability. Choose clearly!")
# Test with different inputs to see program flow


# Step 3: Practical control of program flow
# Objective: Control flow based on conditions
print("\n--- Ministry Faithfulness Score ---")
score = int(input("Enter faithfulness score (0-100): "))

if score >= 90:
    result = "Excellent faithfulness - well done!"
elif score >= 70:
    result = "Good - keep growing in Christ!"
elif score >= 50:
    result = "Room to grow - choose God's way more fully."
else:
    result = "Time for a clear decision - choose life! (Deut 30:19)"

print("Result:", result)


# Final Integration & Reflection
print("\n=== Reflection ===")
print("How do if-elif-else statements mirror the choices we make in life?")
print("Remember: Clear code requires clear decisions, just as clear faith does.")
# Add your own comments or additional code here to experiment


# Bonus Challenge (uncomment and complete):
# nested_decision = True
# if nested_decision:
#     if score > 80 and path == "God's way":
#         print("Strong in both choice and action!")
