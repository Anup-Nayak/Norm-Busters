import pygame
from support import import_csv_layout,import_cut_graphic
from settings import TILESIZE
from tiles import *
from player import Player
from debug import debug
from enemy import *

class Level:
	
	def __init__(self,level_data,surface):
		self.coins = 0
		self.lives = 3
		
		self.heart = pygame.sprite.Group()
		self.display_lives()
		self.display_surface = surface
		bg_layout =	import_csv_layout(level_data['background'])
		self.bg = self.create_tile_group(bg_layout,'background')

		floor_layout = import_csv_layout(level_data['boundary'])
		self.boundary = self.create_tile_group(floor_layout,'boundary')

		level_layout =	import_csv_layout(level_data['level'])
		self.level = self.create_tile_group(level_layout,'level')
  
		platform_layout = import_csv_layout(level_data['platform'])
		self.platform = self.create_tile_group(platform_layout,'platform')

		home_layout =	import_csv_layout(level_data['home'])
		self.home = self.create_tile_group(home_layout,'home')

		platform_anim = import_csv_layout(level_data['Platform_Anim'])
		self.platform_anim = self.create_tile_group(platform_anim,'platform_anim')

		spikes_layout = import_csv_layout(level_data['Spikes'])
		self.spikes = self.create_tile_group(spikes_layout,'spikes')

		movingTiles_layout = import_csv_layout(level_data['movingTiles'])
		self.movingTiles = self.create_tile_group(movingTiles_layout,'movingTiles')

		rewards_layout = import_csv_layout(level_data['rewards'])
		self.rewards = self.create_tile_group(rewards_layout,'rewards')
		self.player = pygame.sprite.GroupSingle()
		self.player_setup()

		# self.enemy = pygame.sprite.GroupSingle()
		# self.enemy_setup()

	def create_tile_group(self,layout,type):
		if type == 'background'  :
			bg_tile_list = import_cut_graphic('./assets/Tiled/TileMap9.png')
		elif type == 'boundary' or type == 'slant_tiles1' or type == 'level' :
			floor_tile_list = import_cut_graphic('./assets/Tiled/TileMap8.png')
		elif type == 'platform':
			platform_tile_list = import_cut_graphic('./assets/Tiled/TileMap8.png')
		elif type == 'spikes':
			spike_tile_list = import_cut_graphic('./assets/Spikes/spikeF.png')
		elif type == 'rewards':
			reward_tile_list = import_cut_graphic('./assets/Spikes/spikeF.png')
		elif type =='platform_anim':
			platform_anim_tile_list = import_cut_graphic('./assets/Platform/Cf.png')
		elif type == 'movingTiles':
			movingTiles_list = import_cut_graphic('./assets/Tiled/TileMap8.png')
		sprite_group = pygame.sprite.Group()
		for row_index,row in enumerate(layout):
			for col_index,val in enumerate(row):
				if val !='-1':
					x = col_index*TILESIZE
					y = row_index*TILESIZE
					if type == 'background':
						
						tile_surface = bg_tile_list[int(val)].convert_alpha()
						sprite = StaticTile(TILESIZE,x,y,tile_surface)
						sprite_group.add(sprite)
      
					elif type =='boundary' or type == 'level':
					
						tile_surface = floor_tile_list[int(val)].convert_alpha()
						sprite = StaticTile(TILESIZE,x,y,tile_surface)
						sprite_group.add(sprite)
      
					elif type =='platform':
						
						tile_surface = platform_tile_list[int(val)].convert_alpha()
						sprite = StaticTile(TILESIZE,x,y,tile_surface)
						sprite_group.add(sprite)
      
					elif type =='home':
						
						# tile_surface = home_tile_list[int(val)].convert_alpha()
						sprite = HomeTile(TILESIZE,x,y)
						sprite_group.add(sprite)

					elif type == 'platform_anim':

						tile_surface = platform_anim_tile_list[int(val)].convert_alpha()
						sprite = Platform_Anim(TILESIZE,x,y,tile_surface)
						sprite_group.add(sprite)
      
					elif type == 'spikes':

						tile_surface = spike_tile_list[int(val)].convert_alpha()
						sprite = SpikeTile(TILESIZE,x,y,tile_surface)
						sprite_group.add(sprite)
      
					elif type == 'rewards':

						tile_surface = reward_tile_list[0].convert_alpha()
						sprite = AnimatedTile(TILESIZE,x,y,'./assets/Diamond/Coins/',speed = 0.1)
						sprite_group.add(sprite)
					
					elif type == 'movingTiles':

						tile_surface = movingTiles_list[0].convert_alpha()
						sprite = MovingTile(TILESIZE,x,y,tile_surface)
						sprite_group.add(sprite)
					
		return sprite_group

	def player_setup(self):
		sprite  = Player((150,650))
		self.player.add(sprite)
	
	def horizontal_collision(self):
		player = self.player.sprite
		player.rect.x += player.direction.x

		for sprite in self.boundary.sprites():
			if sprite.rect.colliderect(player.rect):
				player.can_change = False
				if player.rect.right > sprite.rect.left and player.direction.x > 0:
					player.rect.right = sprite.rect.left

				
				elif player.rect.left < sprite.rect.right and player.direction.x < 0:
					player.rect.left = sprite.rect.right
		
		for sprite in self.spikes.sprites():
			if sprite.rect.colliderect(player.rect):
				player.can_change = False
				# self.display_lives()
				if player.rect.right > sprite.rect.left and player.direction.x > 0:
					player.rect.right = sprite.rect.left

				
				elif player.rect.left < sprite.rect.right and player.direction.x < 0:
					player.rect.left = sprite.rect.right
				self.lives -=1
				if player.gender !='Smoke':
					for sprite in self.player:
						sprite.dissappear()
						self.remove_lives()
				# pygame.quit()
    
		for sprite in self.home.sprites():
			if sprite.rect.colliderect(player.rect):
				player.can_change = False
				if player.rect.right > sprite.rect.left and player.direction.x > 0:
					player.rect.right = sprite.rect.left

				
				elif player.rect.left < sprite.rect.right and player.direction.x < 0:
					player.rect.left = sprite.rect.right

				# pygame.quit()
		
		for sprite in self.rewards.sprites():
			if sprite.rect.colliderect(player.rect):
				player.can_change = False
				if player.rect.right > sprite.rect.left and player.direction.x > 0:
					player.rect.right = sprite.rect.left

				
				elif player.rect.left < sprite.rect.right and player.direction.x < 0:
					player.rect.left = sprite.rect.right

				self.rewards.remove(sprite)
				self.coins += 1
				
	def vertical_collision(self):
		player = self.player.sprite
		player.rect.y += player.direction.y
		player.apply_gravity()
		# Check collision with outline tiles
		for sprite in self.boundary.sprites() :
			if sprite.rect.colliderect(player.rect):
				player.can_change = False
				
				if player.rect.bottom > sprite.rect.top and player.direction.y > 0:
					player.rect.bottom = sprite.rect.top
					player.direction.y = 0
                    			
					

				elif player.rect.top < sprite.rect.bottom and player.direction.y < 0:
					player.rect.top = sprite.rect.bottom
					player.direction.y = -0.5*player.direction.y
					
		
  
		for sprite in self.platform.sprites() :
			
			if sprite.rect.colliderect(player.rect):
				# Check collision from above
				if player.rect.bottom > sprite.rect.top and player.direction.y >= 0:
					player.rect.bottom = sprite.rect.top
					player.direction.y = 0
					player.can_change = True

				
				elif player.rect.top < sprite.rect.bottom and player.direction.y < 0:
					player.rect.top = sprite.rect.bottom
					player.direction.y = -0.5*player.direction.y
			
        
		for sprite in self.spikes.sprites():
			
			if sprite.rect.colliderect(player.rect):
				player.can_change = False
				
				if player.rect.bottom > sprite.rect.top and player.direction.y > 0:
					player.rect.bottom = sprite.rect.top
					player.direction.y = 0
                    			
					

				elif player.rect.top < sprite.rect.bottom and player.direction.y < 0:
					player.rect.top = sprite.rect.bottom
					player.direction.y = -0.5*player.direction.y
				self.lives -=1
				
				if player.gender !='Smoke':
					for sprite in self.player:
						sprite.dissappear()
						self.remove_lives()
				# self.display_lives()
    
		for sprite in self.home.sprites():
			
			if sprite.rect.colliderect(player.rect):
				player.can_change = False
				
				if player.rect.bottom > sprite.rect.top and player.direction.y > 0:
					player.rect.bottom = sprite.rect.top
					player.direction.y = 0
                    			
					

				elif player.rect.top < sprite.rect.bottom and player.direction.y < 0:
					player.rect.top = sprite.rect.bottom
					player.direction.y = -0.5*player.direction.y
				
		for sprite in self.rewards.sprites():
			
			if sprite.rect.colliderect(player.rect):
				player.can_change = False
				
				if player.rect.bottom > sprite.rect.top and player.direction.y > 0:
					player.rect.bottom = sprite.rect.top
					player.direction.y = 0
                    			
					

				elif player.rect.top < sprite.rect.bottom and player.direction.y < 0:
					player.rect.top = sprite.rect.bottom
					player.direction.y = -0.5*player.direction.y
				self.rewards.remove(sprite)
				self.coins += 1
	
	def remove_lives(self):
		# if(self.lives>=0):
		sprite_list =self.heart.sprites()
		if sprite_list:
			last_sprite = sprite_list[-1]
			self.heart.remove(last_sprite)

	def display_lives(self):
		if(self.lives>=0):
			for i in range(self.lives):
				self.heart.add(AnimatedTile(TILESIZE,900-25*i,35,'./assets/Lifes/Health',speed=0))
		
		
	def update_life(self):
		for sprite in self.heart:
			sprite.update()
	def respawn(self):
		if self.player.sprite.respawn == True:
			self.player.empty()
			self.player = pygame.sprite.GroupSingle()
			self.player_setup()
	
	
	def run(self):
		self.display_surface.fill((255,255,255,255))
		self.bg.draw(self.display_surface)
		self.boundary.draw(self.display_surface)
		
		self.update_life()
		self.heart.draw(self.display_surface)
		self.level.draw(self.display_surface)
		self.platform.draw(self.display_surface)
		self.home.draw(self.display_surface)
		self.platform_anim.draw(self.display_surface)
		self.spikes.draw(self.display_surface)
		self.rewards.draw(self.display_surface)
		self.movingTiles.draw(self.display_surface)
		# self.movingTiles.update()
		
  
		for sprite in self.home:
			sprite.update()

		for sprite in self.movingTiles:
			sprite.update()
			

		self.horizontal_collision()
		self.vertical_collision()
		# self.detect_top_left_slant_collision()
		if self.player:
			self.player.draw(self.display_surface)
		
		for sprite in self.rewards:
			sprite.update()
		self.respawn()
		
		# for sprite in self.player:
		# 	sprite.draw_mask(self.display_surface)
		if self.player: 
			self.player.update()
		pygame.display.flip()

		# debug(self.coins)