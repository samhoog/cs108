"""CS 108 Lab 3.1

This application generates a student's login id.

@author: Sam Hoogewind (sth6)
@date: Fall, 2020
"""

# Store the first name as a string
first_name = input('First name: ')

# Store the last name as a string
last_name = input('Last name: ')

# Store the student id number as a string
id_num = input('Student ID: ')

# Compute the login id by taking the first letter of the first name,
# the last name and the first 2 numbers of the id number
login = str(first_name[0] + last_name + id_num[0] + id_num[1])

# Make the login id all lowercase
login = login.lower()

# Print the login id
print('User ID: ' + login)