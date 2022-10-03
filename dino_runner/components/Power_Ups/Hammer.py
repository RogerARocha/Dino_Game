from dino_runner.components.Power_Ups.powerUp import PowerUp
from dino_runner.utils.constants import HAMMER, HAMMER_TYPE

class Hammer(PowerUp):


    def __init__(self, image):
        
        
        self.type = HAMMER_TYPE
        super().__init__(image, self.type) 