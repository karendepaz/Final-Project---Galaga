import pyray
from point import Point

class Player:

    def __init__(self):
        self.appearance = "#"
        self.position = Point(450, 300)
        self.move_counter = 0

    def move(self):
        if self.position.x == 2:
            self.position.x += 1
            return

        if self.position.x == 890:
            self.position.x -= 1
            return

        if self.position.y == 2:
            self.position.y += 1
            return

        if self.position.y == 590:
            self.position.y -= 1
            return

        if pyray.is_key_down(pyray.KEY_LEFT) and pyray.is_key_down(pyray.KEY_RIGHT):
            return

        if pyray.is_key_down(pyray.KEY_LEFT) and pyray.is_key_down(pyray.KEY_UP):
            if self. move_counter < 20:
                self.move_counter += 1
            else:
                self.position.x -= 1
                self.position.y -= 1
                self.move_counter = 0
            return

        if pyray.is_key_down(pyray.KEY_LEFT) and pyray.is_key_down(pyray.KEY_DOWN):
            if self. move_counter < 20:
                self.move_counter += 1
            else:
                self.position.x -= 1
                self.position.y += 1
                self.move_counter = 0
            return

        if pyray.is_key_down(pyray.KEY_RIGHT) and pyray.is_key_down(pyray.KEY_UP):
            if self. move_counter < 20:
                self.move_counter += 1
            else:
                self.position.x += 1
                self.position.y -= 1
                self.move_counter = 0
            return

        if pyray.is_key_down(pyray.KEY_RIGHT) and pyray.is_key_down(pyray.KEY_DOWN):
            if self. move_counter < 20:
                self.move_counter += 1
            else:
                self.position.x += 1
                self.position.y += 1
                self.move_counter = 0
            return

        if pyray.is_key_down(pyray.KEY_UP) and pyray.is_key_down(pyray.KEY_DOWN):
            return

        if pyray.is_key_down(pyray.KEY_LEFT):
            if self. move_counter < 20:
                self.move_counter += 1
            else:
                self.position.x -= 1
                self.move_counter = 0
            return
        
        if pyray.is_key_down(pyray.KEY_RIGHT):
            if self. move_counter < 20:
                self.move_counter += 1
            else:
                self.position.x += 1
                self.move_counter = 0
            return
        
        if pyray.is_key_down(pyray.KEY_UP):
            if self. move_counter < 20:
                self.move_counter += 1
            else:
                self.position.y -= 1
                self.move_counter = 0
            return
        
        if pyray.is_key_down(pyray.KEY_DOWN):
            if self. move_counter < 20:
                self.move_counter += 1
            else:
                self.position.y += 1
                self.move_counter = 0
            return