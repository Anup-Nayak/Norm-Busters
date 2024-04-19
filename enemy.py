import pygame
from settings import *
from debug import debug
from support import *

class Enemy(pygame.sprite.Sprite):
	def __init__(self,pos):
		super().__init__()
		self.import_character_assets()
		self.frame_index = 0 
		self.animation_speed = 0.30
		# print(self.animations['idle_right'])
		self.image = self.animations['idle_right'][0]
		# print(self.animations['idle_right'])
		self.rect = self.image.get_rect(topleft = (pos[0],pos[1]-50))
		self.direction = pygame.math.Vector2(0,0)
		self.gravity = 0.3
		self.jump_speed = 0
		self.idle_state = '_right'
		self.on_ground = True
		self.speed = 7
		self.timer = pygame.time.get_ticks() 
		self.can_change = False
		self.status = 'idle_right' 
		self.jump()
  
	def import_character_assets(self):
		character_path = './assets/Player/Enemy1'
		self.animations = {
			'idle_left': [],
			'idle_right': [],
			'run_left': [],
			'run_right': [],
			'fall_left':[],
			'fall_right':[],
			'jump_left':[],
			'jump_right':[]	
		}
		
		for animation in self.animations.keys():
			full_path = character_path + '/' + animation
			# print(full_path)
			self.animations[animation] = import_folder(full_path)
			# for i,image in enumerate(self.animations[animation]):
			# 	scaled_image = pygame.transform.scale(image, (int(80*image.get_width()/image.get_height()), 80))
			# 	self.animations[animation] = scaled_image
		# print(self.animations)
			
	
	def get_input(self):
		keys = pygame.key.get_pressed()

		if self.status != 'jump_right': 
			self.direction.x = self.speed
			self.idle_state = '_right'
		
	
	def jump(self):
		if (self.status != 'jump_left') and (self.status != 'jump_right') and (self.status != 'fall_left') and (self.status != 'fall_right') and (self.direction.y ==0):
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
		animations = self.animations[self.status]
		self.frame_index += self.animation_speed
		if self.frame_index >= len(animations):
			self.frame_index = 0
		# print(animations)
		self.image = animations[int(self.frame_index)]
		self.rect.height = 70
		self.rect.width = 50
	
	def update(self):
		# print(self.rect)
		self.get_input()
		self.get_status()
		debug(self.rect)
		self.animate()	
                