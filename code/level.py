import pygame as pg
from player import Player
from cameragroup import CameraGroup
from sprites import Generic
from settings import *

class Level:
	def __init__(self):
		print(self)
		
		self.display_surface = pg.display.get_surface()
		self.all_sprites = CameraGroup()




		ground_image = pg.image.load("Wizary\graphics\world\Scene Overview.png").convert_alpha()
		self.ground = Generic((0,0), ground_image, LAYERS['ground'], self.all_sprites)

		self.player = Player((100, 100), self.all_sprites)

		print(f"PLAYER Z: {self.player.z}")
		print(f"GROUND Z: {self.ground.z}")




	def run(self,dt):
		self.display_surface.fill('white')
		self.all_sprites.draw(self.display_surface, (self.player.rect.center))
		self.all_sprites.update(dt)

		

