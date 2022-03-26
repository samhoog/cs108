"""CS 108 Lab 6.2

This application takes a list of strings and returns the longest string in the list.

@author: Sam Hoogewind (sth6)
@date: Fall, 2020
"""

def find_longest(string_list):
    """Finds the longest string in a list of strings"""
    # Set a very short base longest word and accumulator
    longest = ''
    i = 0
    # Write a loop that compares the length of every word with the longest word,
    # and if the length is larger make that word the new length.
    for elements in string_list:
        if len(string_list[i]) > len(longest):
            longest = string_list[i]
        # Incriment the accumlator
        i += 1
    # Return the word with the longest length
    return longest
