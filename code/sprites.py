import pygame as pg
from settings import *


class Generic(pg.sprite.Sprite):

    def __init__(self, pos, surface, z, groups):
        super().__init__(groups)
        self.image = surface
        self.rect = self.image.get_frect(topleft=pos)
        # self.hitbox = self.rect.inflate(-0.2* self.rect.width, -0.75* self.rect.height)
        self.z = z