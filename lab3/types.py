"""CS 108 Lab 3.0

This application assigns different user given values to their appropriate
data structure.

@author: Sam Hoogewind (sth6)
@date: Fall, 2020
"""

# Store the scores in a list
scores = [int(input('score: ')), int(input('score: '))]

# Store the password in a string
password = input('password: ')

# Store the dorm coordinates in a tuple
dorm = (float(input('latitude: ')), float(input('longitude: ')))

# Store the capitals and states in a dictionary
state_capitals = {input('state: '): input('capital: '), \
                  input('state: '): input('capital: ')}
