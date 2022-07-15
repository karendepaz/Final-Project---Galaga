from pyray import *

class LifeCounter:

    def __init__(self):
        self.value = 3

    def display_life_counter(self):
        draw_text(f"Lives: {self.value}", 830, 20, 15, WHITE)

    def set_life_counter(self, points):
        self.value += points