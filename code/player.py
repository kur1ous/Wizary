import pygame as pg
from settings import *
from support import Spritesheet

class Player(pg.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)

        self.sheet = Spritesheet("Wizary\graphics\player\B_witch_idle.png")
        self.player = self.sheet.get_sprite(0,0,128,128)

        