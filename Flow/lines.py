"""CS 108 - Final Project

This application creates the lines where you click and release.

@author: Sam Hoogewind (sth6)
@date: Fall, 2020
"""

class Line():
    
    def __init__(self, width, height, starting_column, starting_row, ending_column, ending_row, color, canvas, grid_size):
        
        # Instigate a lot of variables for later use
        self.sc = starting_column
        self.sr = starting_row
        self.ec = ending_column
        self.er = ending_row
        self.color = color
        self.screen_width = width
        self.screen_height = height
        self.canvas = canvas
        self.grid_size = grid_size
        
        self.width_increment = self.screen_width / self.grid_size
        self.height_increment = self.screen_height / self.grid_size
        self.center_x = self.width_increment / 2
        self.center_y = self.height_increment / 2
        
        # Calculate where to draw the line depending on the starting and ending point
        self.x1 = self.sc * self.width_increment - self.center_x
        self.y1 = self.sr * self.height_increment - self.center_y
        self.x2 = self.ec * self.width_increment - self.center_x
        self.y2 = self.er * self.width_increment - self.center_y
        
        self.create_line(x1=self.x1, y1=self.y1, x2=self.x2, y2=self.y2, color=self.color)
    
    def create_line(self, x1, y1, x2, y2, color):
        
        # Draw the line and dots at either end to make for smooth looking corners
        self.canvas.create_line(x1, y1, x2, y2, fill=color, width=(self.width_increment * 0.35))
        
        self.canvas.create_oval(x2 - (self.width_increment * 0.17),
                                y2 - (self.height_increment * 0.17),
                                x2 + (self.width_increment * 0.17),
                                y2 + (self.height_increment * 0.17),
                                fill=self.color,
                                outline=''
                                )
        
        self.canvas.create_oval(x1 - (self.width_increment * 0.17),
                                y1 - (self.height_increment * 0.17),
                                x1 + (self.width_increment * 0.17),
                                y1 + (self.height_increment * 0.17),
                                fill=self.color,
                                outline=''
                                )
        