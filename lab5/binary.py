"""CS 108 Lab 5.1

This application takes a user given positive integer and prints it
in reversed-binary.

@author: Sam Hoogewind (sth6)
@date: Fall, 2020
"""

# Prompt the user for an integer
num = int(input("integer: "))

# Implement the algorithm with a while loop
while num > 0:
    print(num % 2, end='')
    num //= 2

# Print a newline
print()
