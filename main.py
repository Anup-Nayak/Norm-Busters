import pygame
import sys
from settings import *
from level import Level
from button import Button
from game_data import *
from debug import *


class LevelMap:
    def __init__(self, screen):
        self.screen = screen
        self.background = pygame.image.load("./assets/level_map/map2.png").convert_alpha()
        alpha_value = 120
        self.background.set_alpha(alpha_value)
        font = pygame.font.Font("assets/MainMenu/font.ttf", 40)
        self.level0_button = Button("assets/level_map/levelNum.png", (201, 601), "", font,(255, 255, 255), (100, 100, 100),True)
        self.level1_button = Button("assets/level_map/levelNum.png", (411, 544), "", font, (255, 255, 255), (100, 100, 100),True)
        self.level2_button = Button("assets/level_map/levelNum.png", (632, 477), "", font, (255, 255, 255), (100, 100, 100),True)
        self.level3_button = Button("assets/level_map/levelNum.png", (827, 420 ), "", font, (255, 255, 255), (100, 100, 100),True)
        self.clicked_button = None 
        
    def run(self):
        self.clicked_button = None 
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.level0_button.checkForInput(event.pos):
                        self.clicked_button = "level0" 
                    elif self.level1_button.checkForInput(event.pos):
                        self.clicked_button = "level1" 
                    elif self.level2_button.checkForInput(event.pos):
                        self.clicked_button = "level2" 
                    elif self.level3_button.checkForInput(event.pos):
                        self.clicked_button = "level3" 
                elif event.type == pygame.MOUSEMOTION:
                    self.level0_button.changeColor(event.pos)
                    self.level1_button.changeColor(event.pos)
                    self.level2_button.changeColor(event.pos)
                    self.level3_button.changeColor(event.pos)

            self.screen.blit(self.background, (0, 0))  
            self.level0_button.update(self.screen)
            self.level1_button.update(self.screen)
            self.level2_button.update(self.screen)
            self.level3_button.update(self.screen)
            pygame.display.flip()
            
            if self.clicked_button:  
                return self.clicked_button  
            
class MainMenu:
    def __init__(self, screen):
        self.screen = screen
        self.background = pygame.image.load("./assets/MainMenu/bg8.jpg").convert_alpha()
        alpha_value = 120
        self.background.set_alpha(alpha_value)
        font = pygame.font.Font("assets/MainMenu/font.ttf", 60)
        font1 = pygame.font.Font("assets/MainMenu/font.ttf", 100)
        self.no_button = Button("assets/MainMenu/banner.png", (WIDTH/2, HEIGHT/2 - 250), "Norm Busters", font1, (255, 255, 255), (255, 255, 255),True)
        self.play_button = Button("assets/MainMenu/banner.png", (WIDTH/2, HEIGHT/2 - 50), "Play", font, (255, 255, 255), (100, 100, 100),True)
        self.level_button = Button("assets/MainMenu/banner.png", (WIDTH/2, HEIGHT/2 + 50), "Level", font, (255, 255, 255), (100, 100, 100),True)
        self.quit_button = Button("assets/MainMenu/banner.png", (WIDTH/2, HEIGHT/2 + 150), "Quit", font, (255, 255, 255), (100, 100, 100),True)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.play_button.checkForInput(event.pos):
                        return "play"
                    elif self.level_button.checkForInput(event.pos):
                        # print("level")
                        return "levelMap"
                    elif self.quit_button.checkForInput(event.pos):
                        pygame.quit()
                        sys.exit()
                elif event.type == pygame.MOUSEMOTION:
                    self.play_button.changeColor(event.pos)
                    self.level_button.changeColor(event.pos)
                    self.quit_button.changeColor(event.pos)

            self.screen.blit(self.background, (0, 0))  
            self.no_button.update(self.screen)
            self.play_button.update(self.screen)
            self.level_button.update(self.screen)
            self.quit_button.update(self.screen)
            pygame.display.flip()

