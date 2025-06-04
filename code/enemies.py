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
        self.hitbox = self.rect
        self.player = player
        self.speed = 40  

        self.health = 100

        self.z = LAYERS['main']  

    def movement(self, dt):
        self.direction = self.player.pos - self.pos
        if self.direction.length() > 1:
            self.direction.normalize_ip()
            self.pos += self.direction * self.speed * dt
            self.rect.center = self.pos

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.death()

    def check_if_hit(self):
        if self.hitbox.colliderect(self.player.bullet.rect):
            self.take_damage(5)

    def attack(self):
        if self.rect.colliderect(self.player.rect):
            self.kill()
            self.player.take_damage(5)
        
    def death(self):
        self.kill()

    def update(self, dt):
        self.attack()
        self.check_if_hit()
        self.movement(dt)


