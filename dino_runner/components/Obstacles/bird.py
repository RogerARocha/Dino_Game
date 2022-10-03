from dino_runner.components.Obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD
import random


class bird(Obstacle):
    

    BIRD = {
        'high' : (BIRD, 260),
         'low' : (BIRD, 300)
        }


    def __init__(self, bird_type,):
        image, bird_pos = self.BIRD[bird_type]
        self.type = BIRD
        super().__init__(BIRD, self.type, True)
        self.rect.y = bird_pos
