from cgitb import text
import pygame
import random
from dino_runner.components.Obstacles.Obstacle_Manager import ObsManager
from dino_runner.components.Dino import Dino
from dino_runner.components.Power_Ups.Power_Manager import PupsManager
from dino_runner.utils.constants import BG, DEFAULT_TYPE, DINO_START, GAMEOVER, ICON, RESET, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, CLOUD
FONT_STYLE = 'freesansbold.ttf'


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.x_pos_cloud = 1200
        self.y_pos_cloud = 200
        self.player = Dino()
        self.obstacle_mg = ObsManager()
        self.powerUp_mg = PupsManager()
        self.running = False
        self.score = 0
        self.death_count = 0
        self.record = 0              
    
    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()
        pygame.quit()

    def run(self):
        # Game loop: events - update - draw
        self.score = 0
        self.obstacle_mg.obs_reset()
        self.powerUp_mg.Pups_reset()
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()       

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False               

    def update(self):
        self.score += 1
        if self.score % 100 == 0:
            self.game_speed += 1
        if self.game_speed == 51:
            self.game_speed -= 1
             
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_mg.update(self)
        self.powerUp_mg.update(self)
        if self.score >= self.record:
            self.record = self.score      

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.draw_clouds()
        self.draw_score()
        
        self.player.draw(self.screen)
        self.obstacle_mg.draw(self.screen)
        self.powerUp_mg.draw(self.screen)
        self.draw_powerup_time()

        pygame.display.update()
        pygame.display.flip()
    def draw_powerup_time(self):
        if self.player.has_power_up:
            time_to_show = round((self.player.power_up_time - pygame.time.get_ticks()) / 1000, 2)
            if time_to_show >= 0:
                self.message_components(f' {self.player.type.capitalize()} disponível por {time_to_show}', (0,0,0), SCREEN_WIDTH//2, 40)
            else:
                self.player.has_power_up = False
                self.player.type = DEFAULT_TYPE
                self.player.shield = False
                self.player.hammer = False        

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def draw_clouds(self):    
        image_width = CLOUD.get_width()
        self.screen.blit(CLOUD, (self.x_pos_cloud, self.y_pos_cloud))   
        if self.x_pos_cloud < -image_width:
            cld = random.randint(1000,2000)
            self.x_pos_cloud = cld
            self.screen.blit(CLOUD, (self.x_pos_cloud, self.y_pos_cloud))
            
        self.x_pos_cloud -= self.game_speed

    def draw_score(self):
        font = pygame.font.Font(FONT_STYLE, 18)
        text = font.render(f'Pontos: {self.score}',True, (0,0,0))
        text_rect = text.get_rect()
        text_rect.center = (1000, 40)
        self.screen.blit(text, text_rect)

        font = pygame.font.Font(FONT_STYLE, 18)
        text = font.render(f'Recorde: {self.record}',True, (0,0,0))
        text_rect = text.get_rect()
        text_rect.center = (850, 40)
        self.screen.blit(text, text_rect)
  

    def key_event_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            if event.type == pygame.KEYDOWN:
                self.run()

    def message_components(self, message, color, message_posX, message_posY):
            font = pygame.font.Font(FONT_STYLE, 20)
            text = font.render(message,True, color)
            text_rect = text.get_rect()
            text_rect.center = (message_posX, message_posY)
            self.screen.blit(text, text_rect)

    def show_menu(self):
        self.screen.fill((255, 255, 255))

        if self.death_count == 0:
            self.message_components('Pressione qualquer tecla para Iniciar', (0,0,0),SCREEN_WIDTH//2,SCREEN_HEIGHT//2)
            
            pygame.time.delay(200)
            self.screen.blit(DINO_START, ( 80  ,  320))
            self.screen.blit(BG, (0 ,380))
            
        else:
            self.message_components('Pressione qualquer tecla para Reiniciar',(0,0,0),SCREEN_WIDTH//2, SCREEN_HEIGHT//2)
            
            self.message_components(f'Pontuação Atual {self.score}', (0,0,0), SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + 50)
            
            self.message_components(f'Mortes Atuais {self.death_count}', (255,0,0),SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + 100)
            
            self.message_components(f'Recorde Atual {self.record}', (255,150,0), SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + 150)

            self.screen.blit(GAMEOVER, (SCREEN_WIDTH//2 -191, SCREEN_HEIGHT//2 - 120 ))
            self.screen.blit(RESET, (SCREEN_WIDTH//2 - 40, SCREEN_HEIGHT//2 -90 ))

        pygame.display.update()
        self.key_event_menu()                  