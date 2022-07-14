from pyray import *

class LifeCounter:

    def __init__(self):
        self._value = 3

    def display_life_counter(self):
        draw_text(f"Lives: {self._value}", 830, 20, 15, WHITE)
   
    def subtract_life(self):
        self._value -= 1
    
    def get_life_counter(self):
        return self._value