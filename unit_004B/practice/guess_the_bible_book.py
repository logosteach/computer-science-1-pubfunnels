import random

print("🎉 Welcome to GUESS THE BIBLE BOOK! 🎉")
print("I'll think of a book of the Bible. You have 6 guesses!\n")

books = [
    "Genesis",
    "Exodus",
    "Psalms",
    "Proverbs",
    "Matthew",
    "John",
    "Acts",
    "Romans",
    "Revelation",
]
secret_book = random.choice(books).lower()

guesses = 0
max_guesses = 6

while True:
    guess = input("Guess a book of the Bible: ").strip().lower()
    guesses += 1

    if guess == secret_book:
        print(f"🎉 Amazing! You got it in {guesses} guesses!")
        print(f"The book was: {secret_book.title()}")
        break

    if guesses >= max_guesses:
        print(f"😔 Out of guesses! The book was: {secret_book.title()}")
        break

    if guess < secret_book:
        print("📖 Hint: Try a book that comes later in the Bible.")
    else:
        print("📖 Hint: Try a book that comes earlier in the Bible.")

print(
    "\nThanks for playing! Remember: 'Your word is a lamp to my feet...' - Psalm 119:105"
)
