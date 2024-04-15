import pygame
WHITE = (255, 255, 255,255)

class Tile(pygame.sprite.Sprite):
	def __init__(self,size,x,y):
		super().__init__()
		self.image = pygame.Surface((size,size), pygame.SRCALPHA)
		self.mask = self.mask = pygame.mask.from_surface(self.image)
		# self.image.fill(WHITE) 
		self.rect = self.image.get_rect(topleft = (x,y))
	def set_image(self,surface):
		self.image = surface.convert_alpha()

		for x in range(self.image.get_width()):
			for y in range(self.image.get_height()):
				r, g, b, a = self.image.get_at((x, y))
				if r >= 150 or g >= 150 or b >= 150:
					self.image.set_at((x, y), (0, 0, 0, 0))
	def set_image1(self,surface):
		self.image = surface.convert_alpha()

		for x in range(self.image.get_width()):
			for y in range(self.image.get_height()):
				r, g, b, _ = self.image.get_at((x, y))
				if r <= 1 and g <= 1 and b <= 1:
					self.image.set_at((x, y), (0, 0, 0, 0))  # Set pixel to transparent
	# def draw_mask(self, surface):
	# 	# self.mask = pygame.mask.from_surface(self.image)
	# 	surface.blit(self.mask.to_surface(), self.rect)



class StaticTile(Tile):
	def __init__(self,size,x,y,surface):
		super().__init__(size,x,y)
		self.image = (surface).convert_alpha()

class OutlineTile(Tile):
	def __init__(self,size,x,y,surface):
		super().__init__(size,x,y)
		self.set_image(surface)
		
class HomeTile(Tile):
	def __init__(self,size,x,y,surface):
		super().__init__(size,x,y)
		self.set_image1(surface)


class Platform_Anim(Tile):
	def __init__(self,size,x,y,surface):
		super().__init__(size,x,y)
		self.image = surface.convert_alpha()

		for x in range(self.image.get_width()):
			for y in range(self.image.get_height()):
				r, g, b, _ = self.image.get_at((x, y))
				if r <= 10 and g <= 10 and b <= 10:
					self.image.set_at((x, y), (0, 0, 0, 0))