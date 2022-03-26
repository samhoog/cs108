"""CS 108 - Lab 8.0

This module implements a simple food item class with nutritional information.

@author: Sam Hoogewind (sth6)
@date: Fall, 2020
"""


class FoodItem:

    def __init__(self, name, fat, carbohydrates, protein):
        """Constructs a FoodItem instance with the given attributes"""
        self.name = name
        self.fat = fat
        self.carbohydrates = carbohydrates
        self.protein = protein

    def __str__(self):
        """Returns a printable representation of this food item"""
        return (
            self.name
            + "\n\tFat: {:.2f} g".format(self.fat)
            + "\n\tCarbohydrates: {:.2f} g".format(self.carbohydrates)
            + "\n\tProtein: {:.2f} g".format(self.protein)
        )

    def get_calories(self, num_servings):
        """Returns the number of calories for the given number of servings of
        this food item
        """
        return num_servings * (
            (self.fat * 9) + (self.carbohydrates * 4) + (self.protein * 4)
        )

# Instantiate a food item for M&Ms
MnMs = FoodItem('M&Ms', 10.0, 34.0, 2.0)
# Print the class object
print(MnMs)
# Print the calories per serving while getting 1 serving 
print("Calories per serving:", MnMs.get_calories(1))

# Print a blank line to seperate them
print()

# Instantiate a food item for water
water = FoodItem('Water', 0.0, 0.0, 0.0)
# Print the class object
print(water)
# Print the calories per serving while getting 10 servings
print("Calories per 10 servings:", water.get_calories(10))
