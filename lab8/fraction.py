"""CS 108 Lab 8.1

This application stores fractions in a class and preforms various operations
with them.

@author: Sam Hoogewind (sth6)
@date: Fall, 2020
"""

import sys


def compute_gcd(alpha, beta):
    """ Computes and returns the greatest common divisor of two integers
    using Euclid's algorithm.
    """
    alpha = abs(alpha)
    beta = abs(beta)
    remainder = alpha % beta
    while remainder != 0:
        alpha = beta
        beta = remainder
        remainder = alpha % beta
    return beta


class Fraction():
    """This class keeps track of fraction's numerators and denominators.
    A fraction cannot be divided by 0, so that is an invariant"""
    
    def __init__(self, numerator=0, denominator=1):
        """Set the variables numerator and denominator to whatever the user
        passes, with 0/1 being the default. If invariant, print an error"""
        if denominator != 0:
            self.numerator = numerator
            self.denominator = denominator
            self.simplify()
        else:
            print('Unable to create invalid fraction', file=sys.stderr)
            sys.exit()
    
    def __str__(self):
        """Returns a pretty version of the fraction in the form x/y"""
        return(str(self.numerator) + "/" + str(self.denominator))
    
    def simplify(self):
        """Simplies the fraction using the GCF function"""
        gcd = compute_gcd(self.numerator, self.denominator)
        if gcd != 0:
            self.numerator = self.numerator // gcd
            self.denominator = self.denominator // gcd
        if self.denominator < 0:
            self.numerator = self.numerator * -1
            self.denominator = self.denominator * -1
    
    def __mul__(self, other):
        """Multiplies two fractions together and returns the simplified answer"""
        return Fraction(self.numerator * other.numerator,
                        self.denominator * other.denominator)
        