"""CS 108 Lab 6.1

This application searches for a target in a list of elements, and
returns the position of the first occurance of that target. If the
target isn't in the list, it returns -1.

@author: Sam Hoogewind (sth6)
@date: Fall, 2020
"""

def search(str_list, target):
    """Returns the index of a target word, returns -1 if not found"""
#Implement the given algorithm
    i = 0
    for element in str_list:
        if str_list[i] == target:
            return i
        i += 1
    return -1
