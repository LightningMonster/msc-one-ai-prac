"""
Q.3) Write a Python program to generate Calendar for the given month and year.
[20 Marks]
"""

import calendar

# Input month and year from user
year = int(input("Enter Year (e.g. 2025): "))
month = int(input("Enter Month (1-12): "))

# Display the calendar
print("\n📅 Calendar for", calendar.month_name[month], year)
print("----------------------------------")
print(calendar.month(year, month))
