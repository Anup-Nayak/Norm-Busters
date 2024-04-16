
from settings import *
from support import *
from debug import *
import pygame
WHITE = (255, 255, 255,255)

class Tile(pygame.sprite.Sprite):
	def __init__(self,size,x,y):
		super().__init__()
		self.image = pygame.Surface((size,size), pygame.SRCALPHA)
		# self.mask = self.mask = pygame.mask.from_surface(self.image)
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
		



class MovingTile(Tile):
	def __init__(self,size,x,y,surface):
		super().__init__(size,x,y)
		self.image = (surface).convert_alpha()
		self.rect = self.image.get_rect(topleft = (x,y))
	def update(self):
		self.rect.x +=1

class HomeTile(Tile):
	def __init__(self,size,x,y):
		super().__init__(size,x,y)
		self.animation_speed =0
		self.index = 3
		self.path = './assets/Exit/Door/'
		self.import_assets()

	def import_assets(self):
		self.animations = import_folder(self.path)
		# print(self.animations)
	def animate(self):
		self.index  +=self.animation_speed
		if(self.index >=len(self.animations)):
			self.index =0
		self.image = self.animations[int(self.index)]
	def update(self):
		# self.image = self.animations[0].convert_alpha()
		self.animate()

class SpikeTile(Tile):
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


class AnimatedTile(Tile):
	def __init__(self,size,x,y,path,speed =0.1):
		super().__init__(size,x,y)
		self.animation_speed =speed
		self.index = 0
		self.path = path
		self.import_assets()
	def import_assets(self):
		# slef.path = './assets/Diamond/Coins/'
		self.animations = []
		self.animations = import_folder(self.path)
		# print(self.animations)
	def animate(self):
		self.index  +=self.animation_speed
		if(self.index >=len(self.animations)):
			self.index =0
		self.image = self.animations[int(self.index)]
	def update(self):
		# self.image = self.animations[0].convert_alpha()
		self.animate()
  
  
class MovingTile(Tile):
    def __init__(self, size, x, y, surface, speed=1, direction='horizontal'):
        super().__init__(size, x, y)
        self.surface = surface
        self.image = surface.convert_alpha()
        self.rect = self.image.get_rect(topleft =(x,y))
        self.speed = speed
        self.direction = direction

    def update(self):
        debug(self.rect.x)
        if self.direction == 'horizontal':
            self.rect.x += self.speed
        elif self.direction == 'vertical':
            self.rect.y += self.speed
        # self.image = self.surface
		