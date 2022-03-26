"""CS 108 Lab 10.0

Run some try-except examples.

@author: Sam Hoogewind (sth6)
@date: Fall, 2020
"""


class Name:
    """This class models a simple name
    Invariant:
    - The name can't be blank.
    - The name can't be Keith.
    """

    def __init__(self, name="Clifford"):
        if name == '':
            raise ValueError("The name can't be blank.")
        if name == 'Keith':
            raise ValueError("Your name can't be Keith.")
        self.name = name

    def __str__(self):
        return self.name
