"""CS 108 - Homework 1

This application uses a turtle to draw the French Flag at a user given scale.

@author: Sam Hoogewind (sth6)
@date: Fall, 2020
"""

import turtle

# Start the turtle window in the corner of the screen (helpful for dual monitor).
# turtle.setup(width=800, height=600, startx=100, starty=100)

window = turtle.Screen()
pen = turtle.Turtle()
turtle.hideturtle()

# Have the user input a unit size
UNIT = int(input("Please enter a unit size: "))

# Draw the blue section
turtle.color("#0055A4")
turtle.begin_fill()
turtle.left(90)
turtle.forward(UNIT * 2)
turtle.left(90)
turtle.forward(UNIT)
turtle.left(90)
turtle.forward(UNIT*2)
turtle.left(90)
turtle.forward(UNIT)
turtle.end_fill()

# Bridge the gap
turtle.color('black')
turtle.forward(UNIT)

# Draw the red section
turtle.color("#EF4135")
turtle.begin_fill()
turtle.left(90)
turtle.forward(UNIT * 2)
turtle.right(90)
turtle.forward(UNIT)
turtle.right(90)
turtle.forward(UNIT * 2)
turtle.right(90)
turtle.forward(UNIT)
turtle.end_fill()

# Draw the last line
turtle.right(90)
turtle.forward(UNIT * 2)
turtle.color('black')
turtle.left(90)
turtle.forward(UNIT)

#window.exitonclick()
