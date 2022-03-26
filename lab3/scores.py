"""CS 108 Lab 3.3

This application assigns and edits scores with names using a dictionary.

@author: Sam Hoogewind (sth6)
@date: Fall, 2020
"""

# Create a dictionary with the given values
score_dict = {'Joe': 10, 'Tom': 23, 'Barb': 13, 'Sue': 19, 'Sally': 12}

# Print Barb's score
print(str(score_dict['Barb']))

# Update Sally's score
score_dict['Sally'] = 13

# Delete Tom and his score
del score_dict['Tom']

# Print the final dictionary
print(score_dict)