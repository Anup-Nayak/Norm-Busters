import pygame,sys
from settings import *
from level import Level
from game_data import level_0


class Game:
	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode((WIDTH,HEIGHT),pygame.SRCALPHA)
		self.clock = pygame.time.Clock()
		self.level = Level(level_0,self.screen)	
	def run(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()

			self.screen.fill((255, 255, 255, 255))
			self.level.run()
			pygame.display.flip()
			self.clock.tick(FPS)	
if __name__ == '__main__':
	game = Game()
	game.run() 