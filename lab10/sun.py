"""CS 108 - Lab 10

This class models a sun.

@author: Serita Nelesen (smn4)
@date: Fall, 2014
@author: Chris Wieringa (cwieri39)
@date: Fall, 2020
@author: Sam Hoogewind(sth6)
@date: Fall, 2020
"""


class Sun:
    """Invariant: Radius can't be negative, and temperature can't be less than absolute 0."""

    def __init__(self, name, radius, temperature, color='yellow'):
        if radius <= 0:
            raise ValueError('Sun radius must be positive')
        if temperature <= -273.15:
            raise ValueError('Sun temperature must be greater than absolute zero')
        self.name = name
        self.radius = radius
        self.temp = temperature
        self.color = color

    def __str__(self):
        return self.name

    def render(self, canvas):
        # Fixup coloring code here.
        color = self.color

        # Draw the planet as a filled circle.
        x = 0
        y = int(canvas.cget('height')) // 2
        canvas.create_oval(
            x - self.radius, y - self.radius,
            x + self.radius, y + self.radius,
            fill=color)
    