from pyray import *
import random
from point import Point
from bullet import Bullet

class Enemy:
    """
    The enemy class takes care of the enemies action and attributes. 

    Attributes:
        appearance
        position
        score
        dive
        move_counter
        hit_points
        bullets
    """

    def __init__(self):
        self._appearance = ""
        self._position = Point(0, 0)
        self._score = 0
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

    def get_score(self):
        return self._score

    def get_hit_points(self):
        return self._hit_points

    def display_enemy(self):
        pass

    def random_fire(self):
        pass

    def advance_bullets(self):
        if len(self._bullets) > 0:
            for bullet in self._bullets:
                position = bullet.get_position()
                y = position.get_y()
                if y > 600:
                    self._bullets.remove(bullet)
                else:
                    bullet.advance()
                    bullet.display_bullet()

    def random_dive(self):
        pass
