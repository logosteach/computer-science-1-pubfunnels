# Example 2: Shallow vs Deep Copy
# Theme: Sharing favorite Bible verses with friends

import copy

# Original list of favorite verses
favorites = [
    ["John 3:16", "God loves us"],
    ["Psalm 23:1", "The Lord is my shepherd"],
    ["Philippians 4:13", "I can do all things"]
]

# Make two copies
group_a = favorites.copy()          # shallow copy
group_b = copy.deepcopy(favorites)  # deep copy

# Group A adds a personal note to the first verse
group_a[0].append(" - My favorite!")

print("=== Original list ===")
for item in favorites:
    print(item)

print("\n=== Group A (shallow copy) ===")
for item in group_a:
    print(item)

print("\n=== Group B (deep copy) ===")
for item in group_b:
    print(item)

# Takeaway: Use deepcopy() when sharing so one person's notes 
# don't change another person's list. Each walk with Jesus is unique!

"""
# Output

=== Original list ===
['John 3:16', 'God loves us', ' - My favorite!']
['Psalm 23:1', 'The Lord is my shepherd']
['Philippians 4:13', 'I can do all things']

=== Group A (shallow copy) ===
['John 3:16', 'God loves us', ' - My favorite!']
['Psalm 23:1', 'The Lord is my shepherd']
['Philippians 4:13', 'I can do all things']

=== Group B (deep copy) ===
['John 3:16', 'God loves us']
['Psalm 23:1', 'The Lord is my shepherd']
['Philippians 4:13', 'I can do all things']
"""
