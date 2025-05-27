import pygame as pg
from settings import *
from support import load_sheet, import_assets, import_folder, import_folder_dict
from timehandle import Timer

class Player(pg.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)

        self.input_lock = False

        self.frame_index = 0
        self.animation_speed = 6  

        self.base_speed = 60

        self.status = 'witch_idle'

        self.locked = False

        self.animations = { 
            "witch_idle" : load_sheet(f"Wizary\graphics\player\witch_idle.png", 32, 48),
            "witch_run" : load_sheet(f"Wizary\graphics\player\witch_run.png", 32, 48),
            "witch_charge" : load_sheet(f"Wizary\graphics\player\witch_charge.png", 48, 48),
            "witch_attack" : load_sheet(f"Wizary\graphics\player\witch_attack.png", 104, 46),
            "witch_damage" : load_sheet(f"Wizary\graphics\player\witch_damage.png", 32, 48),
            "witch_death" : load_sheet(f"Wizary\graphics\player\witch_death.png", 32, 40)
        }

        self.spells = [
            "ice_spike",
            "ice_ball",
        ]

        self.timers = {
            'spell use' : Timer(2, self.spell_charge),
        }

        print(f"anims: {self.animations[self.status]}")


        print(f"frame: {self.frames}, number: {len(self.frames)}")
        


        # self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(topleft=(100, 100))

        self.direction = pg.Vector2()
        self.pos = pg.Vector2(self.rect.topleft)

    @property
    def frames(self):
        return self.animations[self.status]

    @property
    def image(self):
        return self.frames[int(self.frame_index)]

    def animate(self, dt):
        self.frame_index += self.animation_speed * dt
        self.frame_index %= len(self.frames)
        # self.image = self.frames[int(self.frame_index)]


    def input(self):
        if self.locked: return
        keys = pg.key.get_pressed()
        keys_just_pressed = pg.key.get_just_pressed()

        self.direction.y = keys[KEYBINDS['down']] - keys[KEYBINDS['up']]
        self.direction.x = keys[KEYBINDS['right']] - keys[KEYBINDS['left']]


        if keys_just_pressed[KEYBINDS['attack']]:
            print("testing")
            self.timers['spell use'].activate()

            print("activated!")



    def get_status(self):
        self.status = self.status.split("_")[0]
        keys = pg.key.get_pressed()

        if self.direction.magnitude() > 0:
            self.status += "_run"

        elif self.direction.magnitude() == 0:
            self.status += "_idle"

        # elif self.spell_charge(True):
        #     self.status += "_charge"
        
        
        # print(self.status)


    def update_timers(self, dt):
        for timer in self.timers.values():
            timer.update(dt)

    def movement(self, dt):
        #simple movement on x and y plane
        if self.direction.magnitude() != 0:
            self.direction.normalize_ip()

        self.pos.x += self.direction.x * dt * self.base_speed
        self.pos.y += self.direction.y * dt * self.base_speed
        self.rect.center = self.pos

        
    def spell_charge(self):
        self.input_locked()
        print("charged!")


    def spell_activate(self):
        #if spell keybind activated then fire off a spell
        pass

    def lock_input(self):
        self.locked = True

    def unlock_input(self):
        self.locked = False

    def update(self, dt):
        self.get_status()
        self.animate(dt)
        self.input()
        self.update_timers(dt)
        self.movement(dt)