# Slicing tuples
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(numbers[2:5])  # Output: (3, 4, 5)
print(numbers[:4])  # Output: (1, 2, 3, 4)
print(numbers[5:])  # Output: (6, 7, 8, 9, 10)
print(numbers[::2])  # Output: (1, 3, 5, 7, 9)
print(numbers[::-1])  # Output: (10, 9, 8, 7, 6, 5, 4, 3, 2, 1)

# Using min and max on tuples
print(min(numbers))  # Output: 1
print(max(numbers))  # Output: 10

# Using sorted() on a tuple returns a list
mixed_numbers = (5, 2, 9, 1, 5, 6)
sorted_numbers = sorted(mixed_numbers)
type(mixed_numbers)  # Output: <class 'tuple'>
print(mixed_numbers)  # Output: (5, 2, 9, 1, 5, 6)
type(sorted_numbers)  # Output: <class 'list'>
print(sorted_numbers)  # Output: [1, 2, 5, 5, 6, 9]

# Use tuple() to convert the list back to a tuple.
sorted_tuple = tuple(sorted_numbers)

# Calculating the length of a tuple
print(len(numbers))  # Output: 10

"""
Copyright 2026 LogosTeach - All Rights Reserved
This software is the property of LogosTeach and is for educational purposes only. It may not be reproduced, distributed, or used for commercial purposes without express written permission from LogosTeach.
LogosTeach is not liable for any damages arising from the use of this software. By using this software, you agree to the terms and conditions outlined in this notice.
"""
