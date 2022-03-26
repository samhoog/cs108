"""CS 108 - Homework 5

This application prompts the user for values and uses bar_graph.py to draw the graph.

@author: Sam Hoogewind (sth6)
@date: Fall, 2020
"""

from bar_graph import BarGraph

try:
    # Prompt the user for the filename with the data
    filename = input("Filename: ")
    
    # Open the file to read the data
    file = open(filename, "r")
    
    # Split the lines into a list
    data = file.read().splitlines()

    # Make the first line the color and remove it from the list
    color = data[0]
    del data[0]

    # Make each line an integer
    for i in range(0, len(data)): 
        data[i] = int(data[i])
    
    # Draw the graph
    user_graph = BarGraph(data, color)
    user_graph.draw(500, 500)

# Handle Exceptions
except FileNotFoundError as fnfe:
    print("Error:", fnfe)
    quit()
except ValueError as ve:
    print("Error:", ve)
    quit()
