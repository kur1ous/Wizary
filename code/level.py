import pygame as pg
from player import Player

class Level:
	def __init__(self):
		print(self)
		
		self.display_surface = pg.display.get_surface()

		self.all_sprites = pg.sprite.Group()

		self.player = Player(self.all_sprites)

	def run(self,dt):
		self.display_surface.fill('white')
		self.all_sprites.update(dt)
		self.all_sprites.draw(self.display_surface)
