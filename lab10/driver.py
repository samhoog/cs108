"""CS 108 - Lab 10

This module builds and renders a simple solar system.

@author: Serita Nelesen (smn4)
@date: Fall, 2014
@author: Chris Wieringa (cwieri39)
@date: Fall, 2020
@author: Sam Hoogewind (sth6)
@date: Fall, 2020
"""

import tkinter
from solar_system import SolarSystem
from sun import Sun
from planet import Planet

# Prompt user for planets
try:
    name = input("Name of the planet: ")
    radius = int(input("Radius of the planet: "))
    distance = int(input("Distance of the planet: "))
    color = input("Color of the planet: ")
    user_planet = Planet(name, radius, distance, color)
except ValueError as ve:
    print("Error:", ve)
    quit()


# Setup Tkinter Canvas
WIDTH = 600
HEIGHT = WIDTH
window = tkinter.Tk()
window.title("Solar System")
canvas = tkinter.Canvas(window, width=WIDTH, height=HEIGHT, background='white')
canvas.pack()

# Build and render a solar system.
sol = Sun('Sun', 100, 5800)
ss = SolarSystem(sol)
earth = Planet('Earth', 10, 150)
ss.add_planet(earth)
ss.add_planet(user_planet)
ss.render(canvas)

# window.mainloop()  # Needed for some IDEs.
