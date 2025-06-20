import pygame as pg
from settings import *
import math
from support import get_spawn_position, load_sheet
from timehandle import Timer

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

        self.abilities = {
            'attack' : Timer(2)
        }

    def movement(self, dt):
        self.direction = self.player.pos - self.pos
        if self.direction.length() > 1:
            self.direction.normalize_ip()
            self.pos += self.direction * self.speed * dt
            self.rect.center = self.pos

    def take_damage(self, damage):
        self.health -= damage
        print(self.health)
        if self.health <= 0:
            self.death()
            self.player.addscore(1)

    def check_if_hit(self):
        for projectile in self.player.projectile_group:
            if self.hitbox.colliderect(projectile.hitbox):
                self.take_damage(getattr(projectile, 'damage', 0))
                projectile.kill()  
        
    def check_if_can_attack(self):
        if self.rect.colliderect(self.player.rect): return True

    def attack_handle(self):
        if self.check_if_can_attack() and not self.abilities['attack'].active:
            self.attack(5)
            self.abilities['attack'].activate()

    def attack(self, damage):
        self.player.take_damage(damage)
        
    def death(self):
        self.kill()
    
    def timer_handle(self, dt):
        for timer in self.abilities.values():
            timer.update(dt)

    def update(self, dt):

        self.check_if_can_attack()
        self.timer_handle(dt)
        self.attack_handle()
        self.check_if_hit()
        self.movement(dt)


