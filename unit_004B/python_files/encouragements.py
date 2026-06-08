import random

print("🙏 Welcome to the Bible Encouragement Machine! 🙏")
print("Keep typing 'next' to get encouragement. Type 'quit' to stop.\n")

verses = [
    "I can do all things through Christ who strengthens me. - Philippians 4:13",
    "The Lord is my shepherd, I shall not want. - Psalm 23:1",
    "Be strong and courageous. - Joshua 1:9",
    "Cast all your anxiety on Him because He cares for you. - 1 Peter 5:7",
    "This is the day that the Lord has made; let us rejoice and be glad in it. - Psalm 118:24",
]

user_input = ""

while user_input.lower() != "quit":
    verse = random.choice(verses)
    print(f"✨ Encouragement for you: ✨")
    print(verse)
    print("-" * 50)

    user_input = input("Type 'next' for another verse or 'quit' to stop: ").strip()

print("\nGod bless you! Go serve Him with joy today! ✝️")

""" 
This file is for educational purposes only.
"""
