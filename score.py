from pyray import *

class Score:

    def __init__(self):
        self.value = 0

    def display_score(self):
        draw_text(f"Score: {self.value}", 20, 20, 25, WHITE)

    def update_score(self, points):
        self.value += points