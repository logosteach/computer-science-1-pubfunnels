# Simulate a large list of church members
church_members_list = ["person_" + str(i) for i in range(5000)] + ["John_Doe", "Mary_Smith"]
church_members_set = set(church_members_list)   # Convert to set once

import time

# Slow way — using a list
start = time.time()
for _ in range(10_000):
    "John_Doe" in church_members_list          # slow on big lists
list_time = time.time() - start

# Fast way — using a set
start = time.time()
for _ in range(10_000):
    "John_Doe" in church_members_set           # very fast
set_time = time.time() - start

print(f"List check took: {list_time:.4f} seconds")
print(f"Set check took:  {set_time:.4f} seconds")
print(f"Sets are about {list_time/set_time:.1f}x faster!")

"""
# Output
List check took: 0.1795 seconds
Set check took:  0.0002 seconds
Sets are about 1100.5x faster!
"""
# File name: performance_benefits_of_sets_membership_testing.py
