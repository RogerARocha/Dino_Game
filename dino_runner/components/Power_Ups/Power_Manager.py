import pygame
import random
from dino_runner.components.Power_Ups.Hammer import Hammer
from dino_runner.components.Power_Ups.Shield import Shield
from dino_runner.components.Power_Ups.powerUp import PowerUp
from dino_runner.utils.constants import SHIELD, HAMMER


chances = [1,2]

class PupsManager:
    def __init__(self):
        self.PowerUps = []
        self.appear = 0
         
    
    def update(self, game, points):       
        if len(self.PowerUps) == 0:
            pups = random.randint(0,1)
            if self.appear == points:
                self.appear = random.randint(self.appear+200, self.appear +300)
            if pups == 0:
                self.PowerUps.append(Shield(SHIELD))
            elif pups == 1:
                self.PowerUps.append(Hammer(HAMMER))
                
        

        for powerUp in self.PowerUps:
            powerUp.update(game.game_speed, self.PowerUps)
            if game.player.dino_rect.colliderect(powerUp):
                powerUp.start_time = pygame.time.get_ticks()
                
                game.player.shield = True
                game.player.type = powerUp.type
                game.player.shield_time_up = powerUp.start_time + (random.randint(5,8)*1000)
                self.PowerUps.remove(powerUp)
           

                break                         
                
           
    def draw(self, screen):
        for powerUp in self.PowerUps:
            powerUp.draw(screen)

    def Pups_reset(self):
        self.PowerUps = []
           
        
