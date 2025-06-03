import pygame as pg
from player import Player
from cameragroup import CameraGroup
from sprites import Generic
from settings import *
from support import get_spawn_position
from enemies import Enemy
from overlay import Overlay

class Level:
	def __init__(self):
		print(self)
		
		self.display_surface = pg.display.get_surface()
		self.all_sprites = CameraGroup()

		# Enemy Spawn Handling
		self.spawn_timer = 0
		self.spawn_interval = 5
		self.spawn_area = pg.Rect(0,0,SCREEN_HEIGHT, SCREEN_WIDTH)





		ground_image = pg.image.load("Wizary\graphics\world\Scene Overview.png").convert_alpha()
		self.ground = Generic((0,0), ground_image, LAYERS['ground'], self.all_sprites)

		self.player = Player((100, 100), self.all_sprites)

		self.overlay = Overlay(self.player)


	def enemy_spawn(self, dt):
		self.spawn_timer += dt
		if self.spawn_timer > self.spawn_interval:
			self.enemy_pos = get_spawn_position(self.player.pos, 200, self.spawn_area)
			self.enemy = Enemy(self.enemy_pos, self.player, self.all_sprites)
			self.spawn_timer = 0



	def run(self,dt):
		self.display_surface.fill('white')
		if GAME_STATE['START']:
			self.overlay.draw(self.display_surface)
			return
		self.enemy_spawn(dt)
		self.all_sprites.draw(self.display_surface, (self.player.rect.center))
		self.all_sprites.update(dt)



		

