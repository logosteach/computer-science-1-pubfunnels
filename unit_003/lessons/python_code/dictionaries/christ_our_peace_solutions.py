# =============================================
# CHRIST OUR PEACE - Dictionary Looping Challenge
# =============================================

christ_our_peace = {
    "Ephesians 2:14": "For he himself is our peace, who has made the two groups one and has destroyed the barrier, the dividing wall of hostility.",
    "John 14:27": "Peace I leave with you; my peace I give you. I do not give to you as the world gives. Do not let your hearts be troubled and do not be afraid.",
    "Philippians 4:7": "And the peace of God, which transcends all understanding, will guard your hearts and your minds in Christ Jesus.",
    "Colossians 1:20": "And through him to reconcile to himself all things... by making peace through his blood, shed on the cross.",
    "Isaiah 9:6": "For to us a child is born... and he will be called Wonderful Counselor, Mighty God, Everlasting Father, Prince of Peace.",
    "Romans 5:1": "Therefore, since we have been justified through faith, we have peace with God through our Lord Jesus Christ.",
}

print("$ CHRIST OUR PEACE")
print("=" * 50)
print("Let's explore what the Bible says about Christ as our peace.\n")

# ======================
# TASKS FOR STUDENTS
# ======================

print("TASK 1: Loop through the dictionary and print only the references (keys)")
print("-" * 60)

# Students should write code here:
for reference in christ_our_peace:
    print(reference)

print("\nTASK 2: Loop through and print the full verses (values only)")
print("-" * 60)

# Students should write code here:
for verse in christ_our_peace.values():
    print(verse)
    print()

print("\nTASK 3: Loop through and print both reference + verse (BEST way)")
print("-" * 60)

# Students should write code here:
for reference, verse in christ_our_peace.items():
    print(f"{reference}:")
    print(f"   {verse}")
    print()

# ======================
# BONUS CHALLENGE
# ======================

print("BONUS CHALLENGE:")
print("Print only the verses that contain the word 'peace' (case insensitive)")

for ref, verse in christ_our_peace.items():
    if "peace" in verse.lower():
        print(f"✓ {ref}")

# Copyright 2026 LogosTeach - All Rights Reserved.
"""
This software is for educational purposes only. It is not intended for commercial use or distribution.
"""
