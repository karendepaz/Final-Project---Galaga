from pyray import *
from point import Point
from player import Player
from score import Score
from life_counter import LifeCounter
from enemy_one import EnemyOne

class Game:

    def __init__(self):

        self._player = Player()
        self._score = Score()
        self._life_counter = LifeCounter()
        self._enemies = []

    def start_game(self):

        # Open the game window.
        init_window(900, 600, "Galaga")

        # Create enemies.
        self.generate_enemies()

        # Begin game loop.
        while not window_should_close():
            begin_drawing()
            clear_background(BLACK)
            self._score.display_score()
            self._life_counter.display_life_counter()
            self._player.display_player()
            for enemy in self._enemies:
                enemy.display_enemy()
                enemy.random_fire()
                enemy.advance_bullets()
                enemy.random_dive()
                enemy.advance_enemy()
            self._player.move()
            self._player.fire()
            self._player.advance_bullets()
            end_drawing()
        close_window()

    def generate_enemies(self):

        # Generate "O" enemy row.
        positions = [Point(120, 100), Point(160, 100), Point(200, 100), Point(240, 100), Point(280, 100), Point(320, 100),
            Point(360, 100), Point(400, 100), Point(440, 100), Point(480, 100), Point(520, 100), Point(560, 100),
            Point(600, 100), Point(640, 100), Point(680, 100), Point(720, 100), Point(760, 100)]
        for position in positions:
            enemy = EnemyOne()
            enemy.set_position(position)
            self._enemies.append(enemy)

    def check_object_collision(self):
        pass
