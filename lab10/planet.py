"""CS 108 - Lab 10

This class models a planet.

@author: Serita Nelesen (smn4)
@date: Fall, 2014
@author: Chris Wieringa (cwieri39)
@date: Fall, 2020
@author: Sam Hoogewind (sth6)
@date: Fall, 2020
"""


class Planet:
    """Invariant: The radius and distance can't be negative"""
    
    def __init__(self, name, radius, distance, color='black'):
        if (radius <= 0) or (distance <= 0):
            raise ValueError('Planet numeric properites must be positive')
        self.name = name
        self.radius = radius
        self.distance = distance
        self.color = color

    def __str__(self):
        return self.name

    def render(self, canvas):
        # Fixup positioning and coloring code here.
        x = self.distance
        color = self.color

        # Draw the planet as a filled circle.
        y = int(canvas.cget('height')) // 2
        canvas.create_oval(
            x - self.radius, y - self.radius,
            x + self.radius, y + self.radius,
            fill=color)
        