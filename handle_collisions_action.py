from player import Player #gets player information
from enemy import Enemy #gets enemies information
from bullet import Bullet #gets bullet information 
from game import Game #get list of enemies
from cast import Cast
from life_counter import LifeCounter
class HandleCollisionsAction():
    
    def __init__(self):
        self._is_game_over = False
    
    def handle_collisions(self,cast, lifecounter):
        bullet = cast.get_first_actor('bullets')
        player = cast.get_first_actor('player')
        enemy = cast.get_first_actor('enemy')

        if bullet.get_position().equals(enemy.get_position()):
            enemy.remove_actor()
        elif bullet.get_position().equals(player.get_position()):
            lifecounter -= 1