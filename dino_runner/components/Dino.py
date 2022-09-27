
import pygame

from pygame.sprite import Sprite
from dino_runner.utils.constants import JUMPING, RUNNING, DUCKING

class Dino(Sprite):

    X_POS = 80
    Y_POS = 310
    JUMP_VEL = 8.5

    def __init__(self):

        self.image = RUNNING[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS

        self.step_index = 0
        self.duck_index = 0        

        self.dino_run = True
        self.dino_jump = False
        self.vel_jump = self.JUMP_VEL
        self.dino_duck = False

    def update(self, user_input):
       if self.dino_run:
          self.run()
       elif self.dino_jump:
          self.jump()
       elif self.dino_duck:
          self.duck()


       if user_input[pygame.K_UP] or user_input[pygame.K_w]:

           self.dino_jump = True
           self.dino_run = False 
       elif not self.dino_jump:

           self.dino_jump = False
           self.dino_run = True
       if user_input[pygame.K_DOWN] or user_input[pygame.K_s]:
           self.dino_duck = True
           self.dino_run = False

       if self.step_index >=10:
          self.step_index = 0
       if self.duck_index >=10:
          self.duck_index = 0

    def run(self):
       if self.step_index < 5:
            self.image = RUNNING[0]
            
       else:
            self.image = RUNNING[1]

       self.dino_rect = self.image.get_rect()
       self.dino_rect.x = self.X_POS
       self.dino_rect.y = self.Y_POS
       self.step_index +=1

    def jump(self):
        self.image = JUMPING
        if self.dino_jump:
            self.dino_rect.y -= self.vel_jump *4
            self.vel_jump -= 0.8
        if self.vel_jump < -self.JUMP_VEL:
            self.dino_rect.y = self.Y_POS
            self.dino_jump = False
            self.vel_jump = self.JUMP_VEL 
    def duck(self):
      if self.duck_index < 5:
         self.image = DUCKING[0]

      
      else:
         self.image = DUCKING[1]
         

      self.dino_rect = self.image.get_rect()
      self.dino_rect.x = self.X_POS
      self.dino_rect.y = 340
      self.duck_index += 1


            
    def draw(self, screen: pygame.Surface):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))