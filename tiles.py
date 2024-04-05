import pygame
WHITE = (255, 255, 255,255)

class Tile(pygame.sprite.Sprite):
	def __init__(self,size,x,y):
		super().__init__()
		self.image = pygame.Surface((size,size), pygame.SRCALPHA)
		# self.image.fill(WHITE) 
		self.rect = self.image.get_rect(topleft = (x,y))
	def set_image(self,surface):
		self.image = surface.convert_alpha()

		for x in range(self.image.get_width()):
			for y in range(self.image.get_height()):
				r, g, b, a = self.image.get_at((x, y))
				if r >= 150 or g >= 150 or b >= 150:
					self.image.set_at((x, y), (0, 0, 0, 0))  # Set pixel to transparent


class StaticTile(Tile):
	def __init__(self,size,x,y,surface):
		super().__init__(size,x,y)
		self.image = (surface).convert_alpha()

class OutlineTile(Tile):
	def __init__(self,size,x,y,surface):
		super().__init__(size,x,y)
		self.set_image(surface)
		

