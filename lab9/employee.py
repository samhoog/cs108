"""CS 108 Lab 9

This class models an employee.

@author: Sam Hoogewind (sth6)
@date: Fall, 2020
"""


class Employee:
    """ Represents an employee object.
    Invariant:
    - Salary is an integer.
    """

    def __init__(self, first='John', last='Doe', rank='Staff', salary=10000):
        """Instantiate a new employee object, defaulting to a basic John Doe."""
        self.first = first
        self.last = last
        self.rank = rank
        self.salary = salary

    def __str__(self):
        """Create a employee string with a simple format."""
        return self.last + ', ' + self.first + ': ' + self.rank + ' ($' + str(self.salary) + ')'


# Run some tests.
if __name__ == "__main__":
    print(str(Employee()) == 'Doe, John: Staff ($10000)')
    print(str(Employee('Jane', 'Doe', 'Czar', 99999)) == 'Doe, Jane: Czar ($99999)')
