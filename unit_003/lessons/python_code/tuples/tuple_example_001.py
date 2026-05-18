# Example of creating a tuple in Python
constants = (3.14, 2.718, 1.618)

# Example of indexing a tuple
print(constants[0])  # Output: 3.14
print(constants[1])  # Output: 2.718
print(constants[2])  # Output: 1.618
print(constants[-1])  # Output: 1.618 (negative indexing)

# Example of unpacking a tuple
pi, e, phi = constants
print(pi)  # Output: 3.14
print(e)  # Output: 2.718
print(phi)  # Output: 1.618

# Example of trying to modify a tuple (this will raise an error)

# constants[0] = 3.14159 # This will raise a TypeError.

# Checking the type
print(type(constants))  # Output: <class 'tuple'>

# Implicit tuple creation
point = 1, 2, 3
# comma separated values without parentheses creates a tuple

# Creating an empty tuple
empty_tuple = ()
print(empty_tuple)  # Output: ()

# Creating a single element tuple (note the comma)
single_element_tuple = (55,)
print(single_element_tuple)  # Output: (55,)

# Creating a tuple with the tuple() constructor
numbers = tuple([1, 2, 3, 4, 5])
print(numbers)  # Output: (1, 2, 3, 4, 5)

# Creating a tuple of characters from a string.
chars = tuple("Hello there!")
print(chars)  # Output: ('H', 'e', 'l', 'l', 'o', ' ', 't', 'h', 'e', 'r', 'e', '!')


"""
Copyright 2026 LogosTeach - All Rights Reserved
This software is the property of LogosTeach and is for educational purposes only. It may not be reproduced, distributed, or used for commercial purposes without express written permission from LogosTeach.
LogosTeach is not liable for any damages arising from the use of this software. By using this software, you agree to the terms and conditions outlined in this notice.
"""
