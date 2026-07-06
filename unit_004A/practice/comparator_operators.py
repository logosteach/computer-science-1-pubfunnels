"""
In this practice, you will learn how to use comparison operators in Python. Comparison operators are used to compare two values and return a boolean value (True or False) based on the comparison.
"""

name = "Mike"
age = 23
height = 6.1  # feet
weight = 180  # pounds

if name == "Mike":
    print("Hello Mike!")

elif name != "Mike":
    print("You are not Mike.")

print(age > 18)  # True
print(height < 7)  # True
print(weight >= 150)  # True
print(weight <= 200)  # True
print(age == 23)  # True
print(name != "John")  # True
print(name == "Mike" and age > 18)  # True

# Copyright (c) 2026 LogosTeach - All Rights Reserved.
