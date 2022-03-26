"""CS 108 Lab 6.3

This application returns all the unique words in a list of strings.

@author: Sam Hoogewind (sth6)
@date: Fall, 2020
"""

#Take the search function from a previous lab
def search(str_list, target):
    """Returns the index of a target word, returns -1 if not found"""
    i = 0
    for element in str_list:
        if str_list[i] == target:
            return i
        i += 1
    return -1

def count_unique_words(str_list):
    """Return all the unique words in a list of strings"""
    #Implement the given algorithm
    unique_words = []
    for word in str_list:
        if (search(unique_words, word) == -1):
            unique_words.append(word)
    return unique_words
