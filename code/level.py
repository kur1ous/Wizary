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

		self.projectiles = pg.sprite.Group()

		# Enemy Spawn Handling
		self.spawn_timer = 0
		self.spawn_interval = 5
		self.spawn_area = pg.Rect(0,0,SCREEN_HEIGHT, SCREEN_WIDTH)

		# ground_image = pg.image.load("graphics\world\Scene Overview.png").convert_alpha()
		# self.ground = Generic((0,0), ground_image, LAYERS['ground'], self.all_sprites)


		self.player = Player((100, 100), self.projectiles, self.all_sprites)

		self.overlay = Overlay(self.player)


	def enemy_spawn(self, dt):
		self.spawn_timer += dt
		if self.spawn_timer > self.spawn_interval:
			self.enemy_pos = get_spawn_position(self.player.pos, 200, self.spawn_area)
			self.enemy = Enemy(self.enemy_pos, self.player, self.all_sprites)
			self.spawn_timer = 0

	def create_tile_background(self, tile_size=64):
		tile_size = 64
		colors = ['#1e1e1e', '#2a2a2a']

		# Camera offset
		cam_offset = pg.Vector2(self.player.rect.center) - pg.Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

		# Determine how many tiles to draw
		cols = (SCREEN_WIDTH // tile_size) + 3
		rows = (SCREEN_HEIGHT // tile_size) + 3

		# Find top-left world coordinate of the visible screen
		top_left_world = cam_offset - pg.Vector2(tile_size, tile_size)
		start_x = int(top_left_world.x // tile_size) * tile_size
		start_y = int(top_left_world.y // tile_size) * tile_size

		for row in range(rows):
			for col in range(cols):
				world_x = start_x + col * tile_size
				world_y = start_y + row * tile_size

				color_index = ((world_x // tile_size) + (world_y // tile_size)) % 2
				surface = pg.Surface((tile_size, tile_size))
				surface.fill(colors[color_index])

				# Convert world position to screen position
				screen_pos = (world_x - cam_offset.x, world_y - cam_offset.y)
				self.display_surface.blit(surface, screen_pos)




	def run(self,dt):
		self.create_tile_background()

		if GAME_STATE['START']:
			self.overlay.draw(self.display_surface)
			return

		self.enemy_spawn(dt)
		self.all_sprites.draw(self.display_surface, self.player.rect.center)
		self.all_sprites.update(dt)

		self.overlay.draw(self.display_surface)



		

