from cgitb import text
import pygame
from dino_runner.Obstacles.Obstacle_Manager import ObsManager
from dino_runner.components.Dino import Dino
from dino_runner.utils.constants import BG, DINO_START, GAMEOVER, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS
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
        self.player = Dino()
        self.obstacle_mg = ObsManager()
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
        if self.score >= self.record:
            self.record = self.score

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()

        self.draw_score()

        self.player.draw(self.screen)
        self.obstacle_mg.draw(self.screen)

        pygame.display.update()
        pygame.display.flip()
        

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

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

    
    def show_menu(self):
        self.screen.fill((255, 255, 255))

        if self.death_count == 0:
            font = pygame.font.Font(FONT_STYLE, 20)
            text = font.render('Pressione qualquer tecla para Iniciar',True, (0,0,0))
            text_rect = text.get_rect()
            text_rect.center = (SCREEN_WIDTH//2, SCREEN_HEIGHT//2)
            self.screen.blit(text, text_rect)
            pygame.time.delay(200)
            self.screen.blit(DINO_START, ( 80  ,  300))
            
        else:
            font = pygame.font.Font(FONT_STYLE, 20)
            text = font.render('Pressione qualquer tecla para Reiniciar',True, (0,0,0))
            text_rect = text.get_rect()
            text_rect.center = (SCREEN_WIDTH//2, SCREEN_HEIGHT//2)
            self.screen.blit(text, text_rect)

            font = pygame.font.Font(FONT_STYLE, 20)
            text = font.render(f'Pontuação Atual {self.score}',True, (0,0,0))
            text_rect = text.get_rect()
            text_rect.center = (SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + 50)
            self.screen.blit(text, text_rect)

            font = pygame.font.Font(FONT_STYLE, 20)
            text = font.render(f'Mortes Atuais {self.death_count}',True, (255,0,0))
            text_rect = text.get_rect()
            text_rect.center = (SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + 100)
            self.screen.blit(text, text_rect)

            font = pygame.font.Font(FONT_STYLE, 20)
            text = font.render(f'Recorde Atual {self.record}',True, (255,150,0))
            text_rect = text.get_rect()
            text_rect.center = (SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + 150)
            self.screen.blit(text, text_rect)

            self.screen.blit(GAMEOVER, (SCREEN_WIDTH//2 -191, SCREEN_HEIGHT//2 - 120 ))

        
        
       


        pygame.display.update()
        self.key_event_menu()
        
    
           
        

