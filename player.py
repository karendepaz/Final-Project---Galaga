from pyray import *
from point import Point
from player_bullet import PlayerBullet

class Player:
    """
    The Player class takes care of the players actions and attributes.

    Attributes:
        appearance
        position
        hit_points
        move_counter
        fire_counter
        bullets
    """

    def __init__(self):
        self._appearance = "A"
        self._position = Point(450, 550)
        self._hit_points = 1
        self.move_counter = 0
        self.fire_counter = 0
        self._bullets = []

    def get_appearance(self):
        return self._appearance

    def display_player(self):
        draw_text(self._appearance, self._position.get_x(), self._position.get_y(), 20, WHITE)
 
    def move(self):

        # Keep player on screen.
        if self._position.get_x() == 2:
            self._position.set_x(3)
            return
        if self._position.get_x() == 890:
            self._position.set_x(889)
            return

        # Check if player is trying to move left and right
        # at the same time. If they are, do nothing.
        if is_key_down(KEY_LEFT) and is_key_down(KEY_RIGHT):
            return

        # Check if the player is trying to move left.
        # If they are, increase the move counter until
        # it reaches 20 and then move them left.
        if is_key_down(KEY_LEFT):
            if self.move_counter < 17:
                self.move_counter += 1
            else:
                x = self._position.get_x()
                x -= 1
                self._position.set_x(x)
                self.move_counter = 0
            return
        
        # Check if the player is trying to move right.
        # If they are, increase the move counter until
        # it reaches 20 and then move them right.
        if is_key_down(KEY_RIGHT):
            if self.move_counter < 17:
                self.move_counter += 1
            else:
                x = self._position.get_x()
                x += 1
                self._position.set_x(x)
                self.move_counter = 0
            return

    def fire(self):
        if self.fire_counter < 1000:
            self.fire_counter += 1

        if is_key_down(KEY_SPACE):
            if self.fire_counter == 1000:
                bullet = PlayerBullet()
                bullet.set_position(self._position)
                self._bullets.append(bullet)
                print("\033[33m" + "Pew!" + "\033[39m")
                self.fire_counter = 0

    def advance_bullets(self):
        if len(self._bullets) > 0:
            for bullet in self._bullets:
                position = bullet.get_position()
                y = position.get_y()
                if y < 0:
                    self._bullets.remove(bullet)
                else:
                    bullet.advance()
                    bullet.display_bullet()
    
    def get_bullet(self):
        return self._bullets

    def get_hit_points(self):
        return self._hit_points

    def subtract_hit_points(self):
        self._hit_points -= 1

    def remove_bullet(self, bullet):
        self._bullets.remove(bullet)

    def get_position(self):
        return self._position
    
    def reset_position(self):
        self._position = Point(450, 550)
    
    def reset_hit_points(self):
        self._hit_points = 1

    def game_over(self):
        self._appearance = "GAME OVER"
