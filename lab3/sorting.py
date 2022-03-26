"""CS 108 Lab 3.2

This application sorts four user given numbers from smallest to largest.

@author: Sam Hoogewind (sth6)
@date: Fall, 2020
"""

# Prompt the user for each number and assign it to a list
number = [float(input('number: ')), float(input('number: ')),\
          float(input('number: ')), float(input('number: '))]

# Assign each number to a variable, assigning the smallest number then
# deleting it from the list, and repeating
num1 = min(number)
number.remove(num1)
num2 = min(number)
number.remove(num2)
num3 = min(number)
number.remove(num3)
num4 = min(number)

# Create a sorted list
sort_number = [num1, num2, num3, num4]

# Print the sorted list
print(sort_number)