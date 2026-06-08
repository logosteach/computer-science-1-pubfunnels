print("🙏 21-DAY PRAYER CHALLENGE 🙏")
print("You will pray for a different focus each day!\n")

# Using range(start, stop, step)
# Important: The end value is EXCLUSIVE (off-by-one behavior)
for day in range(1, 22, 3):  # Try changing 22 to 21 and see what happens!
    if day == 1:
        print(f"Day {day}: Pray for your family")
    elif day == 4:
        print(f"Day {day}: Pray for your church")
    elif day == 7:
        print(f"Day {day}: Pray for your school")
    elif day == 10:
        print(f"Day {day}: Pray for your nation")
    elif day == 13:
        print(f"Day {day}: Pray for the elderly")
    elif day == 16:
        print(f"Day {day}: Pray for children in need")
    elif day == 19:
        print(f"Day {day}: Pray for missionaries")
    else:
        print(f"Day {day}: Pray for whatever the Lord puts on your heart")

print("\nGreat job! You completed your prayer challenge.")
