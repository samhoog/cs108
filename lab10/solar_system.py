"""CS 108 - Lab 10

This class models a solar system.

@author: Serita Nelesen (smn4)
@date: Fall, 2014
@author: Chris Wieringa (cwieri39)
@date: Fall, 2020
@author: Sam Hoogewind (sth6)
@date: Fall, 2020
"""
from sun import Sun
from planet import Planet

class SolarSystem:
    
    def __init__(self, sun):
        self.planets = []
        self.planet = ''
        if isinstance(sun, Sun):
            self.sun = sun
        else:
            raise TypeError("The given parameter is not a sun class object.")
        
    def add_planet(self, planet):
        if isinstance(planet, Planet):
            self.planets.append(planet)
        else:
            raise TypeError("The given parameter is not a planet class object.")
        
    def __str__(self):
        result = 'Sun: ' + str(self.sun)
        if len(self.planets) > 0:
            result += '\nPlanets:'
            for planet in self.planets:
                result += ' ' + str(planet)
        return result

    def render(self, canvas):
        for planet in self.planets:
            Planet.render(planet, canvas)
        Sun.render(self.sun, canvas)
