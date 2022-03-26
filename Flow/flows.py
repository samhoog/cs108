"""CS 108 - Final Project

This application creates the dots of each color.

@author: Sam Hoogewind (sth6)
@date: Fall, 2020
"""

class Flow:
    """Creates the head and tail dots of each low"""
    
    def __init__(self, color, flow_number, width, height, canvas, grid_size):
         
        # Instigate lots of variables for later use
        self.color = color
        self.flow_number = flow_number
        self.screen_width = width
        self.screen_height = height
        self.canvas = canvas
        self.head_column = ""
        self.head_row = ""
        self.tail_column = ""
        self.tail_row = ""
        self.grid_size = grid_size
        self.started = False
        self.ended = False
        
        # Make the dots the right size
        self.width_increment = self.screen_width / self.grid_size
        self.height_increment = self.screen_height / self.grid_size
        self.radius = self.width_increment * 0.3
        self.center_x = self.width_increment / 2
        self.center_y = self.height_increment / 2
        
        # Calculate where to center each dot
        self.head_center_x = self.center_x + (self.width_increment * self.flow_number)
        self.head_center_y = self.center_y
        self.tail_center_x = self.center_x + (self.width_increment * self.flow_number)
        self.tail_center_y = self.center_y + (self.height_increment * 4)

    def head_dot(self):
        """Create the head dot"""

        self.canvas.create_oval(self.head_center_x - self.radius,
                                self.head_center_y - self.radius,
                                self.head_center_x + self.radius,
                                self.head_center_y + self.radius,
                                fill=self.color,
                                outline=""
                                )

    def tail_dot(self):
        """Create the tail dot"""
        
        self.canvas.create_oval(self.tail_center_x - self.radius,
                                self.tail_center_y - self.radius,
                                self.tail_center_x + self.radius,
                                self.tail_center_y + self.radius,
                                fill=self.color,
                                outline=""
                                )

        

