"""CS 108 - Homework 6

This application uses the Scribble class to make an animation of random lines.

@author: Sam Hoogewind (sth6)
@date: Fall, 2020
"""

from tkinter import Tk, Canvas, ALL, Button, Frame
from scribble import Scribble

class ScribbleAnimation:

    def __init__(self, window, width=500, height=500):
        """Construct the canvas GUI and prepare the first frame of the animation"""
        self.window = window
        self.screen_width = width
        self.screen_height = height
        self.canvas = Canvas(self.window, bg='#FFFFFF',
                             width=self.screen_width, height=self.screen_height)
        self.canvas.pack()
        
        # Create a Scribble object
        self.scribble = Scribble()
        
        # Create a frame for the buttons
        frame = Frame(root, width=self.screen_width, height=40)
        frame.pack(side="bottom")
        
        # Create a quit button
        self.quit_button = Button(frame, text="Quit", command=quit)
        self.quit_button.pack(side="right")
        
        # Create a clear button
        self.clear_button = Button(frame, text="Clear", command=self.clear)
        self.clear_button.pack(side="left")

        # Bind the mouse click
        self.canvas.bind('<Button-1>', self.mouse_clicked)

        # Schedule the first animation frame .
        self.window.after(0, self.step_animation)

    def clear(self):
        """Clear the canvas"""
        self.canvas.delete("all")
    
    def step_animation(self):
        """Draw one animation frame and set up the next."""
        # Start the animation
        Scribble.draw_line(self.scribble, self.canvas)
        
        # Schedule the next animation frame.
        self.window.after(50, self.step_animation)
    
    def mouse_clicked(self, event):
        """Reset and move the application when the mouse is clicked"""
        # Set the new starting points to where was clicked
        self.scribble.x = event.x
        self.scribble.y = event.y
        
        # Create a new random color
        self.scribble.color = Scribble.get_random_color(self.scribble)

# Test
if __name__ == '__main__':
    root = Tk()
    root.title('Scribble Animation')
    app = ScribbleAnimation(root)
    root.mainloop()
