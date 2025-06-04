import pygame as pg
from settings import *


class Generic(pg.sprite.Sprite):

    def __init__(self, pos, surface, z, groups):
        super().__init__(groups)
        self.image = surface
        self.rect = self.image.get_frect(topleft=pos)
        self.hitbox = self.rect.inflate(-0.2* self.rect.width, -0.75* self.rect.height)
        self.z = z


class Projectile(Generic):
    def __init__(self, pos, direction, speed, max_distance, groups):
        surface = pg.Surface((8,8), pg.SRCALPHA)
        surface.fill("cyan")
        super().__init__(pos, surface, LAYERS['main'], groups)

        self.pos = pg.Vector2(pos)
        self.direction = direction.normalize()
        self.speed = speed
        self.max_distance = max_distance
        self.distance_traveled = 0




    def update(self, dt):
        movement = self.direction * self.speed * dt
        self.pos += movement
        self.distance_traveled += movement.length()
        self.rect.center = self.pos  # Move image and hitbox
        self.hitbox.center = self.rect.center

        if self.distance_traveled >= self.max_distance:
            self.kill()