from pyray import *

class Score:

    def __init__(self):
        self._value = 0

    def display_score(self):
        draw_text(f"Score: {self._value}", 20, 20, 15, WHITE)

    def set_score(self, points):
        self._value += points