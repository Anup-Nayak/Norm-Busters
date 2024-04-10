import pygame
from support import import_csv_layout,import_cut_graphic
from settings import TILESIZE
from tiles import Tile,StaticTile,OutlineTile
from player import Player
from debug import debug

class Level:
	def __init__(self,level_data,surface):
		self.display_surface = surface
		bg_layout =	import_csv_layout(level_data['background'])
		self.bg = self.create_tile_group(bg_layout,'background')


		floor_layout = import_csv_layout(level_data['boundary'])
		self.boundary = self.create_tile_group(floor_layout,'boundary')

		level_layout =	import_csv_layout(level_data['level'])
		self.level = self.create_tile_group(level_layout,'level')
  
		platform_layout =	import_csv_layout(level_data['platform'])
		self.platform = self.create_tile_group(platform_layout,'platform')
  
		# outline_layout = import_csv_layout(level_data['Outline'])
		# self.outline = self.create_tile_group(outline_layout,'outline')

		# slant_tiles1_layout = import_csv_layout(level_data['Slant_Tiles1'])
		# self.slant_tiles1_layout = self.create_tile_group(slant_tiles1_layout,'slant_tiles1')

		
		# slant_tiles2_layout = import_csv_layout(level_data['Slant_Tiles2'])
		# self.slant_tiles2_layout = self.create_tile_group(slant_tiles1_layout,'slant_tiles2')

		player_layout = import_csv_layout(level_data['Player'])
		self.player = pygame.sprite.GroupSingle()
		self.player_setup(player_layout)
		# print(bg_layout)

	def create_tile_group(self,layout,type):
		if type == 'background'  :
			bg_tile_list = import_cut_graphic('./assets/Tiled/TileMap9.png')
		elif type == 'boundary' or type == 'slant_tiles1' or type == 'level' :
			floor_tile_list = import_cut_graphic('./assets/Tiled/TileMap8.png')
		elif type == 'platform':
			platform_tile_list = import_cut_graphic('./assets/Tiled/TileMap10.png')
			
		# elif type == 'outline':
		# 	outline_tile_list = import_cut_graphic('./assets/Tiled/TileMap10.png')
		# elif type== 'slant_tiles2':
		# 	bottom_left_slant_list = import_cut_graphic('D:/Abhishek_Folder/Coding/Game Dev/COP1/assets/Tiled/TileMap8.png')
		sprite_group = pygame.sprite.Group()
		for row_index,row in enumerate(layout):
			for col_index,val in enumerate(row):
				if val !='-1':
					x = col_index*TILESIZE
					y = row_index*TILESIZE
					if type == 'background':
						# print(val)
						tile_surface = bg_tile_list[int(val)].convert_alpha()
						sprite = StaticTile(TILESIZE,x,y,tile_surface)
						sprite_group.add(sprite)
					if type =='boundary' or type == 'level':
						# print(val)
						tile_surface = floor_tile_list[int(val)].convert_alpha()
						sprite = StaticTile(TILESIZE,x,y,tile_surface)
						sprite_group.add(sprite)
					if type =='platform':
						# print(val)
						tile_surface = platform_tile_list[int(val)].convert_alpha()
						sprite = StaticTile(TILESIZE,x,y,tile_surface)
						sprite_group.add(sprite)
					# if type == 'outline':
					# 	tile_surface = outline_tile_list[int(val)].convert_alpha()
					# 	sprite = OutlineTile(TILESIZE,x,y,tile_surface)
					# 	sprite_group.add(sprite)
					# if type == 'slant_tiles1':
					# 	tile_surface = floor_tile_list[int(val)].convert_alpha()
					# 	sprite = StaticTile(TILESIZE,x,y,tile_surface)
					# 	sprite_group.add(sprite)
					# if type == 'slant_tiles2':
					# 	tile_surface = f_tile_list[int(val)].convert_alpha()
					# 	sprite = StaticTile(TILESIZE,x,y,tile_surface)
					# 	sprite_group.add(sprite)
					
		return sprite_group
	def player_setup(self,layout):
		for row_index,row in enumerate(layout):
			for col_index,val in enumerate(row):
				if val != -1:
					x = col_index*TILESIZE
					y = row_index*TILESIZE
					if val == '0':
						sprite  = Player((x,y))
						self.player.add(sprite)
						# print('player goes here')
	def horizontal_collision(self):
		player = self.player.sprite
		player.rect.x += player.direction.x

		# Check collision with outline tiles
		for sprite in self.boundary.sprites() or self.platform.sprites():
			if sprite.rect.colliderect(player.rect):
				if player.rect.right > sprite.rect.left and player.direction.x > 0:
					player.rect.right = sprite.rect.left
					# Handle left collision here

				# Check collision from right side
				elif player.rect.left < sprite.rect.right and player.direction.x < 0:
					player.rect.left = sprite.rect.right
					# Handle right collision here

		# self.detect_top_left_slant_collision()
	def vertical_collision(self):
		player = self.player.sprite
		player.rect.y += player.direction.y
		player.apply_gravity()
		# Check collision with outline tiles
		for sprite in self.boundary.sprites() :
			if sprite.rect.colliderect(player.rect):
				# Check collision from above
				if player.rect.bottom > sprite.rect.top and player.direction.y > 0:
					player.rect.bottom = sprite.rect.top
					player.direction.y = 0
                    			
					# Handle downward collision here

				# Check collision from below
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
					# Handle downward collision here

				# Check collision from below
				elif player.rect.top < sprite.rect.bottom and player.direction.y < 0:
					player.rect.top = sprite.rect.bottom
					player.direction.y = -0.5*player.direction.y
			else:
				player.can_change = False
        
					# Handle upward collision here
		# self.detect_top_left_slant_collision()
	# def detect_top_left_slant_collision(self):
	# 	player = self.player.sprite
	# 	for sprite in self.slant_tiles1_layout.sprites():
	# 		constant = sprite.rect.topleft[1] - sprite.rect.topleft[0]
	# 		player_top_left = player.rect.topleft
	# 		player_top_right = player.rect.topright

	# 		if (player_top_right[1] <= player_top_right[0] + constant and
    #                 (player.direction.y +player.direction.x)>= 0) and (player_top_right[0]<= sprite.rect.topright[0]) and (player_top_right[1] >= sprite.rect.topright[1]):  # Check player's component in the direction of slant is positive
	# 				# print(1)
	# 				debug([player_top_right,sprite.rect.topright])
    #             # Adjust player's top-right corner to be on the boundary
	# 				player_top_right = (player_top_right[0], player_top_right[0] + constant)
	# 				player.rect.topright = player_top_right

                # Resolve collision based on tile's slant angle and player direction
				# player.resolve_top_left_slant_collision(tile.angle)
	# def detect_bottom_left_slant_collision(self):
	# 	player = self.player.sprite
	# 	for sprite in self.slant_tiles1_layout.sprites():
			
	
	def run(self):
		self.display_surface.fill((255,255,255,255))
		self.bg.draw(self.display_surface)
		self.boundary.draw(self.display_surface)
		self.level.draw(self.display_surface)
		self.platform.draw(self.display_surface)
  		
  
		# self.outline.draw(self.display_surface)	
		# self.slant_tiles1_layout.draw(self.display_surface)
		self.player.update()

		self.horizontal_collision()
		self.vertical_collision()
		# self.detect_top_left_slant_collision()
		self.player.draw(self.display_surface)
		pygame.display.flip()