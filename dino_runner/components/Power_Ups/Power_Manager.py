import pygame
import random
from dino_runner.components.Power_Ups.Hammer import Hammer
from dino_runner.components.Power_Ups.Shield import Shield
from dino_runner.components.Power_Ups.powerUp import PowerUp
from dino_runner.utils.constants import SHIELD, HAMMER

class PupsManager:
    def __init__(self):
        self.PowerUps = []
        self.appear = 0       
    
    def update(self, game):       
        if len(self.PowerUps) == 0:
            self.pups = random.randint(0,1)
            if self.appear == game.score:
                self.appear = random.randint(self.appear+200, self.appear +300)
            if self.pups == 0:
                self.PowerUps.append(Shield(SHIELD))
            elif self.pups == 1:
                self.PowerUps.append(Hammer(HAMMER))      
        
        for powerUp in self.PowerUps:
            powerUp.update(game.game_speed, self.PowerUps)
            if game.player.dino_rect.colliderect(powerUp):
                powerUp.start_time = pygame.time.get_ticks()  
                if self.pups == 0:
                    game.player.shield = True
                    game.player.hammer = False
                    self.player_config(game, powerUp)
                    print('SHield')
                elif self.pups == 1:
                    game.player.hammer = True
                    game.player.shield = False
                    self.player_config(game, powerUp)
                    print('hammer')
                 
                self.PowerUps.remove(powerUp)
                
    def player_config(self, game, powerUp):
        game.player.has_power_up = True
        game.player.type = powerUp.type
        game.player.power_up_time = powerUp.start_time + (powerUp.duration *1000)
                                    
           
    def draw(self, screen):   
        for powerUp in self.PowerUps:
            powerUp.draw(screen)

    def Pups_reset(self):
        self.PowerUps = []
           