"""CS 108 Lab 12

This module implements a GUI controller for a particle simulation

@author: Serita Nelesen (smn4)
@date: Fall, 2014
@author: Keith VanderLinden (kvlinden)
@date: Fall, 2018 - updated to use callback animation
@author: Sam Hoogewind (sth6)
@date: Fall, 2020
"""

from tkinter import Tk, Canvas, Button, Frame, ALL
from random import randint
from particle import Particle
from helpers import get_random_color, distance


class ParticleSimulation:
    """ParticleSimulation runs a simulation of multiple particles interacting
    on a single canvas.
    """
    
    def __init__(self, window, width=500, height=500):
        """Instantiate the simulation GUI window."""
        self.window = window
        self.width = width
        self.height = height
        self.delay = 5

        self.canvas = Canvas(self.window, bg='black',
                             width=self.width, height=self.height)
        
        self.canvas.bind('<Button-1>', self.check_remove_particle)
        
        frame = Frame(root, width=self.width, height=40)
        frame.pack(side="bottom")
        
        add_particle_button = Button(frame, text="Add particle", command=self.add_particle)
        add_particle_button.pack()
        
        self.canvas.pack()
        
        self.p_list = []
        self.step_animation()
        
    def add_particle(self):
        """Create and add a random particle"""
        radius = randint(5, 25)
        x = randint(25, self.width - 25)
        y = randint(25, self.width - 25)
        vel_x = randint(-radius // 10, radius // 10)
        vel_y = randint(-radius // 10, radius // 10)
        color = get_random_color()
        new_particle = Particle(
            x, y, vel_x, vel_y, radius, color = get_random_color()
            )
        self.p_list.append(new_particle)
    
    def step_animation(self):
        """Animate the particle"""
        self.canvas.delete(ALL)
        for particle in self.p_list:
            particle.move(self.canvas, self.width, self.height)
        for p1 in self.p_list:
            for p2 in self.p_list:
                if p1 == p2:
                    break
                p1.bounce(p2)
        for particle in self.p_list:
            particle.render(self.canvas)
        
        self.canvas.after(self.delay, self.step_animation)
        
    def check_remove_particle(self, event):
        """Remove the particle you click on"""
        copy = self.p_list[:]
        for p in copy:
            if Particle.contains(p, event.x, event.y) == True:
                self.p_list.remove(p)
        
if __name__ == '__main__':
    root = Tk()
    root.title('Particle Simulation')    
    app = ParticleSimulation(root)
    root.mainloop()
