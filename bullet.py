from pyray import *
from point import Point

class Bullet:

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