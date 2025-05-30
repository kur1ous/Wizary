import pygame as pg
from settings import *
import math
from support import get_spawn_position

class Enemy(pg.sprite.Sprite):
    def __init__(self, pos, player, groups):
        super().__init__(groups)

        self.image = pg.Surface((32, 32))
        self.image.fill('red')
        self.rect = self.image.get_rect(center=pos)
        self.pos = pg.Vector2(pos)
        self.player = player
        self.speed = 40  

        self.z = LAYERS['main']  

    def movement(self, dt):
        self.direction = self.player.pos - self.pos
        if self.direction.length() > 1:
            self.direction.normalize_ip()
            self.pos += self.direction * self.speed * dt
            self.rect.center = self.pos

    def take_damage(self, damage):
        self.kill()

    def attack(self):
        if self.rect.colliderect(self.player.rect):
            self.kill()
            self.player.take_damage(5)

    def update(self, dt):
        self.attack()
        self.movement(dt)


