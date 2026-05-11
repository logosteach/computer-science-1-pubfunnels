# Nested list representing the generations of the patriarchs
# Outer list: Major patriarchs
# Inner lists: Their key descendants or attributes

patriarchal_line = [
    ["Abraham", 175, ["Isaac"]],                                    # Genesis 25:7
    ["Isaac", 180, ["Jacob", "Esau"]],                              # Genesis 35:28
    ["Jacob", 147, ["Reuben", "Simeon", "Levi", "Judah", 
                    "Dan", "Naphtali", "Gad", "Asher", 
                    "Issachar", "Zebulun", "Joseph", "Benjamin"]]   # Genesis 47:28
]

print("God's faithful generations - Nested like the layers of His promises:\n")

for generation in patriarchal_line:
    name = generation[0]
    age = generation[1]
    descendants = generation[2]
    print(f"• {name} lived {age} years and fathered: {', '.join(descendants)}")
    
print("\nJust as these nested generations carried God's covenant forward,")
print("all God's promises find their 'Yes' in Christ Jesus! (2 Corinthians 1:20)")

"""
# Output

God's faithful generations - Nested like the layers of His promises:

• Abraham lived 175 years and fathered: Isaac
• Isaac lived 180 years and fathered: Jacob, Esau
• Jacob lived 147 years and fathered: Reuben, Simeon, Levi, Judah, Dan, Naphtali, Gad, Asher, Issachar, Zebulun, Joseph, Benjamin

Just as these nested generations carried God's covenant forward,
all God's promises find their 'Yes' in Christ Jesus! (2 Corinthians 1:20)

"""