class PauseMenu:
    def __init__(self, screen):
        self.screen = screen
        self.background = pygame.image.load("./assets/MainMenu/bg8.jpg").convert_alpha()
        alpha_value = 120
        self.background.set_alpha(alpha_value)
        font = pygame.font.Font("assets/MainMenu/font.ttf", 40)
        self.resume_button = Button("assets/MainMenu/banner.png", (WIDTH/2, HEIGHT/2 - 100), "Resume", font, (255, 255, 255), (100, 100, 100),True)
        self.restart_button = Button("assets/MainMenu/banner.png", (WIDTH/2, HEIGHT/2), "Restart", font, (255, 255, 255), (100, 100, 100),True)
        self.home_button = Button("assets/MainMenu/banner.png", (WIDTH/2, HEIGHT/2 + 100), "Home", font, (255, 255, 255), (100, 100, 100),True)
        self.quit_button = Button("assets/MainMenu/banner.png", (WIDTH/2, HEIGHT/2 + 200), "Quit", font, (255, 255, 255), (100, 100, 100),True)
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

            self.screen.blit(self.background, (0, 0))  
            self.resume_button.update(self.screen)
            self.restart_button.update(self.screen)
            self.home_button.update(self.screen)
            self.quit_button.update(self.screen)
            pygame.display.flip()
            
            if self.clicked_button:  
                return self.clicked_button 

class Completed:
    def __init__(self, screen):
        self.screen = screen
        self.background = pygame.image.load("./assets/MainMenu/bg8.jpg").convert_alpha()
        
        font = pygame.font.Font("assets/MainMenu/font.ttf", 50)
        font1 = pygame.font.Font("assets/MainMenu/font.ttf", 100)
        self.no_button = Button("assets/MainMenu/banner.png", (WIDTH/2, HEIGHT/2 - 250), "Level Completed!", font1, (255, 255, 255), (255, 255, 255),True)
        self.next_button = Button("assets/MainMenu/banner.png", (WIDTH/2, HEIGHT/2 -100), "Next Level", font, (255, 255, 255), (100, 100, 100),True)
        self.restart_button = Button("assets/MainMenu/banner.png", (WIDTH/2, HEIGHT/2 ), "Levels", font, (255, 255, 255), (100, 100, 100),True)
        self.home_button = Button("assets/MainMenu/banner.png", (WIDTH/2, HEIGHT/2 + 100), "Home", font, (255, 255, 255), (100, 100, 100),True)
        self.quit_button = Button("assets/MainMenu/banner.png", (WIDTH/2, HEIGHT/2 + 200), "Quit", font, (255, 255, 255), (100, 100, 100),True)
        self.clicked_button = None 
        
    def run(self):
        self.clicked_button = None 
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.restart_button.checkForInput(event.pos):
                        self.clicked_button = "levelMap" 
                    elif self.home_button.checkForInput(event.pos):
                        self.clicked_button = "menu" 
                    elif self.next_button.checkForInput(event.pos):
                        self.clicked_button = "next" 
                    elif self.quit_button.checkForInput(event.pos):
                        pygame.quit()
                        sys.exit()
                elif event.type == pygame.MOUSEMOTION:
                    
                    self.restart_button.changeColor(event.pos)
                    self.home_button.changeColor(event.pos)
                    self.quit_button.changeColor(event.pos)
                    self.next_button.changeColor(event.pos)

            self.screen.blit(self.background, (0, 0))  
            self.no_button.update(self.screen)
            self.restart_button.update(self.screen)
            self.next_button.update(self.screen)
            self.home_button.update(self.screen)
            self.quit_button.update(self.screen)
            pygame.display.flip()
            
            if self.clicked_button:  
                return self.clicked_button  

