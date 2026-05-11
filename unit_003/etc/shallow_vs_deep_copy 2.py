# Simple Program: Understanding Shallow vs Deep Copy using id()
# Perfect for beginners learning about list copying

import copy

print("=== Shallow vs Deep Copy Demonstration ===\n")

# Original list with a nested list inside (this is key to see the difference)
original = ["John 3:16", "Psalm 23:1", ["Pray daily", "Read Bible"]]

print("Original list:", original)
print("Memory address of original list:", id(original))
print("Memory address of inner list:", id(original[2]))
print("-" * 60)

# Create a shallow copy
shallow = original.copy()

print("Shallow copy created with .copy()")
print("Memory address of shallow list:", id(shallow))
print("Memory address of inner list in shallow:", id(shallow[2]))

print("\nNotice: The outer lists have DIFFERENT addresses,")
print("but the inner list has the SAME address!")
print("This means they share the same inner list object.\n")
print("-" * 60)

# Create a deep copy
deep = copy.deepcopy(original)

print("Deep copy created with copy.deepcopy()")
print("Memory address of deep list:   ", id(deep))
print("Memory address of inner list in deep:", id(deep[2]))

print("\nNotice: Both the outer list AND the inner list have")
print("completely DIFFERENT memory addresses.")
print("This means everything is copied independently.\n")
print("-" * 60)

# Now let's make a change to demonstrate the real difference
print("Making a change to the shallow copy...")
shallow[2].append("Give thanks")   # Modifying the inner list

print("\nAfter adding 'Give thanks' to shallow copy's inner list:")

print("Original list now:", original)
print("Shallow copy:     ", shallow)
print("Deep copy:        ", deep)

print("\n" + "="*60)
print("KEY TAKEAWAY:")
print("• shallow copy (.copy()) shares inner mutable objects")
print("• deep copy (copy.deepcopy()) creates fully independent copies")
print("• Always use deepcopy() when you want completely separate lists,")
print("  especially when sharing data between different groups or people.")
print("="*60)
