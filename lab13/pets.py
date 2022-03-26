"""CS 108 Lab 13.0

This module implements an pets hierarchy that includes dogs and cats.

@author: Keith VanderLinden (kvlinden)
@date: Summer, 2015
@author: Sam Hoogewind (sth6)
@date: Fall, 2020
"""


class Pet:
    """This class implements the base class from which all specific pet
    classes are derived.
    """

    def __init__(self, name='', genus=''):
        """Instantiates an pet object"""
        self.name = name
        self.genus = genus


class Dog(Pet):

    def __init__(self, name='', bites=True):
        """Instantiates an pet object"""
        Pet.__init__(self, name, 'canis')
        self.bites = bites

    def get_sound(self):
        """Returns the sound made by the dog"""
        return 'woof'
    
    def get_sound_meaning(self):
        """Returns what the sound the dog makes means"""
        return('Hello, I\'m a dog and my name is ' + str(self.name) + '.')


class Cat(Pet):

    def __init__(self, name='', lives=9):
        """Instantiates an pet object"""
        Pet.__init__(self, name, 'felis')
        self.lives = lives

    def get_sound(self):
        """Returns the sound made by the cat"""
        return 'meow'
    
    def get_sound_meaning(self):
        """Returns what the sound the cat makes means"""
        return("Hello, I\'m a cat and my name is " + str(self.name) +'.')

class Flea(Pet):

    def __init__(self, name=''):
        """Instantiates an pet object"""
        Pet.__init__(self, name, 'pulex')

    def get_sound(self):
        """Returns the sound made by the flea"""
        return 'zzz'
    
    def get_sound_meaning(self):
        """Returns what the sound the flea makes means"""
        return("Hello, I\'m a flea and my name is " + str(self.name) +'.')

if __name__ == '__main__':
    
    phydeaux = Dog(name='Phydeaux')
    assert phydeaux.genus == 'canis'
    assert phydeaux.get_sound() == 'woof'
    assert phydeaux.get_sound_meaning() == 'Hello, I\'m a dog and my name is Phydeaux.'

    # We should be able to name our dog anything we want.
    phred = Dog(name='Phred')
    assert phred.get_sound_meaning() == 'Hello, I\'m a dog and my name is Phred.'

    phelix= Cat(name='Phelix')
    assert phelix.genus == 'felis'
    assert phelix.get_sound() == 'meow'
    assert phelix.get_sound_meaning() == 'Hello, I\'m a cat and my name is Phelix.'

    phiphi = Flea(name='PhiPhi')
    assert phiphi.genus == 'pulex'
    assert phiphi.get_sound() == 'zzz'
    assert phiphi.get_sound_meaning() == 'Hello, I\'m a flea and my name is PhiPhi.'
