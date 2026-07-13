# Biblical XOR Illustration - Gospel of Jesus Christ
#
# Learning Objective:
# - Understand XOR as an exclusive condition using the truth of the Gospel.
# - Practice converting user input to boolean and using it in logical expressions.

"""
Ligonier Ministries: Faith Alone
https://learn.ligonier.org/devotionals/faith-alone
"""

# Get user input and convert to boolean
user_input = (
    input("Do you place faith in Christ alone for salvation? (yes/no): ")
    .strip()
    .lower()
)
faith_in_christ_alone = user_input in ["yes", "y", "true", "1"]

all_have_sinned = True
trusting_own_works = False

# XOR: Exactly one valid path - faith in Christ alone
salvation_by_grace = faith_in_christ_alone != trusting_own_works

print("\nAll have sinned:", all_have_sinned)
print("Trusting in own works:", trusting_own_works)
print("Faith in Christ alone (your input):", faith_in_christ_alone)
print("Salvation by grace through faith (XOR):", salvation_by_grace)

if salvation_by_grace:
    print("Result: Justified by God's grace - the exclusive Gospel path.")
else:
    print("Result: No access apart from Christ.")

# Alternative using ^
print("Bitwise XOR result:", (faith_in_christ_alone ^ trusting_own_works))

# End of Practice File
# Copyright 2026 LogosTeach - All Rights Reserved
