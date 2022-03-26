"""CS 108 - Homework 3

This application displays a list of integers as a bar graph.

@author: Sam Hoogewind (sth6)
@date: Fall, 2020
"""

import tkinter
import random

# Set your list of integers
data = 0
numbers = []
while True:
    data = int(input("integer (negative number to quit): "))
    if len(numbers) == 0 and data < 0:
        print("Please enter at least one value.")
    elif data > 0:
        numbers.append(data)
    else:
        break
    
# Set up the canvas.
window = tkinter.Tk()
canvas = tkinter.Canvas(window, width=500, height=500, background='white')
canvas.pack()

test = [3, 5, 8, 2, 9, 12, 15, 4]

def draw_bar_graph(data, canvas=canvas, total_width=500, total_height=500):
    """Draw the bar graph using the list of integers"""
    i = 0
    for num in data:
        # Draw a bar for each piece of data:
        # x0 calculates the width of the bar and increments each one
        # y0 will always be the bottom most point on the canvas
        # height takes the highest value and divides by the total height
        # of the canvas to come up with a scale factor, which it multiplies
        # the value by
        # width is the total width divided by the number of bars
        # color uses the random_color function to pick a random color
        # increment the accumulator 
        draw_bar(x0 = 500/len(data) * i,
                 y0 = 500,
                 height = 500 - num * (500/max(data)),
                 width = 500 / len(data),
                 color = random_color())
        i += 1


def random_color():
    """Return a random color HEX code"""
    return random.choice(['#FFADAD', '#FFD6A5', '#FDFFB6', '#CAFFBF',
                          '#9BF6FF', '#A0C4FF', '#BDB2FF', '#FFC6FF'])

def draw_bar(x0, y0, height, width, color, canvas=canvas,):
    """Draw a bar given the starting coords, height, width and color"""
    # Draw a rectangle with the top left point being the given x0 and
    # height, and the bottom right point being the given x0 plus the
    # width and the bottom of the canvas, filling with the random color
    canvas.create_rectangle(x0, height, x0 + width, 500, fill=color)

# Call the function using the test list of values
draw_bar_graph(numbers)