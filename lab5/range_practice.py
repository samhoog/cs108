"""CS 108 Lab 5.0

This application takes two user input integers and prints increments
of 10 from the first integer until the value is less than or equal
to the second integer.

@author: Sam Hoogewind (sth6)
@date: Fall, 2020
"""

# Prompt the user for 2 integers
num1 = int(input())
num2 = int(input())

# Print every increment of 10 in the range of the first integer
# to the second
if num1 <= num2:
    for x in range(num1, num2 + 1, 10):
        print(x)

# If the second integer is bigger, print an error
else:
    print("Second integer can't be less than the first.")
    