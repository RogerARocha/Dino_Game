import pygame

from pygame.sprite import Sprite

from dino_runner.utils.constants import  BIRD, SCREEN_WIDTH


class Obstacle(Sprite):
    

    def __init__(self, image, type, bird = False):
        if bird:
            self.image = image[0]
            self.rect = self.image.get_rect()
        else:
            self.image = image  
            self.rect = self.image[self.type].get_rect()     
        self.type = type
        self.rect.x = SCREEN_WIDTH
        self.fly_index = 0
        
      

    def update(self, game_speed, obstacles):
        self.rect.x -= game_speed
        if type(self.type) == list:
            self.fly()
        if self.fly_index >= 10:
            self.fly_index = 0 
        if self.rect.x < -self.rect.width:
            obstacles.pop()
        self.fly_index += 1

    def fly(self):
         if self.fly_index < 5:
            self.image = BIRD[0]
            
         else:
            self.image = BIRD[1]       

        
    def draw(self, screen: pygame.Surface):
        if type(self.type) != list:
            screen.blit(self.image[self.type], self.rect)
        else:
            screen.blit(self.image, self.rect)



