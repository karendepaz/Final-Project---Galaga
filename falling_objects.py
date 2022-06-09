import pyray
import random
from point import Point

class FallingObject:
    
    def __init__(self):
        self.appearance = "0"
        self.color = ""
        self.position = Point(random.randint(2, 890), 0)
        self.points = 1
        self.move_counter = 0

    def fall(self):
        if self. move_counter < 30:
            self.move_counter += 1
        else:
            self.position.y += 1
            self.move_counter = 0

    def pick_color(self):
        picker = random.randint(1, 10)

        if picker == 1:
            return YELLOW
        elif picker == 2:
            return ORANGE
        elif picker == 3:
            return PINK
        elif picker == 4:
            return RED
        elif picker == 5:
            return DARKGREEN
        elif picker == 6:
            return LIME
        elif picker == 7:
            return SKYBLUE
        elif picker == 8:
            return BLUE
        elif picker == 9:
            return VIOLET
        elif picker == 10:
            return GOLD


# Available Colors Include:
# LIGHTGRAY
# GRAY
# DARKGRAY
# YELLOW
# GOLD
# ORANGE
# PINK
# RED
# MAROON
# GREEN
# LIME
# DARKGREEN
# SKYBLUE
# BLUE
# DARKBLUE
# PURPLE
# VIOLET
# DARKPURPLE
# BEIGE
# BROWN
# DARKBROWN
# WHITE
# BLACK
# BLANK
# MAGENTA
# RAYWHITE
