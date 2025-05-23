import pygame as pg
from settings import *
from support import Spritesheet

class Player(pg.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)

        self.sheet = Spritesheet("Wizary\graphics\player\B_witch_idle.png")
        self.frame_index = 0
        self.frames = [self.sheet.get_sprite(0, y * 50,111,40) for y in range(6)] # not operational -- fix

        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(topleft=(100, 100))

        self.direction = pg.Vector2()
    def animation(self):
        pass

    def input(self):
        # if self.locked: return
        keys = pg.key.get_pressed()
        keys_just_pressed = pg.key.get_just_pressed()

        self.direction.y = keys[KEYBINDS['down']] - keys[KEYBINDS['down']] 
        self.direction.x = keys[KEYBINDS['right']] - keys[KEYBINDS['left']]


    def movement(self):
        #simple movement on x and y plane
        pass

    def spell_activate(self):
        #if spell keybind activated then fire off a spell
        pass

    def update(self, dt):
        self.frame_index += dt
        if self.frame_index >= len(self.frames):
            self.frame_index = 0
        self.image = self.frames[int(self.frame_index)] # move all frame handling into animation method
        self.input()