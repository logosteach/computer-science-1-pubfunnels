"""
Learning how to sort a list using keys.
This Python file is for educational purposes only.
© LogosTeach 2026 - All Rights Reserved
"""

# List of the biblical patriarchs with their God-given lifespans (Genesis)
patriarchs = [
    {"name": "Abraham", "age": 175, "verse": "Genesis 25:7"},
    {"name": "Isaac",   "age": 180, "verse": "Genesis 35:28"},
    {"name": "Jacob",   "age": 147, "verse": "Genesis 47:28"}
]

print("The Patriarchs - Lifespans according to Scripture:\n")

# 1. Original order
print("Original order:")
for p in patriarchs:
    print(f"• {p['name']} lived to {p['age']} years ({p['verse']})")

# 2. Sort by age (youngest to oldest) using key=
sorted_by_age = sorted(patriarchs, key=lambda p: p["age"])

print("\nSorted by age (youngest to oldest):")
for p in sorted_by_age:
    print(f"• {p['name']} lived to {p['age']} years ({p['verse']})")

# 3. Sort by age descending (oldest to youngest) with reverse=True
sorted_by_age_desc = sorted(patriarchs, key=lambda p: p["age"], reverse=True)

print("\nSorted by age (oldest to youngest):")
for p in sorted_by_age_desc:
    print(f"• {p['name']} lived to {p['age']} years ({p['verse']})")
