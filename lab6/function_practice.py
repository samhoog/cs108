"""CS 108 Lab 6.0

This application calculates the gasoline cost of a road trip with
user given miles, miles per gallon and dollars per gallon, as
well as counting the number of spaces in a user given string.

@author: Sam Hoogewind (sth6)
@date: Fall, 2020
"""

def compute_cost(miles, miles_per_gallon, dollars_per_gallon):
    """Calculates gasoline cost of a road trip"""
    cost = (miles / miles_per_gallon) * dollars_per_gallon
    return cost

def count_spaces(string):
    """Calculates number of spaces in a string"""
    spaces = 0
    for letter in string:
        if letter == ' ':
            spaces += 1
    return spaces
