import pygame
import sys
from settings import *
from level import Level
from button import Button
from game_data import level_0

class MainMenu:
    def __init__(self, screen):
        self.screen = screen
        self.background = pygame.image.load("./assets/MainMenu/background.png").convert_alpha()
        alpha_value = 120
        self.background.set_alpha(alpha_value)
        font = pygame.font.Font("assets/MainMenu/font.ttf", 40)
        self.play_button = Button("assets/MainMenu/banner.png", (WIDTH/2, HEIGHT/2 - 100), "Play", font, (0, 0, 0), (100, 100, 100))
        self.quit_button = Button("assets/MainMenu/banner.png", (WIDTH/2, HEIGHT/2 + 100), "Quit", font, (0, 0, 0), (100, 100, 100))

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.play_button.checkForInput(event.pos):
                        return "play"
                    elif self.quit_button.checkForInput(event.pos):
                        pygame.quit()
                        sys.exit()
                elif event.type == pygame.MOUSEMOTION:
                    self.play_button.changeColor(event.pos)
                    self.quit_button.changeColor(event.pos)

            self.screen.blit(self.background, (0, 0))  # Blit background image
            self.play_button.update(self.screen)
            self.quit_button.update(self.screen)
            pygame.display.flip()


class PauseMenu:
    def __init__(self, screen):
        self.screen = screen
        self.background = pygame.image.load("./assets/MainMenu/background.png").convert_alpha()
        alpha_value = 120
        self.background.set_alpha(alpha_value)
        font = pygame.font.Font("assets/MainMenu/font.ttf", 40)
        self.resume_button = Button("assets/MainMenu/banner.png", (WIDTH/2, HEIGHT/2 - 100), "Resume", font, (0, 0, 0), (100, 100, 100))
        self.restart_button = Button("assets/MainMenu/banner.png", (WIDTH/2, HEIGHT/2), "Restart", font, (0, 0, 0), (100, 100, 100))
        self.home_button = Button("assets/MainMenu/banner.png", (WIDTH/2, HEIGHT/2 + 100), "Home", font, (0, 0, 0), (100, 100, 100))
        self.quit_button = Button("assets/MainMenu/banner.png", (WIDTH/2, HEIGHT/2 + 200), "Quit", font, (0, 0, 0), (100, 100, 100))
        self.clicked_button = None 
        
    def run(self):
        self.clicked_button = None 
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.clicked_button = "resume" 
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.resume_button.checkForInput(event.pos):
                        self.clicked_button = "resume" 
                    elif self.restart_button.checkForInput(event.pos):
                        self.clicked_button = "restart" 
                    elif self.home_button.checkForInput(event.pos):
                        self.clicked_button = "home" 
                    elif self.quit_button.checkForInput(event.pos):
                        pygame.quit()
                        sys.exit()
                elif event.type == pygame.MOUSEMOTION:
                    self.resume_button.changeColor(event.pos)
                    self.restart_button.changeColor(event.pos)
                    self.home_button.changeColor(event.pos)
                    self.quit_button.changeColor(event.pos)

            self.screen.blit(self.background, (0, 0))  # Blit background image
            self.resume_button.update(self.screen)
            self.restart_button.update(self.screen)
            self.home_button.update(self.screen)
            self.quit_button.update(self.screen)
            pygame.display.flip()
            
            if self.clicked_button:  # Check if a button has been clicked
                return self.clicked_button  # Return the clicked button




class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.SRCALPHA)
        self.clock = pygame.time.Clock()
        self.state = "menu"  # Initial state is menu
        self.main_menu = MainMenu(self.screen)
        self.pause_menu = PauseMenu(self.screen)  # Added pause menu
        self.level = Level(level_0, self.screen)

    def run(self):
        while True:
            if self.state == "menu":
                self.state = self.main_menu.run()
            elif self.state == "pause":  
                pause_action = self.pause_menu.run()  
                if pause_action == "resume":
                    self.state = "play"  
                elif pause_action == "restart":
                    self.level = Level(level_0, self.screen)  
                    self.state = "play"  
                elif pause_action == "home":
                    self.state = "menu"
            elif self.state == "play":
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        self.state = "pause"  
                        
                self.screen.fill((255, 255, 255, 255))
                self.level.run()
                pygame.display.flip()
                self.clock.tick(FPS)


if __name__ == '__main__':
    game = Game()
    game.run()
