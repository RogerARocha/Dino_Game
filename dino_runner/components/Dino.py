
import pygame

from pygame.sprite import Sprite
from dino_runner.utils.constants import DINO_DEAD, DUCKING_HAMMER, HAMMER_TYPE, JUMPING, JUMPING_HAMMER, RUNNING, DUCKING,DEFAULT_TYPE,DUCKING_SHIELD,JUMPING_SHIELD, RUNNING_HAMMER,RUNNING_SHIELD, SHIELD_TYPE

RUN_IMG = {DEFAULT_TYPE: RUNNING, SHIELD_TYPE:RUNNING_SHIELD, HAMMER_TYPE:RUNNING_HAMMER}
JUMP_IMG = {DEFAULT_TYPE:JUMPING, SHIELD_TYPE:JUMPING_SHIELD, HAMMER_TYPE: JUMPING_HAMMER}
DUCK_IMG = {DEFAULT_TYPE:DUCKING, SHIELD_TYPE:DUCKING_SHIELD, HAMMER_TYPE:DUCKING_HAMMER}

class Dino(Sprite):

    X_POS = 80
    Y_POS = 310
    JUMP_VEL = 8.5

    def __init__(self):
        self.type = DEFAULT_TYPE
        self.image = RUN_IMG[self.type][0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS

        self.step_index = 0        

        self.dino_run = True
        self.dino_jump = False
        self.vel_jump = self.JUMP_VEL
        self.dino_duck = False
        self.shield = False
        self.hammer = False
        self.time_up= 0
        

    def update(self, user_input):
       if self.dino_run:
          self.run()
       elif self.dino_jump:
          self.jump()
       elif self.dino_duck:
          self.duck()
       elif self.dino_dead:
           self.dead()


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


    def run(self): 
      
        self.image = RUN_IMG[self.type][self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index +=1

    def jump(self):
        self.image = JUMP_IMG[self.type]
        if self.dino_jump:
            self.dino_rect.y -= self.vel_jump *3
            self.vel_jump -= 0.8
        if self.vel_jump < -self.JUMP_VEL:
            self.dino_rect.y = self.Y_POS
            self.dino_jump = False
            self.vel_jump = self.JUMP_VEL 

    def duck(self):
         
        self.image = DUCK_IMG[self.type][self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = 340
        self.step_index += 1
    
    def check_intangible(self):
        if self.shield:
            time_shield = round((self.shield_time_up - pygame.time.get_ticks()) / 1000, 2)
            if time_shield < 0:
                self.shield = False
                self.hammer= False
                self.update_to_default(SHIELD_TYPE)
                self.update_to_default(HAMMER_TYPE)

    def update_to_default(self, current_type):
        if self.type == current_type:
            self.type = DEFAULT_TYPE
    
        



            
    def draw(self, screen: pygame.Surface):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))