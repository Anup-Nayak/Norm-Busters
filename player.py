import pygame
from settings import *
from debug import debug
from support import *

class Player(pygame.sprite.Sprite):
	def __init__(self,pos):
		super().__init__()
		self.import_character_assets()
		self.frame_index =0 
		self.animation_speed = 0.15
		# self.image = pygame.image.load('D:/Abhishek_Folder/Coding/Game Dev/COP1/assets/Player/Run/Run1G.png')
		self.image = self.animations['idle_right'][self.frame_index]
		# self.image.fill('black')
		self.rect = self.image.get_rect(topleft = (pos[0],pos[1]-30))
		self.direction = pygame.math.Vector2(0,0)
		self.gravity = 0.3
		self.jump_speed = -7
		self.idle_state = '_right'
		self.on_ground = True
	def import_character_assets(self):
		character_path = 'D:/Abhishek_Folder/Coding/Game Dev/COP1/assets/Player/'
		self.animations = {
			'idle_left': ['1F.png'],
			'idle_right': ['1F.png'],
			'run_left': ['Run1G.png','Run2G.png','Run3G.png','Run4G.png','Run5G.png','Run6G.png'],
			'run_right': ['Run1G.png','Run2G.png','Run3G.png','Run4G.png','Run5G.png','Run6G.png'],
			'fall_left':['1F.png'],
			'fall_right':['1F.png'],
			'jump_left':['1F.png'],
			'jump_right':['1F.png']
		}
		for animation in (self.animations.keys()):
			full_path = character_path + animation
			self.animations[animation] = import_folder(full_path)

	def get_input(self):
		keys = pygame.key.get_pressed()

		# if keys[pygame.K_UP]:
		# 	self.direction.y = -5
		# 	self.start = pygame.time.get_ticks()
		# elif keys[pygame.K_DOWN]:
		# 	self.direction.y = +5
		# else:
			# self.direction.y = 0
		if keys[pygame.K_RIGHT]:
			self.direction.x = 4
			self.idle_state = '_right'
		elif keys[pygame.K_LEFT]:
			self.direction.x = -4
			self.idle_state = '_left'
		else:
			self.direction.x = 0
		if keys[pygame.K_UP]:
			self.jump()
	
	def jump(self):
		if (self.status != 'jump_left') and (self.status != 'jump_right') :
			self.on_ground = False
			self.direction.y = self.jump_speed
	def apply_gravity(self):
		if self.on_ground == False:
			self.direction.y += self.gravity 

	def get_status(self):
		if self.direction.y < 0:
			if self.direction.x >=0:
				self.status = 'jump'+self.idle_state
			else:
				self.status = 'jump'+self.idle_state
		
		elif self.direction.y > 0:
			if self.direction.x >= 0:
				self.status = 'fall'+self.idle_state
			else:
				self.status = 'fall'+self.idle_state
		elif self.direction.x > 0:
			self.status = 'run_left'
		elif self.direction.x < 0 :
			self.status = 'run_right'
		else:
			self.status = 'idle'+self.idle_state
	def animate(self):
		animations = self.animations[self.status]
		self.frame_index += self.animation_speed
		if self.frame_index >= len(animations):
			self.frame_index = 0
		self.image = animations[int(self.frame_index)]
	def update(self):
		# debug(self.rect.x)
		self.get_input()
		# self.apply_gravity()
		self.get_status()
		debug(self.rect.y)
		self.animate()