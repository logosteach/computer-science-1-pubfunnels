# Using the zip and enumerate functions with tuples
names = ("Andrew", "Bryce", "Cody", "Deena")
ages = (35, 23, 43, 23)

# Using zip to combine two tuples into a list of tuples
combined = zip(names, ages)
type(combined)  # Output: <class 'zip'>
print(
    list(combined)
)  # Output: [('Andrew', 35), ('Bryce', 23), ('Cody', 43), ('Deena', 23)]

# Using enumerate to get index and value from a tuple
for index, name in enumerate(names):
    print(f"Index: {index}, Name: {name}")
    # Output:
    # Index: 0, Name: Andrew
    # Index: 1, Name: Bryce
    # Index: 2, Name: Cody
    # Index: 3, Name: Deena

# Using zip and enumerate in a for loop together:
for index, (name, age) in enumerate(zip(names, ages)):
    print(f"Index: {index}, Name: {name}, Age: {age}")
    # Output:
    # Index: 0, Name: Andrew, Age: 35
    # Index: 1, Name: Bryce, Age: 23
    # Index: 2, Name: Cody, Age: 43
    # Index: 3, Name: Deena, Age: 23

"""
Copyright 2026 LogosTeach - All Rights Reserved
This software is the property of LogosTeach and is for educational purposes only. It may not be reproduced, distributed, or used for commercial purposes without express written permission from LogosTeach.
LogosTeach is not liable for any damages arising from the use of this software. By using this software, you agree to the terms and conditions outlined in this notice.
"""
