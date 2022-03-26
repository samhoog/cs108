"""CS 108 Lab 11.0

This module implements the GUI assigned in this unit's preparation assignment.

@author: Keith VanderLinden (kvlinden)
@date: Spring, 2020
@author: Sam Hoogewind (sth6)
@date: Fall, 2020
"""

from tkinter import Tk, Label, Button, Entry


class App:

    def __init__(self, window):

        label = Label(window, text="Please enter your name.")
        label.pack()

        # Create an entry box
        entry = Entry(window)
        entry.pack()
        
        quit_button = Button(window, text='Quit', command=window.destroy)
        quit_button.pack()
       
if __name__ == '__main__':
    root = Tk()
    root.title('Hello')
    App(root)
    root.mainloop()
