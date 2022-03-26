"""CS 108 - Lab 1.2

This application has a turtle draw a star.

@author: Sam Hoogewind (sth6)
@date: Fall, 2020
"""

import turtle

# Start the turtle window in the corner of the screen (helpful for dual monitor).
# turtle.setup(width=800, height=600, startx=100, starty=100)

window = turtle.Screen()
pen = turtle.Turtle()

# Have the turtle go straight and turn right 5 times

pen.forward(250)
pen.right(144)
pen.forward(250)
pen.right(144)
pen.forward(250)
pen.right(144)
pen.forward(250)
pen.right(144)
pen.forward(250)

#window.exitonclick()
