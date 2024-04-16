import pygame
from settings import *
from debug import debug
from support import *

class Player(pygame.sprite.Sprite):
	def __init__(self,pos):
		super().__init__()
		self.import_character_assets()
		self.respawn = False
		self.respawn_timer = -1
		self.frame_index = 0 
		self.animation_speed = {
			'Boy':0.15,
			'Girl': 0.30
		}
		self.image = self.animations['Boy']['idle_right'][self.frame_index]
		# self.image.fill('black')
		self.rect = self.image.get_rect(topleft = (pos[0],pos[1]-55))
		self.direction = pygame.math.Vector2(0,0)
		self.gravity = {
			'Boy':0.3,
			'Girl':0.3
		}
		self.jump_speed = {'Boy':-7.7,'Girl': -8.8}
		self.idle_state = '_right'
		self.on_ground = True
		self.gender = "Girl"
		self.speed = {'Boy':5,"Girl":6}
		self.timer = pygame.time.get_ticks() 
		self.can_change = False
		self.status = 'idle_right' 
		self.jump()
		# self.mask = pygame.mask.from_surface(self.image)
  
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
			},
			'Smoke':[]
		}
		
		
		for gender in self.animations.keys():
			if gender =='Smoke':
				self.animations['Smoke'] = import_folder('./assets/Player/Death/Smoke')
				continue
			for animation in self.animations[gender].keys():
				if gender != 'Smoke':
					full_path = character_path + gender + '/' + animation
					self.animations[gender][animation] = import_folder(full_path)
                
				if gender == 'Boy' :
					for i, image in enumerate(self.animations[gender][animation]):
						scaled_image = pygame.transform.scale(image, (int(80*image.get_width()/image.get_height()), 80))
						self.animations[gender][animation][i] = scaled_image
				elif (gender == 'Girl'):
					for i, image in enumerate(self.animations[gender][animation]):
						scaled_image = pygame.transform.scale(image, (int(image.get_width() * 1.4), int(image.get_height() * 1.4)))
						self.animations[gender][animation][i] = scaled_image

	def get_input(self):
		keys = pygame.key.get_pressed()
		if self.gender =='Smoke':
			return
		if keys[pygame.K_SPACE] and (pygame.time.get_ticks() > self.timer +500) and (self.status == "idle_left" or self.status == "idle_right") and self.can_change:
			self.timer = pygame.time.get_ticks()
			if self.gender == 'Boy':
				self.gender = 'Girl'
			elif self.gender =='Girl':
				self.gender = 'Boy'

			if self.status == "run_left" or self.status == "run_right":
				self.rect.x += 1  
		
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
	
	
	def jump(self):
		if self.gender !='Smoke':
			if (self.status != 'jump_left') and (self.status != 'jump_right') and (self.status != 'fall_left') and (self.status != 'fall_right') and (self.direction.y ==0):
				self.on_ground = False
				self.direction.y = self.jump_speed[self.gender]
	def apply_gravity(self):
		if self.on_ground == False and self.gender !='Smoke':
			self.direction.y += self.gravity[self.gender] 

	def get_status(self):
		if self.gender !='Smoke':
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
		if self.gender !='Smoke':
			animations = self.animations[self.gender][self.status]
			self.frame_index += self.animation_speed[self.gender]
			if self.frame_index >= len(animations):
				self.frame_index = 0
			self.image = animations[int(self.frame_index)]
		else:
			self.frame_index += 0.1
			if self.frame_index >= len(self.animations[self.gender]):
				self.frame_index = 0
			self.image = self.animations[self.gender][int(self.frame_index)]
		
			
		# self.image.fill('black')
	
	def adjust_rect_for_gender(self):
		if self.gender == "Girl":
			self.rect.height = 42*1.4
			self.rect.width = 32
		elif self.gender == 'Boy':
			self.rect.height = 80
			self.rect.width = 40
	def dissappear(self):
		self.gender = 'Smoke'
		self.direction.x =0
		self.direction.y =0
		self.respawn_timer = pygame.time.get_ticks()
	def update(self):
		if (self.respawn_timer != -1) and (pygame.time.get_ticks() -self.respawn_timer >=1000):
			self.respawn = True
		self.get_input()
		self.get_status()
		# debug(self.can_change)
		self.animate()
		self.adjust_rect_for_gender()

	# def draw(self, surface):
	# 	surface.blit(self.image, self.rect)

	# def draw_mask(self, surface):
	# 	self.mask = pygame.mask.from_surface(self.image)
	# 	surface.blit(self.mask.to_surface(), self.rect)

	# def handle_collision(self, sprite):
    #     # Check for collision
	# 	if pygame.sprite.collide_mask(self, sprite):
    #         # Calculate the overlap area
	# 		overlap_area = self.mask.overlap_area(sprite.mask, (sprite.rect.x - self.rect.x, sprite.rect.y - self.rect.y))

    #         # If there is an overlap, handle collision
	# 		if overlap_area > 0:
	# 			offset_x = (self.rect.x + self.rect.width / 2) - (sprite.rect.x + sprite.rect.width / 2)
	# 			offset_y = (self.rect.y + self.rect.height / 2) - (sprite.rect.y + sprite.rect.height / 2)

    #             # Adjust player's position with the calculated offset
	# 			# self.rect.x += offset_x
	# 			# self.rect.y += offset_y
	# 			if abs(offset_x) > abs(offset_y):
	# 				self.rect.x += offset_x
	# 			else:
	# 				self.rect.y += offset_y
	
                