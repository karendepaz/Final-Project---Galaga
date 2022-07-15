from pyray import *
from point import Point

class Bullet:
    """
    The Bullet class takes care of the bullets action and attributes. 

    Atrributes:
        appearance
        position
        advance_counter
        hit_points
    """
    
    def __init__(self):
        self._appearance = "|"
        self._position = Point(0, 0)
        self.advance_counter = 0
        self._hit_points = 1

    def get_appearance(self):
        return self._appearance

    def get_position(self):
        return self._position

    def set_position(self, position):
        x = position.get_x()
        y = position.get_y()
        self._position.set_x(x)
        self._position.set_y(y)

    def advance(self):
        pass

    def display_bullet(self):
        pass

    def get_hit_points(self):
        return self._hit_points

    def subtract_hit_points(self):
        self._hit_points -= 1
