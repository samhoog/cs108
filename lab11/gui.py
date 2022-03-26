"""CS 108 Lab 11.2

This module implements a basic calculator GUI.

@author: Serita Nelesen (smb4)
@date: Fall, 2014
@author: Keith VanderLinden (kvlinden)
@date: Spring, 2020 - ported to ZyLabs

@author: Sam Hoogewind (sth6)
@date: Fall, 2020
"""

from tkinter import (
    Tk, Label, Entry, Button, Radiobutton, Frame, E, W, LEFT, StringVar)
from calculator import Calculator


class App:

    def __init__(self, window):
        """Build the Calculator interface."""

        # Instantiate a single calculator object for repeated use.
        self.calculator = Calculator()
        
        # Create and instantiate a StringVar object
        self.operator = StringVar()
        self.operator.set("+")

        # Build the input widgets for the two operands.
        input1_label = Label(window, text="Input 1:")
        input1_label.grid(row=0, column=0, sticky=E)
        self.input1 = StringVar()
        input1_entry = Entry(window, width=6, textvariable=self.input1)
        input1_entry.grid(row=0, column=1, sticky=W)
        input2_label = Label(window, text="Input 2:")
        input2_label.grid(row=1, column=0, sticky=E)
        self.input2 = StringVar()
        input2_entry = Entry(window, width=6, textvariable=self.input2)
        input2_entry.grid(row=1, column=1, sticky=W)
        
        # Create a frame for the radio buttons
        operator_frame = Frame(window)
        operator_frame.grid(row=2, column=0, columnspan=2)
        
        # Add buttons for each operator
        add_button = Radiobutton(operator_frame, text="+", variable=self.operator, value='+')
        add_button.pack(side=LEFT)
        subtract_button = Radiobutton(operator_frame, text="-", variable=self.operator, value='-')
        subtract_button.pack(side=LEFT)
        multiply_button = Radiobutton(operator_frame, text="*", variable=self.operator, value='*')
        multiply_button.pack(side=LEFT)
        divide_button = Radiobutton(operator_frame, text="/", variable=self.operator, value='/')
        divide_button.pack(side=LEFT)
        
        # Create a calculate button
        calculate_button = Button(window, text="Calculate", command=self.do_calculation)
        calculate_button.grid(row=3, column=0)
        
        # Create a result label
        result_label = Label(window, text="Result:")
        result_label.grid(row=3, column=1)
        self.result = StringVar()
        self.result_label = Label(window, textvariable=self.result, width=6)
        self.result_label.grid(row=3, column=2, sticky=W)
        
        # Create a label for errors
        self.error = StringVar()
        self.error.set("Ready to calculate!")
        error_label = Label(window, textvariable=self.error)
        error_label.grid(row=4, column=0, columnspan=4)
    
        
    def do_calculation(self):
        """Use the calculator application to preform the calculations"""
        try:
            self.error.set("Ready to calculate!")
            result = self.calculator.calculate(
                self.input1.get(),
                self.operator.get(),
                self.input2.get()
            )
            self.result.set(result)
        # Handle exceptions
        except ValueError as ve:
            self.error.set(ve)
        except ZeroDivisionError as zde:
            self.error.set(zde)
        
if __name__ == '__main__':
    root = Tk()
    root.title('Calculator')
    app = App(root)
    root.mainloop()
