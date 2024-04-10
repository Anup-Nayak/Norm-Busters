import pygame
from settings import *
from debug import debug
from support import *

class Player(pygame.sprite.Sprite):
	def __init__(self,pos):
		super().__init__()
		self.import_character_assets()
		self.frame_index = 0 
		self.animation_speed = 0.15
		self.image = self.animations['Boy']['idle_right'][self.frame_index]
		self.rect = self.image.get_rect(topleft = (pos[0],pos[1]-30))
		self.direction = pygame.math.Vector2(0,0)
		self.gravity = 0.3
		self.jump_speed = {'Boy':-7,'Girl': -8}
		self.idle_state = '_right'
		self.on_ground = True
		self.gender = "Girl"
		self.speed = {'Boy':4,"Girl":5}
	def import_character_assets(self):
		character_path = './assets/Player/'
		self.animations = {
			'Boy':{
			'idle_left': ['1F.png'],
			'idle_right': ['1F.png'],
			'run_left': ['Run1G.png','Run2G.png','Run3G.png','Run4G.png','Run5G.png','Run6G.png'],
			'run_right': ['Run1G.png','Run2G.png','Run3G.png','Run4G.png','Run5G.png','Run6G.png'],
			'fall_left':['1F.png'],
			'fall_right':['1F.png'],
			'jump_left':['1F.png'],
			'jump_right':['1F.png']
			},
			'Girl':{
			'idle_left': ['1F.png'],
			'idle_right': ['1F.png'],
			'run_left': ['Run1G.png','Run2G.png','Run3G.png','Run4G.png','Run5G.png','Run6G.png'],
			'run_right': ['Run1G.png','Run2G.png','Run3G.png','Run4G.png','Run5G.png','Run6G.png'],
			'fall_left':['1F.png'],
			'fall_right':['1F.png'],
			'jump_left':['1F.png'],
			'jump_right':['1F.png']
			}
		}
		
		for animation in (self.animations['Boy'].keys()):
			full_path = character_path +'Boy/'+ animation
			self.animations['Boy'][animation] = import_folder(full_path)
		for animation in(self.animations['Girl'].keys()):
			full_path = character_path+'Girl/'+animation
			self.animations['Girl'][animation] = import_folder(full_path)

	def get_input(self):
		keys = pygame.key.get_pressed()

		if keys[pygame.K_RIGHT]:
			self.direction.x = self.speed[self.gender]
			self.idle_state = '_right'
		elif keys[pygame.K_LEFT]:
			self.direction.x = -1*self.speed[self.gender]
			self.idle_state = '_left'
		else:
			self.direction.x = 0
		if keys[pygame.K_UP]:
			self.jump()
	
		if keys[pygame.K_SPACE]:
			if self.gender == 'Boy':
				self.gender = 'Girl'
			else:
				self.gender = 'Boy'
	
	def jump(self):
		# if (self.status != 'jump_left') and (self.status != 'jump_right') and (self.status != 'fall_left') and (self.status != 'fall_right') and (self.direction.y ==0):
		self.on_ground = False
		self.direction.y = self.jump_speed[self.gender]
	def apply_gravity(self):
		if self.on_ground == False:
			self.direction.y += self.gravity 

	def get_status(self):
		if self.direction.y < 0:
			if self.direction.x >=0:
				self.status = 'jump'+self.idle_state
			else:
				self.status = 'jump'+self.idle_state
		
		elif self.direction.y > 1:
			if self.direction.x >= 0:
				self.status = 'fall'+self.idle_state
			else:
				self.status = 'fall'+self.idle_state
		elif self.direction.x > 0:
			self.status = 'run_right'
		elif self.direction.x < 0 :
			self.status = 'run_left'
		else:
			self.status = 'idle'+self.idle_state
	def animate(self):
		animations = self.animations[self.gender][self.status]
		self.frame_index += self.animation_speed
		if self.frame_index >= len(animations):
			self.frame_index = 0
		self.image = animations[int(self.frame_index)]
	
	def adjust_rect_for_gender(self):
		if self.gender == "Girl":
			self.rect.height = 42
		else:
			self.rect.height = 53
		 
	def update(self):
		self.get_input()
		self.get_status()
		debug(self.rect)
		self.animate()
		self.adjust_rect_for_gender()