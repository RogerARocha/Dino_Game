import pygame
import random


from dino_runner.Obstacles.cactus import Cactus




class ObsManager:
    def __init__(self):
        self.obstacles = []
    
    def update(self, game):
        if len(self.obstacles) == 0:
            cactus_type = 'SMALL' if random.randint(0,1) == 0 else 'LARGE'
            self.obstacles.append(Cactus(cactus_type))

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle):
                game.game_speed = 0 
                game.player.step_index = -1
                
           
    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
           
        
