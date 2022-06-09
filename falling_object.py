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
