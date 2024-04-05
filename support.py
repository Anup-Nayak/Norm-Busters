from csv import reader
import pygame
from os import walk
from settings import *
import os

def import_csv_layout(path):
	m = []
	if os.path.exists(path):
		with open(path) as map:
			level = reader(map,delimiter=',')
			for row in level:
				m.append(list(row))
			return m
def import_cut_graphic(path):
	surface = pygame.image.load(path).convert_alpha()
	tile_num_x = int(surface.get_size()[0]/TILESIZE)
	tile_num_y = int(surface.get_size()[1]/TILESIZE)
	
	cut_tiles = []
	
	for row in range(tile_num_y):
		for col in range(tile_num_x):
			x = col*TILESIZE
			y = row*TILESIZE
			newsurf = pygame.Surface((TILESIZE,TILESIZE))
			newsurf.blit(surface,(0,0),pygame.Rect(x,y,TILESIZE,TILESIZE))
			cut_tiles.append(newsurf)
	
	return cut_tiles	

def import_folder(path):
	surface_list = []
	for _,_,information in walk(path):
		for img in information:
			full_path = path + '/'+ img
			image_surf = pygame.image.load(full_path).convert_alpha()
			surface_list.append(image_surf)
	return surface_list

# import_folder('D:/Abhishek_Folder/Coding/Game Dev/COP1/assets/Player/Run')