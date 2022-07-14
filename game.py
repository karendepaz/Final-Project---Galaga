from pyray import *
from point import Point
from player import Player
from score import Score
from life_counter import LifeCounter
from enemy_one import EnemyOne
from enemy_two import EnemyTwo
from enemy_three import EnemyThree

class Game:
    """
    The Game class takes care of the running game loop, generates enemies, and collision. 

    Attributes:
        player
        score
        life_counter
        enemies
    """

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
        o_positions = [Point(120, 100), Point(160, 100), Point(200, 100), Point(240, 100), Point(280, 100), Point(320, 100),
            Point(360, 100), Point(400, 100), Point(440, 100), Point(480, 100), Point(520, 100), Point(560, 100),
            Point(600, 100), Point(640, 100), Point(680, 100), Point(720, 100), Point(760, 100)]
        for position in o_positions:
            enemy = EnemyOne()
            enemy.set_position(position)
            self._enemies.append(enemy)

        # Generate "H" enemy row.
        h_positions = [Point(140, 175), Point(180, 175), Point(220, 175), Point(260, 175), Point(300, 175), Point(340, 175),
            Point(380, 175), Point(420, 175), Point(460, 175), Point(500, 175), Point(540, 175), Point(580, 175),
            Point(620, 175), Point(660, 175), Point(700, 175), Point(740, 175)]
        for position in h_positions:
            enemy = EnemyTwo()
            enemy.set_position(position)
            self._enemies.append(enemy)

        # Generate "W" enemy row.
        o_positions = [Point(120, 250), Point(160, 250), Point(200, 250), Point(240, 250), Point(280, 250), Point(320, 250),
            Point(360, 250), Point(400, 250), Point(440, 250), Point(480, 250), Point(520, 250), Point(560, 250),
            Point(600, 250), Point(640, 250), Point(680, 250), Point(720, 250), Point(760, 250)]
        for position in o_positions:
            enemy = EnemyThree()
            enemy.set_position(position)
            self._enemies.append(enemy)

    def check_object_collision(self):
        pass
