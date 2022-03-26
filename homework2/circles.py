"""CS 108 - Homework 2

This application prompts the user to enter center coordinates and
radii of two circles, then determines if they are overlapping, disjoint,
or inside of each other, and prints the result to the canvas and the shell.

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

# Prompt the user to enter the center coordinates and radii of two circles
# and store all the variables
x1 = float(input('Circle 1 x: '))
y1 = float(input('Circle 1 y: '))
r1 = float(input('Circle 1 radius: '))
x2 = float(input('Circle 2 x: '))
y2 = float(input('Circle 2 y: '))
r2 = float(input('Circle 2 radius: '))

# Draw both circles
canvas.create_oval(x1 - r1, y1 - r1, x1 + r1, y1 + r1)
canvas.create_oval(x2 - r2, y2 - r2, x2 + r2, y2 + r2)

# Calculate the distance between the centers
d = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Create variables for the different possible text outcomes
disjoint = 'The circles are disjoint.'
overlap = 'The circles overlap.'
c1 = 'Circle 1 contains circle 2.'
c2 = 'Circle 2 contains circle 1.'

# Print the text on the canvas and output
# depending on if the circles overlap, contain one another or are disjoint
if (r1 == r2) and (d == 0): 
    canvas.create_text(250, 250, font = (20), text = overlap)
    print(overlap)
elif (r2 >= r1) and (d <= r2 - r1):
    canvas.create_text(250, 250, font = (20), text = c2)
    print(c2)
elif (r1 >= r2) and (d <= r1 - r2):
    canvas.create_text(250, 250, font = (20), text = c1)
    print(c1)
elif d <= (r1 + r2) or ((d == 0) and (r1 == r2)):
    canvas.create_text(250, 250, font = (20), text = overlap)
    print(overlap)
else:
    canvas.create_text(250, 250, font = (20), text = disjoint)
    print(disjoint)
 
# window.mainloop() # Needed for some IDEs.
