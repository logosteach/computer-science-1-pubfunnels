# Example: Processing a list of prayer requests, skipping empty ones
prayer_requests = [
    "Heal my mom",
    "",
    "Help with school",
    " ",
    "Strength for my dad",
    "",
]

for request in prayer_requests:
    request = request.strip()  # clean whitespace
    if request == "":  # skip empty requests
        continue  # go to the next iteration
    print("Praying for:", request)
