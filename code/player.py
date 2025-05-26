import pygame as pg
from settings import *
from support import load_sheet, import_assets, import_folder, import_folder_dict

class Player(pg.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)

        self.input_lock = False

        self.frame_index = 0
        self.animation_speed = 6  

        self.base_speed = 60

        self.status = 'witch_idle'

        self.animations = import_folder_dict("Wizary\graphics\player")
        print(f"anims: {self.animations[self.status]}")


        self.frames = load_sheet(f"Wizary\graphics\player\{self.status}.png", 32, 48)
        print(f"frame: {self.frames}")

        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(topleft=(100, 100))

        self.direction = pg.Vector2()
        self.pos = pg.Vector2(self.rect.topleft)

    # @property
    # def image(self):
    #     return self.animations[self.status]

    def animate(self, dt):
        self.frame_index += self.animation_speed * dt
        self.frame_index = self.frame_index % len(self.frames)
        self.image = self.frames[int(self.frame_index)]


    def input(self):
        # if self.locked: return
        keys = pg.key.get_pressed()
        keys_just_pressed = pg.key.get_just_pressed()

        self.direction.y = keys[KEYBINDS['down']] - keys[KEYBINDS['up']]
        self.direction.x = keys[KEYBINDS['right']] - keys[KEYBINDS['left']]


    def get_status(self):
        self.status = self.status.split("_")[0]
        keys = pg.key.get_pressed()

        if self.direction.magnitude() > 0:
            self.status += "_run"

        elif self.direction.magnitude() == 0:
            self.status += "_idle"
        




    def movement(self, dt):
        #simple movement on x and y plane
        if self.direction.magnitude() != 0:
            self.direction.normalize_ip()

        self.pos.x += self.direction.x * dt * self.base_speed
        self.pos.y += self.direction.y * dt * self.base_speed
        self.rect.center = self.pos



    def spell_activate(self):
        #if spell keybind activated then fire off a spell
        pass

    def update(self, dt):
        self.get_status()
        self.animate(dt)
        self.input()
        self.movement(dt)