from bullet import Bullet
from pyray import *

class EnemyBullet(Bullet):
    """
    The EnemyBullet inherits from the bullet class. This class takes care of the enemies bullet action and attribures.
    
    Attributes:
        inherits from Bullet class
    """
    
    def __init__(self):
        super().__init__()

    def advance(self):
        if self.advance_counter < 5:
            self.advance_counter += 1
        else:
            y = self._position.get_y()
            y += 1
            self._position.set_y(y)
            self.advance_counter = 0

    def display_bullet(self):
        draw_text(self._appearance, self._position.get_x(), self._position.get_y(), 20, RED)
