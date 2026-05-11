# Example 3: Common List Methods + Best Practices
# Theme: Growing in Christ (Discipleship steps)

steps = ["Pray daily", "Read the Bible", "Serve others", "Share the Gospel"]

print("Original steps:", steps)

# Add one new step
steps.append("Give thanks")
print("\nAfter append:", steps)

# Add multiple steps
steps.extend(["Worship", "Memorize verses"])
print("After extend:", steps)

# Insert at the beginning
steps.insert(0, "Start with Jesus")
print("After insert:", steps)

# Remove an item
steps.remove("Worship")
print("After remove:", steps)

# Sort the list
steps.sort()
print("After sort:", steps)

# Best Practices:
# - Use clear names: growth_steps = []
# - Use list comprehension for simple changes
upper_steps = [step.upper() for step in ["pray", "read", "serve"]]
print("\nUppercase steps:", upper_steps)

# Takeaway: Keep your lists simple and purposeful,
# just as we seek to grow steadily in our walk with Christ.
