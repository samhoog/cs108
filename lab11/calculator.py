"""CS 108 Lab 11.1

This module provides basic functionality for a calculator.

@author: Serita Nelesen (smb4)
@date: Fall, 2014
@author: Keith VanderLinden (kvlinden)
@date: Summer, 2015 - replaced JUnit tests with assert tests
@date: Spring, 2020 - ported to ZyLabs

@author: Sam Hoogewind (sth6)
@date: Fall, 2020
"""


class Calculator:

    def __init__(self):
        """ Initialize calculator memory to 0.
        This is only needed for the extra credit exercise.
        """
        self.memory = 0

    def calculate(self, operand1, operator, operand2):
        """ Perform the specified calculation. """

        operand1 = float(operand1)
        operand2 = float(operand2)

        if operator == '+':
            return operand1 + operand2
        elif operator == '-':
            return operand1 - operand2
        elif operator == '*':
            return operand1 * operand2
        elif operator == '/':
            return operand1 / operand2
        else:
            raise ValueError()


if __name__ == '__main__':

    # Use this (one) calculator to run all the tests.
    calc = Calculator()

    # These addition tests should run without raised exceptions.
    assert calc.calculate('0', '+', '1') == 1
    assert calc.calculate('-7', '+', '9') == 2
    assert calc.calculate('-4', '+', '-8') == -12
    assert calc.calculate('3', '+', '0') == 3
    assert calc.calculate('2.0', '+', '5.3') == 7.3

    # These subtraction tests should run without raised exceptions.
    assert calc.calculate('3', '-', '9') == -6
    assert calc.calculate('-4', '-', '-8') == 4
    assert calc.calculate('-7', '-', '9') == -16
    assert calc.calculate('3', '-', '0') == 3
    assert calc.calculate('2.0', '-', '5.3') == -3.3

    # These division tests should run without raised exceptions.
    assert calc.calculate('3', '/', '12') == 0.25
    assert calc.calculate('-4', '/', '-8') == 0.5
    assert calc.calculate('16', '/', '-8') == -2
    assert calc.calculate('0', '/', '3') == 0
    assert calc.calculate('-5.0', '/', '2') == -2.5

    # These multiplication tests should run without raised exceptions.
    assert calc.calculate('3', '*', '9') == 27
    assert calc.calculate('-4', '*', '-8') == 32
    assert calc.calculate('-7', '*', '9') == -63
    assert calc.calculate('3', '*', '0') == 0
    assert calc.calculate('2.0', '*', '5.3') == 10.6

    # Test the bad operator exception.
    try:
        calc.calculate('4', 'f', '9')
        # This should raise an exception.
        assert False
    except ValueError:
        assert True

    # Test the divide by zero exception.
    try:
        calc.calculate('5', '/', '0')
        # This should raise an exception.
        assert False
    except ZeroDivisionError:
        assert True

    # Test the bad operand exception
    try:
        calc.calculate('hi', '+', '9')
        # This should raise an exception.
        assert False
    except ValueError:
        assert True
        
    # If we get this far, the tests must have all passed.
    print('tests passed!')
