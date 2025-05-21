import pygame as pg
import os, sys

class Spritesheet(object):
    def __init__(self, filename):
        self.filename = filename
        self.sprite_sheet = pg.image.load(filename).convert_alpha()

    def get_sprite(self, x, y, w, h):
        sprite = pg.Surface((w,h))
        sprite.set_colorkey((0,0,0))
        sprite.blit(self.sprite_sheet, (0,0), (x,y,w,h))
        return sprite