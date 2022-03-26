"""CS 108 Lab 12

This module implements a model of a particle.

@author: Serita Nelesen (smn4)
@date: Fall, 2014
@author: Sam Hoogewind (sth6)
@date: Fall, 2020
"""

from helpers import distance


class Particle:
    """ Particle models a single particle that may be rendered to a canvas. """

    def __init__(self, x=50, y=50, vel_x=1, vel_y=1.5, radius=40, color="red"):
        """Instantiate a particle object."""
        self.x = x
        self.y = y
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.radius = radius
        self.color = color

    # Add your methods here...

    def hits(self, other):
        """ Determine if I've collided with 'other'. """
        if self == other:
            # I can't collide with myself.
            return False

        # Determine if I overlap with the other particle.
        return (
            self.radius + other.radius >=
            distance(self.x, self.y, other.x, other.y)
        )

    def bounce(self, other):
        """Handle elastic collisions between this particle and 'other'.
        
        This method checks if the two particles collide and, if so, modifies
        the positions and velocities to reflect the result of the collision.

        The result is reasonably physically accurate, but limited by being
        run only *after* a collision has already occurred.

        Both objects are changed, so this method should only be run once for each pair of objects.

        Thanks to Dr. Paul Harper (Calvin Physics).
        """
        if not self.hits(other):
            return

        # Calculate masses (proportional to area)
        m1 = self.radius ** 2
        m2 = other.radius ** 2

        # Calculate velocity of center of mass
        v_cm_x = (m1 * self.vel_x + m2 * other.vel_x) / (m1 + m2)
        v_cm_y = (m1 * self.vel_y + m2 * other.vel_y) / (m1 + m2)

        # Calculate new velocities.
        # Note that the velocity of the center of mass is unchanged, and
        # that if the center of mass is not moving, the velocity just inverts.
        self.vel_x = 2 * v_cm_x - self.vel_x
        self.vel_y = 2 * v_cm_y - self.vel_y

        other.vel_x = 2 * v_cm_x - other.vel_x
        other.vel_y = 2 * v_cm_y - other.vel_y

        # Fix up the positions to ensure they're not stuck together.
        dist_x = self.x - other.x
        dist_y = self.y - other.y
        dist = (dist_x ** 2 + dist_y ** 2) ** 0.5
        dist_x_norm = dist_x / dist
        dist_y_norm = dist_y / dist
        intrusion_distance = (self.radius + other.radius - dist) / 2 + 1e-6

        self.x += intrusion_distance * dist_x_norm
        self.y += intrusion_distance * dist_y_norm
        other.x -= intrusion_distance * dist_x_norm
        other.y -= intrusion_distance * dist_y_norm
        
    def render(self, canvas):
        """Renders the particles"""
        canvas.create_oval(
            self.x - self.radius,
            self.y - self.radius,
            self.x + self.radius,
            self.y + self.radius,
            fill=self.color
        )
        
    def move(self, canvas, width, height):
        """Moves the particle"""
        self.x += self.vel_x
        self.y += self.vel_y
        
        if (self.x + self.radius) > width or (self.x - self.radius) < 0:
            self.x -= self.vel_x
            self.vel_x = -self.vel_x
            
        if (self.y + self.radius) > height or (self.y - self.radius) < 0:
            self.y -= self.vel_y
            self.vel_y = -self.vel_y
            
    def contains(self, x, y):
        """Check i you the spot you click is in a particle"""
        if distance(self.x, self.y, x, y) < self.radius:
            return True