"""CS 108 - Homework 5

This application displays a list of integers as a bar graph using a class.

@author: Sam Hoogewind (sth6)
@date: Fall, 2020
"""

import tkinter
import random
import sys

# Set up the canvas.
window = tkinter.Tk()
canvas = tkinter.Canvas(window, width=500, height=500, background='white')

class BarGraph():
    """Draws a bar graph and prints a summary"""
    def __init__(self, data, color='random'):
        """Initialize values for the data, color, and variables to be used later"""
        self.data = data
        self.color = color
        self.color_list = ['#FFADAD', '#FFD6A5', '#FDFFB6', '#CAFFBF','#9BF6FF',
                        '#A0C4FF', '#BDB2FF','#FFC6FF']
        self.i = 0
        self.temp_color = ''
        self.canvas = 0
        for num in self.data:
            if num < 0: 
                # If there is a negative value, print an error and close the system
                print("You cannot have a negative value", file=sys.stderr)
                sys.exit()
        if self.data == []:
            # If the list is empty, print an error and close the system
            print("You cannot have an empty data list", file=sys.stderr)
            sys.exit()

    def __str__(self):
        """Return a string printing the color and list of data"""
        return("Bar Graph - Color: " + self.color + " Data: " + str(self.data))
    
    def draw(self, canvas=canvas, total_width=500, total_height=500):
        """Draw the bar graph using the list of integers"""
        # Create and pack a canvas with the user given width and height
        self.canvas = tkinter.Canvas(window, width=total_width,
                                height=total_height, background='white')
        self.canvas.pack()
        i = 0
        for num in self.data:
            # Draw a bar for each piece of data:
            # x calculates the width of the bar and increments each one.
            # y will always be the bottom most point on the canvas.
            # height takes the highest value and divides by the total height
            # of the canvas to come up with a scale factor, which it multiplies
            # the value by.
            # width is the total width divided by the number of bars.
            # increment the accumulator 
            self.draw_bar(canvas = self.canvas,
                     x = total_width/len(self.data) * i,
                     y = total_height,
                     height = total_height - num * (total_height/max(self.data)),
                     width = total_width / len(self.data),
                     )
            i += 1

    def get_color(self):
        """Return the color of the bar being drawn"""
        # If the color is set as random return a random choice, otherwise
        # return the selected color
        if self.color == 'random':
            # Choose a random color, setting it to a temp variable. Then remove
            # that color from the list of colors. Set the temp variable to a global
            # one, then incriment i so after the second color is chosen the global
            # color is readded to the list, and the cycle repeats, so you can never
            # have the same color twice in a row.
            temp_color = random.choice(self.color_list)
            self.color_list.remove(temp_color)
            if self.i != 0:
                self.color_list.append(self.temp_color)
            self.i += 1
            self.temp_color = temp_color
            return temp_color
        else:
            return self.color

    def draw_bar(self, canvas, x, y, width, height):
        """Draw a bar given the starting coords, height, width and color"""
        # Draw a rectangle with the top left point being the given x0 and
        # height, and the bottom right point being the given x0 plus the
        # width and the bottom of the canvas, filling with the selected color
        self.canvas.create_rectangle(x, height, x + width,
                                y, fill=self.get_color())

if __name__ == "__main__":
    bg = BarGraph([3, 5, 8, 2, 9, 12, 15, 4], 'random')
    print(bg)                      
bg.draw(canvas, 500, 500)