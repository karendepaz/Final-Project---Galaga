from pyray import *
import random
from point import Point
from enemy import Enemy
from enemy_bullet import EnemyBullet

class EnemyTwo(Enemy):
    """
    The EnemyTwo class inherits from the Enemy class. This class takes care of the "H" enemy, its action and attributes.

    Attributes:
        inherits Enemy class
        appearance
        score
        hit_points
    """

    def __init__(self):
        super().__init__()
        self._appearance = "H"
        self._score = 300
        self._hit_points = 1

    def display_enemy(self):
        draw_text(self._appearance, self._position.get_x(), self._position.get_y(), 20, GREEN)

    def random_fire(self):
        maybe_fire = random.randint(1, 100000)

        if maybe_fire == 500:
            bullet = EnemyBullet()
            bullet.set_position(self._position)
            self._bullets.append(bullet)
            print("\033[31m" + "Pew!" + "\033[39m")

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
        maybe_dive = random.randint(1, 150000)

        if maybe_dive == 500:
            self._dive = True

    def advance_enemy(self):
        if self._dive == True:
            if self._move_counter < 8:
                self._move_counter += 1
            else:
                y = self._position.get_y()
                y += 1
                self._position.set_y(y)
                if self._position.get_y() == 640:
                    self._position.set_y(-100)
                if self._position.get_y() == 175:
                    self._dive = False
                self._move_counter = 0