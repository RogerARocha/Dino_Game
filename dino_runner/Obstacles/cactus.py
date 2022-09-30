import random
from dino_runner.utils.constants import LARGE_CACTUS, SMALL_CACTUS
from dino_runner.Obstacles.obstacle import Obstacle


class Cactus(Obstacle):
    CACTUS = {
        'LARGE' : (LARGE_CACTUS, 310),
        'SMALL' : (SMALL_CACTUS, 333)
        }


    def __init__(self, cactus_type):
        image, cactus_pos = self.CACTUS[cactus_type]
        self.type = random.randint(0,2)
        super().__init__(image, self.type) 
        self.rect.y = cactus_pos