# Real ministry data
sunday_attendees = ["Alice", "Bob", "Charlie", "Alice", "David"]
wed_bible_study = ["Bob", "Eve", "Frank"]
prayer_requests = ["heal grandma", "job for Mike", "heal grandma", "church growth", "guidance for missions"]
spiritual_gifts = ["teaching", "prophecy", "serving", "teaching", "healing", "mercy"]

# 1. Unique people across events
unique_attendees = set(sunday_attendees) | set(wed_bible_study)

# 2. Unique prayer topics (case-insensitive)
unique_prayers = {req.lower().strip() for req in prayer_requests}

# 3. Unique spiritual gifts in the church
unique_gifts = set(spiritual_gifts)

# 4. Immutable core leadership gifts
core_leadership_gifts = frozenset(["teaching", "leadership", "pastoral"])

print("Unique attendees this week:", unique_attendees)
print("Unique prayer topics:", unique_prayers)
print("Spiritual gifts present:", unique_gifts)
print("Core leadership gifts (locked):", core_leadership_gifts)
