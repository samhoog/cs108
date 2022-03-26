"""CS 108 - Lab 3.4

This application uses Tkinter Canvas to draw a scalable stick figure.

@author: Sam Hoogewind (sth6)
@date: Fall, 2020
"""

import tkinter

# Start the tkinter window, naming it "Tkinter Canvas".  Create a tkinter canvas
# with an initial size of 500 pixels by 500 pixels on a white background.
# Call the pack function to add the canvas to our window.
window = tkinter.Tk()
window.title("Tkinter Canvas")
canvas = tkinter.Canvas(window, width=500, height=500, background='white')
canvas.pack()

UNIT = 50

# Draw the head
canvas.create_oval(
    1 * UNIT, 2 * UNIT, # bounding box x1, y1
    3 * UNIT, 4 * UNIT, # bounding box x2, y2
    outline="blue"
)

# Draw the body
canvas.create_line(
    2 * UNIT, 4 * UNIT, # x1, y1
    2 * UNIT, 6 * UNIT, # x2, y2
    fill='red'
)

# Draw the arms
canvas.create_line(
    1 * UNIT, 5 * UNIT, # x1, y1
    3 * UNIT, 5 * UNIT, # x2, y2
    fill='black'
)

# Draw the left leg
canvas.create_line(
    1 * UNIT, 7 * UNIT, # x1, y1
    2 * UNIT, 6 * UNIT, # x2, y2
    fill='black'
)

# Draw the right leg
canvas.create_line(
    3 * UNIT, 7 * UNIT, # x1, y1
    2 * UNIT, 6 * UNIT, # x2, y2
    fill='black'
)
# window.mainloop() # Needed for some IDEs.