class Over:
    def __init__(self, screen):
        self.screen = screen
        self.background = pygame.image.load("./assets/MainMenu/bg8.jpg").convert_alpha()
        
        font = pygame.font.Font("assets/MainMenu/font.ttf", 50)
        font1 = pygame.font.Font("assets/MainMenu/font.ttf", 100)
        self.no_button = Button("assets/MainMenu/banner.png", (WIDTH/2, HEIGHT/2 - 250), "Level Failed!", font1, (255, 255, 255), (255, 255, 255),True)
        self.restart_button = Button("assets/MainMenu/banner.png", (WIDTH/2, HEIGHT/2), "Retry", font, (255, 255, 255), (100, 100, 100),True)
        self.home_button = Button("assets/MainMenu/banner.png", (WIDTH/2, HEIGHT/2 + 100), "Home", font, (255, 255, 255), (100, 100, 100),True)
        self.quit_button = Button("assets/MainMenu/banner.png", (WIDTH/2, HEIGHT/2 + 200), "Quit", font, (255, 255, 255), (100, 100, 100),True)
        self.clicked_button = None 
        
    def run(self):
        self.clicked_button = None 
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.restart_button.checkForInput(event.pos):
                        self.clicked_button = "play" 
                    elif self.home_button.checkForInput(event.pos):
                        self.clicked_button = "menu" 
                    elif self.quit_button.checkForInput(event.pos):
                        pygame.quit()
                        sys.exit()
                elif event.type == pygame.MOUSEMOTION:
                    
                    self.restart_button.changeColor(event.pos)
                    self.home_button.changeColor(event.pos)
                    self.quit_button.changeColor(event.pos)

            self.screen.blit(self.background, (0, 0))  
            self.no_button.update(self.screen)
            self.restart_button.update(self.screen)
            self.home_button.update(self.screen)
            self.quit_button.update(self.screen)
            pygame.display.flip()
            
            if self.clicked_button:  
                return self.clicked_button  

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("NormBusters")

        sound_file = "./assets/sound/a.mp3"
        pygame.mixer.music.load(sound_file)
        pygame.mixer.music.play(-1) 
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.SRCALPHA)
        self.clock = pygame.time.Clock()
        self.state = "menu"  
        self.main_menu = MainMenu(self.screen)
        self.pause_menu = PauseMenu(self.screen)  
        self.completed_menu = Completed(self.screen)
        self.over_menu = Over(self.screen)
        self.levelNumbers = [level_0,level_1,level_2,level_3]
        self.levelTexts = ['Level 0','Level 1','Level 2','Level 3']
        self.levelIndex = 0
        self.level =  Level(self.levelNumbers[self.levelIndex], self.screen, type = self.levelTexts[self.levelIndex])  
        self.levelMap = LevelMap(self.screen)  

    def run(self):
        while True:
            if self.state == "menu":
                self.state = self.main_menu.run()
            elif self.state == "pause":  
                pause_action = self.pause_menu.run()  
                if pause_action == "resume":
                    self.state = "play"  
                elif pause_action == "restart":
                    self.level = Level(self.levelNumbers[self.levelIndex], self.screen, type = self.levelTexts[self.levelIndex])  
                    self.state = "play"  
                elif pause_action == "home":
                    self.state = "menu"
            elif self.state == "complete":
                if (self.completed_menu.run() == "next"):
                    self.levelIndex = (self.levelIndex+1)%4
                    self.level = Level(self.levelNumbers[self.levelIndex], self.screen, type = self.levelTexts[self.levelIndex])  
                    self.state = "play"
                else:
                    self.state = self.completed_menu.run()
            elif self.state == "over":
                self.state = self.over_menu.run()
            elif self.state == "levelMap":
                level_number = self.levelMap.run()
                # print(level_number)
                if level_number == "level0":
                    self.levelIndex = 0
                    self.level = Level(self.levelNumbers[self.levelIndex], self.screen, type = self.levelTexts[self.levelIndex])  
                    self.state = "play"
                elif level_number == "level1":
                    self.levelIndex = 1
                    self.level = Level(self.levelNumbers[self.levelIndex], self.screen, type = self.levelTexts[self.levelIndex])    
                    self.state = "play"
                elif level_number == "level2":
                    self.levelIndex = 2
                    self.level = Level(self.levelNumbers[self.levelIndex], self.screen, type = self.levelTexts[self.levelIndex])   
                    self.state = "play"
                elif level_number == "level3":
                    self.levelIndex = 3
                    self.level = Level(self.levelNumbers[self.levelIndex], self.screen, type = self.levelTexts[self.levelIndex])  
                    self.state = "play"
                else:
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
                playState = self.level.updateState()
                if playState == "complete":
                    self.level = Level(self.levelNumbers[self.levelIndex], self.screen, type = self.levelTexts[self.levelIndex])  
                    self.state = "complete"
                    self.level.playState = None
                elif playState == "over":
                    self.level =  Level(self.levelNumbers[self.levelIndex], self.screen, type = self.levelTexts[self.levelIndex])  
                    self.state = "over"
                    self.level.playState = None
                pygame.display.flip()
                self.clock.tick(FPS)

if __name__ == '__main__':
    game = Game()
    game.run()
