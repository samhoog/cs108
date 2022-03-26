"""CS 108 Lab 10.0

Run some try-except examples.

@author: Sam Hoogewind (sth6)
@date: Fall, 2020
"""

try:
    import happiness
    assert False  # this statement should never run
except ImportError as ie:
    print("There is no happiness module in Python:", ie)

# Add the other exceptions tests here.
except TypeError as te:
    print("Error:", te)
except ZeroDivisionError as zde:
    print("Error:", zde)
except AttributeError as ae:
    print("Error:", ae)
except IndexError as ine:
    print("Error:", ine)
except NameError as ne:
    print("Error:", ne)
except FileNotFoundError as fnfe:
    print("Error:", fnfe)

# Try out the exception handling for the name class.

from name import Name

# Instantiating a default name object should give us 'Clifford'.
default_name = Name()
assert str(default_name) == "Clifford"

# Instantiating an empty name object should raise a ValueError.
try:
    Name('')
    Name('Keith')
    assert False, "This line should never be reached because trying to construct an empty name should raise a ValueError."
except ValueError:
    assert True

# Instantiating a Keith name object should raise a ValueError.
try:
    Name('Keith')
    assert False, "This line should never be reached because trying to construct an empty name should raise a ValueError."
except ValueError:
    assert True