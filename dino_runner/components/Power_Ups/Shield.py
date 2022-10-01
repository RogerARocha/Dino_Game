
from dino_runner.components.Power_Ups.powerUp import PowerUp
from dino_runner.utils.constants import SHIELD, SHIELD_TYPE


class Shield(PowerUp):


    def __init__(self, image):
        image = SHIELD
        
        self.type = SHIELD_TYPE
        super().__init__(image, self.type) 
     