# Dictionaries Lab Solutions
# Author: John C. Partridge with LogosTeach

christ_our_peace = {
    "Ephesians 2:14": "For he himself is our peace, who has made the two groups one and has destroyed the barrier, the dividing wall of hostility.",
    "John 14:27": "Peace I leave with you; my peace I give you. I do not give to you as the world gives. Do not let your hearts be troubled and do not be afraid.",
    "Philippians 4:7": "And the peace of God, which transcends all understanding, will guard your hearts and your minds in Christ Jesus.",
    "Colossians 1:20": "And through him to reconcile to himself all things... by making peace through his blood, shed on the cross.",
    "Isaiah 9:6": "For to us a child is born... and he will be called Wonderful Counselor, Mighty God, Everlasting Father, Prince of Peace.",
    "Romans 5:1": "Therefore, since we have been justified through faith, we have peace with God through our Lord Jesus Christ.",
}

# Part 1
print("#" * 10, "Part 1", "#" * 10)
key = "Ephesians 2:14"
print(f"{key} says, {christ_our_peace[key]}")

"""
Question 1: The difference between a list and a dictionary is that a list is an
ordered sequence of values. Where-as a dictionary is an unordered group,
or comma-separated group of key-value pairs.
"""
print("#" * 20, "\n\n")

# Part 2
print("#" * 10, "Part 2", "#" * 10)
key = "John 14:27"
print(f"{key} says, {christ_our_peace[key]}")
print(f"{'Phillipians 4:6'} says, {christ_our_peace.get('Phillipians 4:6', \
'Verse not found.')}")

"""
Question 2: If you use [] square brackets and a key does not exist then you
get a KeyError.
"""
print("#" * 20, "\n\n")

# Part 3A
print("#" * 10, "Part 3A", "#" * 10)
for ref in christ_our_peace:
    print(ref)
print("#" * 20, "\n\n")

# Part 3B
print("#" * 10, "Part 3B", "#" * 10)
for ref, verse in christ_our_peace.items():
    print(f"{ref}: {verse}")

"""
Question 3: When you need both the key and the value then the .items() method
is the best method to use.
"""
print("#" * 20, "\n\n")

# Part 4
print("#" * 10, "Part 3A", "#" * 10)
new_verses = {
    "2 Thessalonians 3:16": "Now may the Lord of peace himself give you peace at all times and in every way. The Lord be with all of you.",
    "John 16:33": "I have told you these things, so that in me you may have peace. In this world you will have trouble. But take heart! I have overcome the world.",
}

# merge the two dictionaries together into our first dictionary
christ_our_peace.update(new_verses)
print("#" * 20, "\n\n")

# add a nested dictionary for the Ephesians 2:14 key.
christ_our_peace["Ephesians 2:14"] = {
    "text": "For He Himself is our peace...",
    "theme": "Unity and Reconciliation",
    "key_word": "barrier",
}

for ref, verse in christ_our_peace.items():
    print(f"{ref}:{verse}")

print("Updated count: ", len(christ_our_peace))

"""
Question 4: When you have a duplicate key when using .update() the old value
for that key is replaced with the new value/values.

Lab Reflection (Answer in your notebook)
1. What is one advantage of using a dictionary over a list?
A dictionary has an advantage over a list in that each value is given an associated
name or key. This makes searching through a dictionary very fast. Dictionaries also
provide more structure in organizing data than lists do.

2. What error can occur with square bracket access, and how do you prevent it?
If you use square brackets [] to find the value of a key that does not exist
then you will get a KeyError.

To prevent this, you can use the .get() method. You can also customize a response
if that particular key does not exist in the dictionary. If a key does not exist
in the dictionary then the .get() method returns the None data type.

3. Why is  .items()  often the most useful when looping?
.items() allows us to loop through all the contents of the dictionary, each
key with its associated value.

4. What happens when  .update()  finds a duplicate key?
If you find a duplicate key with the .update() method then the old value is replaced
with the new value. No error is thrown.

5. How did nesting help organize more complex data?
If you have a set of data that requires more structure, like a computer's file system
 where you have multiple folders, subfolders and files in each then a dictionary is the
 right data structure for you!
"""

# Final Integration

for ref, data in christ_our_peace.items():
    if isinstance(data, dict):  # nested case
        print(f"\n{ref}")
        print(f"   {data['text']}")
        print(f"   Theme: {data['theme']}")
    else:
        print(f"\n{ref}")
        print(f"   {data}")
        print(f"\nTotal verses stored: {len(christ_our_peace)}")
        print("Christ Himself is our peace! 🕊")

# -------------------------------------------------------
# Copyright 2026 LogosTeach - All Rights Reserved
# This software is for educational purposes only.
# It is not intended for commercial use or distribution.
# -------------------------------------------------------
