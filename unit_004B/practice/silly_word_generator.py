"""
In the terminal window, you may have to install the requests library if you have not already done this, the type:

pip install requests

in the terminal window.
"""

import requests

print("Welcome to the Silly Word Generator!")
print("This program uses a free API to get fun, clean words.\n")

while True:
    user_input = input("Would you like another silly word? (yes/no): ").strip().lower()

    if user_input in ["no", "n", "quit", "q"]:
        print("Goodbye! Thanks for playing with silly words. 🚀")
        break
    elif user_input in ["yes", "y"]:
        try:
            # Free random word API (no API key needed)
            response = requests.get(
                "https://random-word-api.herokuapp.com/word?number=1"
            )

            if response.status_code == 200:
                silly_word = response.json()[0]
                print(f"\n🎉 Your silly word is: **{silly_word}** 🎉\n")
            else:
                print("Oops! Couldn't fetch a word right now. Try again later.")
        except Exception:
            print("Something went wrong with the connection. Check your internet!")
    else:
        print("Please type 'yes' or 'no'.\n")
