import pygame
from support import import_csv_layout,import_cut_graphic
from settings import TILESIZE
from tiles import *
from player import Player
from debug import debug
from enemy import *

class Level:
    
    def __init__(self,level_data,surface,type):
        self.coins = 0
        self.lives = 3
        self.type = type
        self.heart = pygame.sprite.Group()
        self.display_lives()
        self.display_surface = surface
        self.playState = None

        self.background_image = pygame.image.load("./assets/bg/bg8.png").convert()
        # bg_layout =	import_csv_layout(level_data['background'])
        # self.bg = self.create_tile_group(bg_layout,'background')

        floor_layout = import_csv_layout(level_data['boundary'])
        self.boundary = self.create_tile_group(floor_layout,'boundary')
        
        # level_layout =	import_csv_layout(level_data['level'])
        # self.level = self.create_tile_group(level_layout,'level')
  
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

        movable_blocks = import_csv_layout(level_data['Movable block'])
        # print(movable_blocks)
        self.movable_blocks = self.create_tile_group(movable_blocks,'Movable Block') 
        
        wheel_layout = import_csv_layout(level_data['Wheel'])
        self.wheel = self.create_tile_group(wheel_layout,'wheel')

        self.player = pygame.sprite.GroupSingle()
        self.player_setup()
        
        self.enemy = pygame.sprite.GroupSingle()
        self.enemy_spawn = False


    def draw_background(self, surface):
        surface.blit(self.background_image, (0, 0))
    
    
    def create_tile_group(self,layout,type):
        # if type == 'background'  :
        # 	bg_tile_list = import_cut_graphic('./assets/Tiled/TileMap9.png')
        if type == 'boundary' or type == 'slant_tiles1' or type == 'level' or type == 'Movable Block' :
            floor_tile_list = import_cut_graphic('./assets/Tiled/TileMap2.png')
        elif type == 'platform':
            platform_tile_list = import_cut_graphic('./assets/Tiled/TileMap2.png')
        elif type == 'spikes':
            spike_tile_list = import_cut_graphic('./assets/Spikes/spikeF.png')
        elif type == 'rewards':
            reward_tile_list = import_cut_graphic('./assets/Spikes/spikeF.png')
        elif type =='platform_anim':
            platform_anim_tile_list = import_cut_graphic('./assets/Platform/Cf.png')
        elif type == 'movingTiles':
            movingTiles_list = import_cut_graphic('./assets/Tiled/TileMap8.png')
        
        sprite_group = pygame.sprite.Group()
        # print(layout)
        for row_index,row in enumerate(layout):
            for col_index,val in enumerate(row):
                if val !='-1':
                    x = col_index*TILESIZE
                    y = row_index*TILESIZE
      
                    if type =='boundary':
                    
                        tile_surface = floor_tile_list[int(val)].convert_alpha()
                        sprite = SpikeTile(TILESIZE,x,y,tile_surface)
                        sprite_group.add(sprite)
      
                    elif type =='platform':
                        
                        tile_surface = platform_tile_list[int(val)].convert_alpha()
                        sprite = SpikeTile(TILESIZE,x,y,tile_surface)
                        sprite_group.add(sprite)
      
                    elif type =='home':
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

                    elif type == 'Movable Block':
                        # tile_surface =floor_tile_list[int(val)].convert_alpha()
                        sprite = MovableBlocks(TILESIZE,x,y)
                        sprite_group.add(sprite)
                    elif type == 'wheel':
                        # print(type)
                        sprite = Wheel(TILESIZE,x,y,'./assets/Spikes/Rotating/',speed = 0.1,)
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
        for sprite in self.wheel.sprites():
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
                self.playState = "complete"
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

        for sprite in self.movable_blocks.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.gender == 'Boy' and (self.type == 'Level 1' and sprite.rect.left>=170):
                    # print(sprite.rect.x)
                    player.can_change = False
                    if player.rect.right > sprite.rect.left and player.direction.x > 0:
                        sprite.rect.left = player.rect.right

                    
                    elif player.rect.left < sprite.rect.right and player.direction.x < 0:
                        sprite.rect.right = player.rect.left
                else:
                    if player.rect.right > sprite.rect.left and player.direction.x > 0:
                         player.rect.right = sprite.rect.left

                    
                    elif player.rect.left < sprite.rect.right and player.direction.x < 0:
                        player.rect.left = sprite.rect.right 

        
        if self.enemy:
            if self.enemy.sprite.rect.x >= player.rect.x  and (player.rect.y <= self.enemy.sprite.rect.y +70) and (player.rect.y >= self.enemy.sprite.rect.y-70) :
                
                self.lives -=1
                if player.gender !='Smoke':
                    for sprite in self.player:
                        sprite.dissappear()
                        self.remove_lives()
                        self.enemy.empty()
                        self.enemy_spawn = False
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
            #     player.can_change = False
                
            #     if player.rect.bottom > sprite.rect.top and player.direction.y > 0:
            #         player.rect.bottom = sprite.rect.top
            #         player.direction.y = 0
                                
                    

            #     elif player.rect.top < sprite.rect.bottom and player.direction.y < 0:
            #         player.rect.top = sprite.rect.bottom
            #         player.direction.y = -0.5*player.direction.y
                self.rewards.remove(sprite)
                self.coins += 1
        for sprite in self.movable_blocks.sprites():
            if sprite.rect.colliderect(player.rect):
                player.can_change = False
                if player.rect.bottom > sprite.rect.top and player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                            
                

                elif player.rect.top < sprite.rect.bottom and player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = -0.5*player.direction.y
                
                    
                    
        
    def enemy_setup(self):
        if self.type =='Level 0':
            sprite  = Enemy((self.player.sprite.rect.x-110,697))
        elif self.type =='Level 1':
            sprite = Enemy((self.player.sprite.rect.x-110,291)) 

        self.enemy_spawn = True
        self.enemy.add(sprite)
    
    def remove_lives(self):
        # if(self.lives>=0):
        sprite_list = self.heart.sprites()
        if sprite_list:
            last_sprite = sprite_list[-1]
            self.heart.remove(last_sprite)
        if self.lives == 0:
            self.playState = "over"
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
    


        
    def enemy_horizontal_collision(self):
        enemy = self.enemy.sprite
        # if enemy.rect.x >=760:
        # 	return
        if enemy.rect.x + enemy.direction.x >=760:
            self.enemy.empty()
            self.enemy_spawn = False
        else:
            enemy.rect.x += enemy.direction.x

        for sprite in self.boundary.sprites():
            if sprite.rect.colliderect(enemy.rect):
                enemy.can_change = False
                if enemy.rect.right > sprite.rect.left and enemy.direction.x > 0:
                    enemy.rect.right = sprite.rect.left
                    # enemy.speed = 0

                
                elif enemy.rect.left < sprite.rect.right and enemy.direction.x < 0:
                    enemy.rect.left = sprite.rect.right
        
        for sprite in self.spikes.sprites():
            if sprite.rect.colliderect(enemy.rect):
                enemy.rect.bottom = sprite.rect.top
                enemy.direction.y = 0
                enemy.can_change = True
                self.enemy.empty()
                self.enemy_spawn = False
        
        
        
    def enemy_vertical_collision(self):
        enemy = self.enemy.sprite
        enemy.rect.y += enemy.direction.y
        enemy.apply_gravity()
        # Check collision with outline tiles
        for sprite in self.boundary.sprites() :
            if sprite.rect.colliderect(enemy.rect):
                enemy.can_change = False
                
                if enemy.rect.bottom > sprite.rect.top and enemy.direction.y > 0:
                    enemy.rect.bottom = sprite.rect.top
                    enemy.direction.y = 0
                                
                    

                elif enemy.rect.top < sprite.rect.bottom and enemy.direction.y < 0:
                    enemy.rect.top = sprite.rect.bottom
                    enemy.direction.y = -0.5*enemy.direction.y
                    
        for sprite in self.platform.sprites() :
            
            if sprite.rect.colliderect(enemy.rect):
                if enemy.rect.bottom > sprite.rect.top and enemy.direction.y >= 0:
                    enemy.rect.bottom = sprite.rect.top
                    enemy.direction.y = 0
                    enemy.can_change = True

                
                elif enemy.rect.top < sprite.rect.bottom and enemy.direction.y < 0:
                    enemy.rect.top = sprite.rect.bottom
                    enemy.direction.y = -0.5*enemy.direction.y
        for sprite in self.spikes.sprites():
            if sprite.rect.colliderect(enemy.rect):
                enemy.rect.bottom = sprite.rect.top
                enemy.direction.y = 0
                enemy.can_change = True
                self.enemy.empty()
                self.enemy_spawn = False
            
    
    def run(self):
        self.display_surface.fill((255,255,255,255))
        # self.bg.draw(self.display_surface)
        
        self.draw_background(self.display_surface)
        self.boundary.draw(self.display_surface)
        
        self.update_life()
        self.heart.draw(self.display_surface)
        # self.level.draw(self.display_surface)
        self.platform.draw(self.display_surface)
        self.home.draw(self.display_surface)
        self.platform_anim.draw(self.display_surface)
        self.spikes.draw(self.display_surface)
        self.rewards.draw(self.display_surface)
        self.movingTiles.draw(self.display_surface)
        self.movable_blocks.draw(self.display_surface)
        self.wheel.draw(self.display_surface)
        # self.movingTiles.update()
        for sprite in self.wheel:
            sprite.update()
        for sprite in self.home:
            sprite.update()

        for sprite in self.movingTiles:
            sprite.update()
            

        self.horizontal_collision()
        self.vertical_collision()
        # self.detect_top_left_slant_collision()
        if self.player:
            # print(self.player.sprite.rect)
            self.player.draw(self.display_surface)
        if self.enemy_spawn == False and self.player.sprite.gender =='Girl' and ((self.player.sprite.rect.x >= 200 and self.type == 'Level 0') or (self.player.sprite.rect.x >=371 and self.player.sprite.rect.y == 241  and self.type == 'Level 1')):
            self.enemy_setup()
        
        if self.player.sprite.gender !='Girl':
            self.enemy.empty()
            self.enemy_spawn = False

        if self.enemy:
            # print(self.enemy.sprite.rect)
            self.enemy.update()
            self.enemy_horizontal_collision()
            self.enemy_vertical_collision()
            self.enemy.draw(self.display_surface)	
        
        for sprite in self.rewards:
            sprite.update()
        self.respawn()
        
        # for sprite in self.player:
        # 	sprite.draw_mask(self.display_surface)
        if self.player: 
            self.player.update()
            
        # pygame.display.flip()

        # debug(self.coins)
    
    def updateState(self):
        if self.playState:
            return self.playState
        if self.playState == "over":
            return "over"
        elif self.playState == "complete":
            return "complete"