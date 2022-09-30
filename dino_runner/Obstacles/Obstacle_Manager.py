import pygame
import random
from dino_runner.Obstacles.bird import bird

from dino_runner.Obstacles.cactus import Cactus
from dino_runner.utils.constants import LARGE_CACTUS, SMALL_CACTUS, BIRD




class ObsManager:
    def __init__(self):
        self.obstacles = []
        
        
    
    
    def update(self, game):
        if len(self.obstacles) == 0:
            obs = random.randint(1,3)
            if obs == 1:   
             cactus_type = 'SMALL' if random.randint(0,1) == 0 else 'LARGE'
             self.obstacles.append(Cactus(cactus_type))

            elif obs == 2:
              cactus_type = 'SMALL' if random.randint(0,1) == 0 else 'LARGE'
              self.obstacles.append(Cactus(cactus_type))

            elif obs == 3:
                bird_type = 'high' if random.randint(0,1) == 0 else 'low'
                self.obstacles.append(bird(bird_type))
        
     

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle):
                pygame.time.delay(700)
                game.playing = False
                
                game.death_count += 1
                game.game_speed = 20
                break          
                      
                
           
    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def obs_reset(self):
        self.obstacles = []
           
        
