from pyray import *
import random
from point import Point
from bullet import Bullet

class Enemy:

    def __init__(self):
        self._appearance = ""
        self._position = Point(0, 0)
        self._dive = False
        self._move_counter = 0
        self._hit_points = 0
        self._bullets = []

    def get_appearance(self):
        return self._appearance

    def get_position(self):
        return self._position

    def set_position(self, position):
        self._position = position

    def get_hit_points(self):
        return self._hit_points

    def display_enemy(self):
        pass

    def random_fire(self):
        pass

    def random_dive(self):
        pass
