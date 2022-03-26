"""CS 108 - Final Project

This application runs Flow, a numberlink-like game where you have to connect all the dots.

@author: Sam Hoogewind (sth6)
@date: Fall, 2020
"""
from tkinter import Tk, Canvas, Button, Frame, PhotoImage, Toplevel, Label, StringVar
from flows import Flow
from grid import grid
from endpoints import Endpoint
from random import randint
from lines import Line

class FlowGame:
    """Run the game"""

    def __init__(self, window, width=650, height=650):
        """Start the GUI interface"""
        
        # Construct the canvas
        self.window = window
        self.screen_width = width
        self.screen_height = height
        self.canvas = Canvas(self.window, bg='#404040',
                             width=self.screen_width, height=self.screen_height)
        self.canvas.pack()
        
        # Instigate a bunch of variables for later use
        self.colors = ["red", "orange", "yellow", "green", "blue"]
        self.flows = []
        self.started_flows = []
        self.ended_flows = []
        self.lines = []
        self.endpoints = []
        self.grid_size = 5
        self.width_increment = self.screen_width / self.grid_size
        self.height_increment = self.screen_height / self.grid_size
        self.center_x = self.width_increment / 2
        self.center_y = self.height_increment / 2
        self.starting_column = 0
        self.starting_row = 0
        self.ending_column = 0
        self.ending_row = 0
        self.started_color = ""
        self.grid = grid
        self.i = 0
        self.j = 1
        self.k = 0
        self.l = 0
        self.m = 0
        self.doc_line = randint(0,19)
        self.text = StringVar()
        self.text.set("Complete Flows: 0")
        
        # Create the flows
        for i in range(0,5):
            flow = Flow(color=self.colors[i], flow_number=i, width=self.screen_width, height=self.screen_height, canvas=self.canvas, grid_size=self.grid_size)
            self.flows.append(flow)
            
        # Create the endpoints
        for i in range(0,5):
            endpoint = Endpoint(column=0, row=0, color=self.colors[i])
            self.endpoints.append(endpoint)
        
        # Create the board and and load the pattern and buttons
        self.create_board()
        self.load(self.doc_line)
        self.create_buttons()
        
        # Bind mouse controls
        self.canvas.bind('<ButtonPress-1>', self.click)
        self.canvas.bind('<ButtonRelease-1>', self.release)
        
    def reset(self):
        """Reset the board"""
        
        # Delete the board and clear lists
        self.canvas.delete("all")
        self.grid.update((k,"Empty") for k in self.grid)
        self.create_board()
        self.flows.clear()
        self.started_flows.clear()
        self.ended_flows.clear()
        self.endpoints.clear()
        self.text.set("Complete Flows: 0")
       
        # Reload all the flows 
        for i in range(0,5):
            flow = Flow(color=self.colors[i], flow_number=i, width=self.screen_width, height=self.screen_height, canvas=self.canvas, grid_size=self.grid_size)
            self.flows.append(flow)
        
        # Reset all the endpoints
        for i in range(0,5):
            endpoint = Endpoint(column=0, row=0, color=self.colors[i])
            self.endpoints.append(endpoint)
       
        # Reload the same board and clear the lists of flows and endpoints
        self.load(self.doc_line)
        
    def change_board_size(self):
        """Change the board size between 5x5 and 6x6"""
        
        # Clear the board and grid dictionary
        self.canvas.delete("all")
        self.grid.update((k,"Empty") for k in self.grid)
        
        # Algorithm for switching back and forth between grid sizes
        if self.j % 2 == 1:
            self.grid_size = 6
            self.j += 1
        elif self.j % 2 == 0:
            self.grid_size = 5
            self.j += 1
        
        # Reset variables depending on new grid size
        self.width_increment = self.screen_width / self.grid_size
        self.height_increment = self.screen_height / self.grid_size
        self.center_x = self.width_increment / 2
        self.center_y = self.height_increment / 2
        self.create_board()
        self.flows.clear()
        self.started_flows.clear()
        self.ended_flows.clear()
        self.endpoints.clear()
        self.text.set("Complete Flows: 0")
        
        # Reload all the flows
        for i in range(0,5):
            flow = Flow(color=self.colors[i], flow_number=i, width=self.screen_width, height=self.screen_height, canvas=self.canvas, grid_size=self.grid_size)
            self.flows.append(flow)
        
        # Reset all the endpoints
        for i in range(0,5):
            endpoint = Endpoint(column=0, row=0, color=self.colors[i])
            self.endpoints.append(endpoint)
        
        # Pick a new random board layout depending on what grid size is chosen
        # Lines 0 - 19 are 5x5 maps, lines 20 - 39 are 6x6 maps
        if self.grid_size == 5:
            self.doc_line = randint(0,19)
        elif self.grid_size == 6:
            self.doc_line = randint(20,39)
        self.load(self.doc_line)
        
    def change_theme(self):
        """Change the color of the dots"""
        
        # Incriment an accumulator
        self.i += 1
        
        # If you reach the end of the list, reset the accumulator
        if self.i == 5:
            self.i = 0
        
        # Define all the themes
        theme1 = ["red", "orange", "yellow", "green", "blue"]
        theme2 = ["#ef476f", "#ffd166", "#06d6a0", "#118ab2", "#073b4c"]
        theme3 = ["#70d6ff", "#ff70a6", "#ff9770", "#ffd670", "#e9ff70"]
        theme4 = ["#588b8b", "#ffffff", "#ffd5c2", "#f28f3b", "#c8553d"]
        theme5 = ["#e63946", "#f1faee", "#a8dadc", "#457b9d", "#1d3557"]
        theme_list = [theme1, theme2, theme3, theme4, theme5]
        
        # Cycle through the themes using the accumulator
        self.colors = theme_list[self.i]
        
        # Call the reset method, redrawing the board and flows but with the new colors
        self.reset()
        
    def winner_new_level(self):
        """Generate a new level"""
        
        # When you hit the new level on the winning window, also close the window
        self.new_level()
        self.root.destroy()
    
    def new_level(self):
        """Load a new random level"""
        
        # Delete and reset everything like in the reset method, but generate
        # a new random level instead of keeping the same one
        self.canvas.delete("all")
        self.grid.update((k,"Empty") for k in self.grid)
        self.create_board()
        self.flows.clear()
        self.started_flows.clear()
        self.ended_flows.clear()
        self.endpoints.clear()
        self.text.set("Complete Flows: 0")
        
        for i in range(0,5):
            flow = Flow(color=self.colors[i], flow_number=i, width=self.screen_width, height=self.screen_height, canvas=self.canvas, grid_size=self.grid_size)
            self.flows.append(flow)
        for i in range(0,5):
            endpoint = Endpoint(column=0, row=0, color=self.colors[i])
            self.endpoints.append(endpoint)
        if self.grid_size == 5:
            self.doc_line = randint(0,19)
        elif self.grid_size == 6:
            self.doc_line = randint(20,39)
        
        self.load(line=self.doc_line)
        
    def load(self, line):
        """Choose a random board pattern"""
        
        # Open a text document with all the dot placements
        boards = open("boards.txt")       
       
        # Initial accumlators 
        i = 0
        j = 0
       
        # Skip over the lines until you reach the randomly selected one
        while j != line:
            boards.readline()
            j += 1
        
        # Make a list of the values from the document
        values = boards.readline()
        lines = values.split()
        
        for f in self.flows:
            
            # Calculate the position of the head dot
            f.head_column = int(lines[i])
            f.head_center_x = f.head_column * self.width_increment - self.center_x
            
            f.head_row = int(lines[i+1])
            f.head_center_y = f.head_row * self.height_increment - self.center_y
            
            space = str(f.head_column) + str(f.head_row)
            
            # Mark on the grid the color of the head dot
            self.grid[int(space)] = f.color
            
            # Calculate the position of the tail dot
            f.tail_column = int(lines[i+2])
            f.tail_center_x = f.tail_column * self.width_increment - self.center_x
            
            f.tail_row = int(lines[i+3])
            f.tail_center_y = f.tail_row * self.height_increment - self.center_y
            
            end = str(f.tail_column) + str(f.tail_row)
            
            # Mark on the grid the color of the tail dot
            self.grid[int(end)] = f.color
            
            # Draw the dots
            f.head_dot()
            f.tail_dot()
            
            # Increment the accumulator
            i += 4
        
        # Close the file
        boards.close()

    def create_board(self): 
        """Create the board"""
        
        for i in range(0,self.grid_size): 
            # Create the rows
            self.canvas.create_line(self.width_increment * i,
                                    0,
                                    self.width_increment * i,
                                    self.screen_height,
                                    fill="#606060"
                                    #dash=(1,1)
                                    )
            
            # Create the columns
            self.canvas.create_line(0,
                                    self.height_increment * i,
                                    self.screen_height,
                                    self.height_increment * i,
                                    fill="#606060"
                                    #dash=(1,1)
                                    )
            
    def create_buttons(self):
        """Create the buttons"""
        
        # Create a quit button
        self.quit_button = Button(self.window, text="Quit", command=quit)
        self.quit_button.pack(side="right")
        
        # Create a reset button
        self.reset_button = Button(self.window, text="Reset", command=self.reset)
        self.reset_button.pack(side="right")
        
        # Create a new level button
        self.new_level_button = Button(self.window, text="New Level", command=self.new_level)
        self.new_level_button.pack(side="left")
        
        # Create a change theme button
        self.change_theme_button = Button(self.window, text="Change Theme", command=self.change_theme)
        self.change_theme_button.pack(side="left")
        
        # Create a change board size button
        self.change_board_size_button = Button(self.window, text="Change Board Size", command=self.change_board_size)
        self.change_board_size_button.pack(side="left")
        
        self.label = Label(self.window, textvariable=self.text)
        self.label.pack()
           
    def click(self, c):
        """Calculate what column and row you clicked in"""
        
        self.starting_column = (c.x // int(self.width_increment) + 1)
        self.starting_row = (c.y // int(self.height_increment) + 1)
        
    def release(self, l):
        """Record what column and row you let go in"""
        
        # Calculate what column and row you released in
        temp_column = (l.x // int(self.width_increment) + 1)
        temp_row = (l.y // int(self.height_increment) + 1)
        
        # If the column and row are valid, set global variables equal to them
        # If not, raise a ValueError
        if temp_column <= 0 or temp_column >= self.grid_size + 1:
            raise ValueError("Ending location out of bounds")
        else:
            self.ending_column = temp_column
           
        if temp_row <= 0 or temp_row >= self.grid_size + 1:
            raise ValueError("Ending location out of bounds")
        else:
            self.ending_row = temp_row
            
        # Run the drawing method
        self.draw() 

    def winner(self):
        """Open a window for the winning screen"""
        
        # Create a new canvas that opens on top of the main game
        self.root = Toplevel()
        self.root.title('Congrats!')
        
        # Add a frame, new level button and quit button
        frame = Frame(self.root, height=30)
        frame.pack(side="bottom")
        
        new_level_button = Button(frame, text="New Level", command=self.winner_new_level)
        new_level_button.pack(side="left")
        
        quit_button = Button(frame, text="Quit", command=quit)
        quit_button.pack(side="right")

        # Add a congratulatory image and winner text
        self.pic = PhotoImage(file = 'winner.png')
        self.label = Label(self.root, text='Winner!', bg="#ffffff", fg="red", image=self.pic, compound="top", font=("Gill Sans MT Condensed", "40"))
        self.label.pack()
        
        # Start the animation for the color changing text
        self.root.after(0, self.winner_text)
        self.root.mainloop()

    def winner_text(self):
        """Cycle through rainbow HEX color codes"""
        
        # Open a document of a bunch of HEX codes
        colors = open("colors.txt", "r")
        
        # If the accumulator isn't at the end of the list, keep going up by 1
        if self.m != 72:
            self.m += 1
        if self.m == 72:
            self.m = 0
        
        # Skip over however many lines the accumulator is at 
        for i in range(self.m):
            colors.readline()
        
        # Set the current color to whatever line you're at
        current_color = colors.readline()
        
        # Split the line to get rid of the newline character ('/n')
        current_color = current_color.split()
        colors.close()
        
        # Set the color of the text to whatever line you're on
        self.label['fg'] = current_color
        
        # Schedule the next frame of the animation
        self.root.after(100, self.winner_text)
        
    def draw(self):
        """See if the given moves are legal and create a line object if they are"""
        
        # Loop through all the flows
        for f in self.flows:
            
            # Check if starting column and row matches with a dot
            if ((self.starting_column == f.head_column) and (self.starting_row == f.head_row)) \
               or ((self.starting_column == f.tail_column) and (self.starting_row == f.tail_row)):
                
                # Check that the ending location is empty or the same color
                temp_location = str(self.ending_column) + str(self.ending_row)
                if self.grid[int(temp_location)] == "Empty" or self.grid[int(temp_location)] == f.color:
                    
                    # Check if the line is vertical
                    if (self.starting_column == self.ending_column) and \
                    (self.starting_row != self.ending_row):
                        a = self.starting_row
                        b = self.ending_row
                        c = 1
                        if self.ending_row < self.starting_row:
                            c = -1
                        t = 1
                        
                        # Calculate the range of rows you passed through
                        for i in range(a, b + c, c):
                            squares = str(self.starting_column) + str(i)
                            
                            # If all of the passed through squares are empty or the same color
                            # as the starting dot, continue
                            if self.grid[int(squares)] == "Empty" or self.grid[int(squares)] == f.color:
                                pass
                            
                            # If there is an illegal move, set a dummy variable to off
                            else:
                                t = -1
                                
                        # Only continue if the move is legal
                        if t == 1:
                            
                            # Create a line object
                            self.line = Line(starting_column=self.starting_column,
                                ending_column=self.ending_column,
                                starting_row=self.starting_row,
                                ending_row=self.ending_row,
                                color=f.color,
                                canvas=self.canvas,
                                grid_size=self.grid_size,
                                width=self.screen_width,
                                height=self.screen_height
                                )
                            self.lines.append(self.line)
                                
                            # Mark all the passed through squares on the grid with the
                            # corresponding color
                            for i in range(a, b + c, c):
                                square = str(self.starting_column) + str(i)
                                self.grid[int(square)] = f.color
                            
                            # Set variables for an Endpoint object so you will be able to draw from it
                            for endpoint in self.endpoints:
                                if endpoint.color == self.line.color:
                                    endpoint.column = self.ending_column
                                    endpoint.row = self.ending_row
                            
                            # Update the ending location with the dot color
                            self.grid[int(temp_location)] = f.color
                            
                            self.check_if_won()

                   # If the line isn't vertical, check if the line is horizontal and run the same tests as the horizontal   
                    elif (self.starting_row == self.ending_row) and \
                    (self.starting_column != self.ending_column):
                        a = self.starting_column
                        b = self.ending_column
                        c = 1
                        if self.ending_column < self.starting_column:
                            c = -1
                        t = 1
                        for i in range(a, b + c, c):
                            square = str(i) + str(self.starting_row)
                            if self.grid[int(square)] == "Empty" or self.grid[int(square)] == f.color:
                                pass
                            else:
                                t = -1
                            
                        if t == 1:    
                            self.line = Line(starting_column=self.starting_column,
                                ending_column=self.ending_column,
                                starting_row=self.starting_row,
                                ending_row=self.ending_row,
                                color=f.color,
                                canvas=self.canvas,
                                grid_size=self.grid_size,
                                width=self.screen_width,
                                height=self.screen_height
                                )
                            self.lines.append(self.line)
                                
                            # Mark all the passed through squares on the grid with the
                            # corresponding color
                            for i in range(a, b + c, c):
                                square = str(i) + str(self.starting_row)
                                self.grid[int(square)] = f.color
                            
                            # Set variables for an Endpoint object so you will be able to draw from it
                            for endpoint in self.endpoints:
                                if endpoint.color == self.line.color:
                                    endpoint.column = self.ending_column
                                    endpoint.row = self.ending_row
                            
                            # Update the ending location with the dot color
                            self.grid[int(temp_location)] = f.color
                            
                            
                            self.check_if_won()
                    # If the line isn't vertical or horizontal it must be diagonal
                    # which isnt allowed, so pass
                    else:
                        pass

            # Loop through the endpoints
            for endpoint in self.endpoints:
                
                # Check if starting on an endpoint
                if (self.starting_column == endpoint.column) and (self.starting_row == endpoint.row):
                   
                   # Run all the same checks as previously, but this time with the endpoint
                    temp_location = str(self.ending_column) + str(self.ending_row)
                    if self.grid[int(temp_location)] == "Empty" or \
                       (self.grid[int(temp_location)] == endpoint.color and endpoint.color == f.color):
                    
                        # Check if a vertical line
                        if (self.starting_column == self.ending_column) and \
                        (self.starting_row != self.ending_row):
                            a = self.starting_row
                            b = self.ending_row
                            c = 1
                            if self.ending_row < self.starting_row:
                                c = -1
                            t = 1
                            for i in range(a, b + c, c):
                                square = str(self.starting_column) + str(i)
                                if (self.grid[int(square)] == "Empty") or \
                                (self.grid[int(square)] == endpoint.color and endpoint.color == f.color):
                                    pass
                                else:
                                    t = -1
                                    
                            if t == 1:
                                self.line = Line(starting_column=self.starting_column,
                                    ending_column=self.ending_column,
                                    starting_row=self.starting_row,
                                    ending_row=self.ending_row,
                                    color=endpoint.color,
                                    canvas=self.canvas,
                                    grid_size=self.grid_size,
                                    width=self.screen_width,
                                    height=self.screen_height
                                    )
                                self.lines.append(self.line)
                            
                                # Mark all the passed through squares on the grid
                                for i in range(a, b + c, c):
                                    square = str(self.starting_column) + str(i)
                                    self.grid[int(square)] = endpoint.color
                                
                                # Set variables for an Endpoint object so you will be able to draw from it
                                if endpoint.color == self.line.color:
                                    endpoint.column = self.ending_column
                                    endpoint.row = self.ending_row                  
                 
                                # Update the ending location with the endpoint color
                                self.grid[int(temp_location)] = endpoint.color
                                
                                self.check_if_won()
                        # Check if a horizontal line   
                        elif (self.starting_row == self.ending_row) and \
                        (self.starting_column != self.ending_column):
                            a = self.starting_column
                            b = self.ending_column
                            c = 1
                            if self.ending_column < self.starting_column:
                                c = -1
                            t = 1
                            for i in range(a, b + c, c):
                                square = str(i) + str(self.starting_row)
                                if (self.grid[int(square)] == "Empty") or \
                                    ((self.grid[int(square)] == endpoint.color) and (endpoint.color == f.color)):
                                    pass
                                else:
                                    t = -1
                                        
                            if t == 1:
                                self.line = Line(starting_column=self.starting_column,
                                        ending_column=self.ending_column,
                                        starting_row=self.starting_row,
                                        ending_row=self.ending_row,
                                        color=endpoint.color,
                                        canvas=self.canvas,
                                        grid_size=self.grid_size,
                                        width=self.screen_width,
                                        height=self.screen_height
                                        )
                                self.lines.append(self.line)
                                
                                # Mark all the passed through squares on the grids
                                for i in range(a, b + c, c):
                                    square = str(i) + str(self.starting_row)
                                    self.grid[int(square)] = endpoint.color
                                
                                # Set variables for an Endpoint object so you will be able to draw from it
                                if endpoint.color == self.line.color:
                                    endpoint.column = self.ending_column
                                    endpoint.row = self.ending_row
                                                        
                                # Update the ending location with the endpoint color
                                self.grid[int(temp_location)] = endpoint.color
                                
                                self.check_if_won()
                        # If the line isn't vertical or horizontal it must be diagonal
                        # which isnt allowed, so pass
                        else:
                            pass

    def check(self):
        """Check if a line is drawn and the endpoint is updated"""
        
        # Otherwise you could just click the dots and it would be set as started
        for e in self.endpoints:
                if (e.color == self.started_color) and \
                (e.column != 0 and e.row != 0):
                    # If endpoint updated then run second check
                    self.check2(e.color)
                    
    def check2(self, color):
        """Add flows to started list"""
        
        # Loop through flows
        for f in self.flows:
            if f.color == color:
                # If the flow hasn't been started yet, update it's variable and append it
                if f.started == False:
                    f.started = True
                    self.started_flows.append(f)

    def check_if_won(self):
        """Determine if you've won"""
        
        # Loop through flows
        for f in self.flows:       
                # Make sure the flow hasn't been started
                if f.started == False:  
                    
                    # First check if you're drawing a line straight from head to tail dot or vice verse
                    if (self.starting_row == f.tail_row and \
                    self.starting_column == f.tail_column) and \
                    (self.ending_row == f.head_row and \
                    self.ending_column == f.head_column):
                        self.ended_color = f.color
                        f.ended = True
                        self.ended_flows.append(f)
                        self.text.set("Complete Flows: " + str(len(self.ended_flows)))
                    
                    elif (self.starting_row == f.head_row and \
                    self.starting_column == f.head_column) and \
                    (self.ending_row == f.tail_row and \
                    self.ending_column == f.tail_column):
                        self.ended_color = f.color
                        f.ended = True
                        self.ended_flows.append(f)
                        self.text.set("Complete Flows: " + str(len(self.ended_flows)))

                    # If you start on a head or tail, set a variable and run checking method
                    elif (self.starting_row == f.head_row and \
                    self.starting_column == f.head_column):
                        self.started_color = f.color
                        self.check()
                    
                    elif (self.starting_row == f.tail_row and \
                    self.starting_column == f.tail_column):
                        self.started_color = f.color
                        self.check()
                
                # Check if the flow has started but not ended
                elif f.started == True and f.ended != True:
                    
                    # If you end on a head or tail, set a variable and set the flow to ended
                    if (self.ending_row == f.head_row and \
                    self.ending_column == f.head_column):
                        self.ended_color = f.color
                        f.ended = True
                        self.ended_flows.append(f)
                        self.text.set("Complete Flows: " + str(len(self.ended_flows)))
                    
                    elif (self.ending_row == f.tail_row and \
                    self.ending_column == f.tail_column):
                        self.ended_color = f.color
                        f.ended = True
                        self.ended_flows.append(f)
                        self.text.set("Complete Flows: " + str(len(self.ended_flows)))

        # If all the flows are in the ended flow list you've won, so run the winners command
        if len(self.ended_flows) == 5:
            self.winner()

# Run the game
if __name__ == "__main__":
    root = Tk()
    root.title('Flow')
    app = FlowGame(root)
    root.mainloop()
