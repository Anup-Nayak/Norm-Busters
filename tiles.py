
from settings import *
from support import *
from debug import *
import pygame
WHITE = (255, 255, 255,255)

class Tile(pygame.sprite.Sprite):
    def __init__(self,size,x,y):
        super().__init__()
        self.image = pygame.Surface((size,size), pygame.SRCALPHA)
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
                    self.image.set_at((x, y), (0, 0, 0, 0))  

class StaticTile(Tile):
    def __init__(self,size,x,y,surface):
        super().__init__(size,x,y)
        
        self.rect = self.image.get_rect(topleft = (x,y))
        self.image = (surface).convert_alpha()

class OutlineTile(Tile):
    def __init__(self,size,x,y,surface):
        super().__init__(size,x,y)
        
        self.rect = self.image.get_rect(topleft = (x,y))
        self.set_image(surface)
     
class HomeTile(Tile):
    def __init__(self,size,x,y):
        super().__init__(size,x,y)
        
        self.rect = self.image.get_rect(topleft = (x,y))
        self.animation_speed =0
        self.index = 3
        self.path = './assets/Exit/Door/'
        self.import_assets()

    def import_assets(self):
        self.animations = import_folder(self.path)
        
    def animate(self):
        self.index  +=self.animation_speed
        if(self.index >=len(self.animations)):
            self.index =0
        self.image = self.animations[int(self.index)]
        self.rect.height = 150
        self.rect.width = 50

    def update(self):
        self.animate()

class SpikeTile(Tile):
    def __init__(self,size,x,y,surface):
        super().__init__(size,x,y)
        
        self.rect = self.image.get_rect(topleft = (x,y))
        self.set_image1(surface)

class Platform_Anim(Tile):
    def __init__(self,size,x,y,surface):
        super().__init__(size,x,y)
        
        self.rect = self.image.get_rect(topleft = (x,y))
        self.image = surface.convert_alpha()

        for x in range(self.image.get_width()):
            for y in range(self.image.get_height()):
                r, g, b, _ = self.image.get_at((x, y))
                if r <= 10 and g <= 10 and b <= 10:
                    self.image.set_at((x, y), (0, 0, 0, 0))

class AnimatedTile(Tile):
    def __init__(self,size,x,y,path,speed =0.1):
        super().__init__(size,x,y)
        
        self.rect = self.image.get_rect(topleft = (x,y))
        self.animation_speed =speed
        self.index = 0
        self.path = path
        self.import_assets()
    def import_assets(self):
        self.animations = []
        self.animations = import_folder(self.path)

    def animate(self):
        self.index  +=self.animation_speed
        if(self.index >=len(self.animations)):
            self.index =0
        self.image = self.animations[int(self.index)]
        self.rect.height = self.image.get_height()
        self.rect.width = self.image.get_width()
        
    def update(self):
        self.animate()
  
class MovingTile(Tile):
    def __init__(self, size, x, y, surface, speed=1, direction='horizontal'):
        super().__init__(size, x, y)
        self.rect = self.image.get_rect(topleft = (x,y))
        self.surface = surface
        self.image = surface.convert_alpha()
        self.rect = self.image.get_rect(topleft =(x,y))
        self.speed = speed
        self.direction = direction

    def update(self):
        if self.direction == 'horizontal':
            self.rect.x += self.speed
        elif self.direction == 'vertical':
            self.rect.y += self.speed
        
class MovableBlocks(Tile):
    def __init__(self,size,x,y):
        super().__init__(size,x,y)
        self.rect = self.image.get_rect(topleft = (x,y))
        self.image = (import_folder('./assets/Block/'))[0]
        self.rect.height = 50
        self.rect.width = 50
    def move(self,dx,dy):
        self.rect.x += dx
        self.rect.y += dy
        print(self.rect.x,self.rect.y)

class Wheel(Tile):
    def __init__(self,size,x,y,path,speed =0.1):
        super().__init__(size,x,y)
        self.rect = self.image.get_rect(topleft = (x,y))
        self.animation_speed =speed
        self.index = 0
        self.path = path
        self.import_assets()
        
    def import_assets(self):
        self.animations = []
        self.animations = import_folder(self.path)
        
    def animate(self):
        self.index  +=self.animation_speed
        if(self.index >=len(self.animations)):
            self.index =0
        self.image = self.animations[int(self.index)]
        self.rect.height = 69
        self.rect.width = 69
        
    def update(self):
        self.animate()
  
