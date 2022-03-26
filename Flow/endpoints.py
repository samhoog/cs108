"""CS 108 - Final Project

This application defines a class for Endpoints so you can interact with where you let go.

@author: Sam Hoogewind (sth6)
@date: Fall, 2020
"""

class Endpoint():
    
    def __init__(self, color, column=0, row=0):
        """Store variables so the program knows where you can click and which color the line should be"""
        
        self.column = column
        self.row = row
        self.color = color
