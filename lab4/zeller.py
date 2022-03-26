"""CS 108 Lab 4.2

This application calculates the day of the week of a date the user inputs.

@author: Sam Hoogewind (sth6)
@date: Fall, 2020
"""

# Prompt the user for a day, month and year and store them as integers
year = int(input('Enter year: '))
month = int(input('Enter month: '))
day = int(input('Enter day: '))

# Convert January and February to 13 and 14 and subtract the year by 1
if month == 1:
    month = 13
    year -= 1
if month == 2:
    month = 14
    year -= 1

# Calculate h (the day of the week) using the formula
h = (day + ((month + 1) * 26 // 10) + year % 100 + (year % 100) // 4 +\
    (year // 100) // 4 + 5 * (year // 100)) % 7

# Create a list of the days of the week
week = [
    'Saturday', 'Sunday', 'Monday', 'Tuesday',
    'Wednesday', 'Thursday', 'Friday'
    ]

# Print the day of the week using the index of days
print(week[h])
