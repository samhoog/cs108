"""CS 108 Lab 12.0

This module implements a simple line animation.

@author: Keith VanderLinden (kvlinden)
@date: Spring, 2020
@author: Sam Hoogewind (sth6)
@date: Fall, 2020
"""
from tkinter import Tk, Canvas, ALL


class LineAnimation:

    def __init__(self, window, width=250, height=250):
        """Construct the canvas GUI and prepare the first frame of the animation"""
        self.window = window

        self.screen_width = width
        self.screen_height = height
        self.canvas = Canvas(self.window, bg='#FFFFFF',
                             width=self.screen_width, height=self.screen_height)
        self.canvas.pack()

        # Start the animation with a horizontal line from the top left.
        self.x1 = 0
        self.y1 = 0
        self.x2 = self.screen_width
        self.y2 = 0

        # Schedule the first animation frame .
        self.window.after(0, self.step_animation)

    def step_animation(self):
        """Draw one animation frame and set up the next."""

        # Draw the line
        self.canvas.create_line(self.x1, self.y1, self.x2, self.y2, fill="#85A1C1")

        # Move the right coordinate down one pixel until it hits the corner.
        if self.y2 < self.screen_height:
            self.y2 += 1

        # Schedule the next animation frame.
        self.window.after(10, self.step_animation)


if __name__ == '__main__':
    root = Tk()
    root.title('Line Animation')
    app = LineAnimation(root)
    root.mainloop()
