print("🙏 21-DAY PRAYER CHALLENGE - COUNTDOWN EDITION 🙏")
print("We're counting down the days until the end of our prayer challenge!\n")

# Reverse range: range(start, stop, step) with negative step
for day in range(21, 0, -1):  # Starts at 21, stops before 0, counts down by 1
    if day == 21:
        print(f"Day {day}: Pray for your own heart and walk with God")
    elif day == 14:
        print(f"Day {day}: Pray for your family")
    elif day == 7:
        print(f"Day {day}: Pray for your church")
    elif day == 3:
        print(f"Day {day}: Pray for boldness to share the Gospel")
    elif day == 1:
        print(f"Day {day}: Pray with thanksgiving for all God has done!")
    else:
        print(f"Day {day}: Keep pressing on in prayer!")

print("\n🎉 Challenge Complete! God is faithful!")
print("‘Pray without ceasing’ — 1 Thessalonians 5:17")
