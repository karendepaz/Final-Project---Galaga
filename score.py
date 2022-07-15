from pyray import *

class Score:
    """
    The Score class takes care of players score value. 

    Attributes:
        value
    """
    
    def __init__(self):
        self._value = 0

    def display_score(self):
        draw_text(f"Score: {self._value}", 20, 20, 15, WHITE)

    def set_score(self, points):
        self._value += points
    
    def get_score(self):
        return self._value
