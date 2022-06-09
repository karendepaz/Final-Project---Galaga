from pyray import *
import random
from player import Player
from score import Score
from gem import Gem
from rock import Rock
from mine import Mine

class Game:

    def __init__(self):

        self.player = Player()
        self.falling_objects = []
        self.score = Score()
        self.add_object_counter = 0

    def start_game(self):

        init_window(900, 600, "Greed")

        while not window_should_close():
            begin_drawing()
            clear_background(BLACK)
            self.check_object_removal()
            if self.add_object_counter > 500:
                picker = random.randint(1, 100)
                if picker in range(0, 6):
                    object = Mine()
                elif picker in range(6, 61):
                    object = Rock()
                elif picker in range(61, 101):
                    object = Gem()
                self.falling_objects.append(object)
                self.add_object_counter = 0
            else:
                self.add_object_counter += 1
            self.score.display_score()
            for object in self.falling_objects:
                object.fall()
                draw_text(object.appearance, object.position.x, object.position.y, 15, RED)
            self.player.move()
            draw_text(self.player.appearance, self.player.position.x, self.player.position.y, 15, WHITE)
            end_drawing()
        close_window()

    def check_object_removal(self):
        for object in self.falling_objects:
            if object.position.x in range(self.player.position.x - 8, self.player.position.x + 8):
                if object.position.y in range(self.player.position.y - 8, self.player.position.y + 8):
                    self.falling_objects.remove(object)
                    self.score.value += object.points
            if object.position.y == 590:
                self.falling_objects.remove(object)
