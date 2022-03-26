"""CS 108 Lab 2.1

This application calculates Albert Einstein's number puzzle.

@author: Sam Hoogewind (sth6)
@date: Fall, 2020
"""

# Have the user input a number and assign it to a variable
number = int(input())

# Assign the 3 digits to variables
digit1 = number // 100
digit2 = (number // 10) % 10
digit3 = number % 10

# Reverse the numbers and assign it to a variable
rev_number = (digit3 * 100) + (digit2 * 10) + digit1

# Calculate the difference
difference = abs(number - rev_number)

# Assign the 3 digits to variables
digit1 = difference // 100
digit2 = (difference // 10) % 10
digit3 = difference % 10

# Reverse the numbers and assign it to a variable
rev_diff = (digit3 * 100) + (digit2 * 10) + digit1

# Print final sum
print("Number: " + str(difference + rev_diff))
