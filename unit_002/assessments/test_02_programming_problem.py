"""
Test 2 - Programming Problem
Author: LogosTeach - All Rights Reserved
This software is for educational purposes only and may not be redistributed for any
purpose without express written permission from LogosTeach
"""

weather_log = "Date: 2026-01-19\tTemp: 32.5F\tWind: 15mph\tNotes: Snowy day\n"

date = weather_log[6:16].strip() # Year / Month / Day format

# Extract year, month, and day from date
year = date[0:4]
month = date[5:7]
day = date[8:10]

# Assemble the date in reverse order
reversed_date = day + '-' + month + '-' + year

temp_f = float(weather_log[23:27].strip()) # Decimal format XX.X
temp_c = (temp_f - 32)/ 1.8

wind_speed = int(weather_log[35:37].strip()) # Integer Format

notes = weather_log[48:].strip('\n') # Brief description of the type of day

print(f"Reversed Date: {reversed_date}")
print(f"Temp in Celsius: {temp_c}")
print(f"Window Groups: 3 full groups of {wind_speed // 3} mph, remainder {wind_speed % 3} mph")
print(f"Clean Notes: {notes}")
