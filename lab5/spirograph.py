"""CS 108 - Lab 5.2

This application uses Tkinter to draw a spirograph with user
read radii, pen offset and color.

@author: Sam Hoogewind (sth6)
@date: Fall, 2020
"""

import tkinter
import math

# Start the tkinter window, naming it "Tkinter Canvas".  Create a tkinter canvas
# with an initial size of 500 pixels by 500 pixels on a white background.
# Call the pack function to add the canvas to our window.
window = tkinter.Tk()
window.title("Tkinter Canvas")
canvas = tkinter.Canvas(window, width=500, height=500, background='white')
canvas.pack()

# Prompt the user for all the input values and assign them to variables
moving_radius = float(input("moving radius: "))
fixed_radius = float(input("fixed radius: "))
pen_offset = float(input("pen offset: "))
color = input("color: ")

# Set the center to half the canvas width
center = 250

# Set x and y to the appropriate positions using the equations
x = fixed_radius + moving_radius + pen_offset + center
y = 0.0 + center

# Create variable t = 0 as a base point
t = 0.0

# Create loop that will draw spirograph
while t < 360:
# Increment t
    t += 0.1
# Calculate next x and y values using the given equations
    next_x = (fixed_radius + moving_radius) * math.cos(t) + pen_offset * \
             math.cos(((fixed_radius + moving_radius) * t) / moving_radius) + center
    next_y = (fixed_radius + moving_radius) * math.sin(t) + pen_offset * \
             math.sin(((fixed_radius + moving_radius) * t) / moving_radius) + center
# Draw a line in the user given color
    canvas.create_line(x, y, next_x, next_y, fill=color)
# Assign x and y to the newly calculated values 
    x = next_x
    y = next_y

# window.mainloop() # Needed for some IDEs.
