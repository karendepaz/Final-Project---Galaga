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
            self.check_object_collision()
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
        player_bullets = self._player.get_bullet()
        
        for bullet in player_bullets:
            for enemy in self._enemies:
                if bullet.get_position().get_x() in range(enemy.get_position().get_x(), enemy.get_position().get_x() + 16):
                    if bullet.get_position().get_y() in range(enemy.get_position().get_y(), enemy.get_position().get_y() + 16):
                        bullet.subtract_hit_points()
                        enemy.subtract_hit_points()
                    
                        if bullet.get_hit_points() == 0:
                            self._player.remove_bullet(bullet)
                                
                        if enemy.get_hit_points() == 0:
                            self._enemies.remove(enemy)
                            self._score.set_score(enemy.get_score())
        
        for enemy in self._enemies:
            if enemy.get_position().get_x() in range(self._player.get_position().get_x(), self._player.get_position().get_x() + 20):
                    if enemy.get_position().get_y() in range(self._player.get_position().get_y(), self._player.get_position().get_y() + 20):
                        enemy.subtract_hit_points()
                        self._player.subtract_hit_points()

                        if enemy.get_hit_points() == 0:
                            self._enemies.remove(enemy)
                        
                        if self._player.get_hit_points() == 0:
                            self._player.reset_position()
                            self._player.reset_hit_points()
                        
                        if self._life_counter.get_life_counter() > 0:
                            self._life_counter.subtract_life()
            
            enemy_bullets = enemy.get_bullets()
            
            for bullet in enemy_bullets:
                if bullet.get_position().get_x() in range(self._player.get_position().get_x(), self._player.get_position().get_x() + 16):
                    if bullet.get_position().get_y() in range(self._player.get_position().get_y(), self._player.get_position().get_y() + 16):
                        bullet.subtract_hit_points()
                        self._player.subtract_hit_points()

                        if bullet.get_hit_points() == 0:
                            enemy.remove_bullet(bullet)

                        if self._player.get_hit_points() == 0:
                            self._player.reset_position()
                            self._player.reset_hit_points()
                        
                        if self._life_counter.get_life_counter() > 0:
                            self._life_counter.subtract_life()

        if self._life_counter.get_life_counter() == 0:
            self._player.game_over()


                        
            


        
