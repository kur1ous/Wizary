import pygame as pg
from settings import *
from support import load_sheet, import_assets, import_folder, import_folder_dict
from timehandle import Timer
from sprites import Generic, Projectile

class Player(pg.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)

        self.health = 100

        self.frame_index = 0

        self.animation_speed = 6  

        self.base_speed = 60

        self.status = 'witch_idle'

        self.z = LAYERS['main']

        self.right = True

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
            "basic",
            "ice_ball",
        ]

        self.selected_spell = self.spells[0]

        self.timers = {
            'spell charge' : Timer(2, self.spell_charge),
            'spell fire' : Timer(0.999, self.spell_fire)
        }

        print(f"anims: {self.animations[self.status]}")


        print(f"frame: {self.frames}, number: {len(self.frames)}")
        


        # self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(center=(pos))

        self.direction = pg.Vector2()
        self.pos = pg.Vector2(self.rect.midbottom)

    @property
    def frames(self):
        return self.animations[self.status]

    @property
    def image(self):
        frame = self.frames[int(self.frame_index)]
        if not self.right:
            frame = pg.transform.flip(frame, True, False)
        return frame    
    @property
    def locked(self):
        return self.timers['spell charge'].active or self.timers['spell fire'].active

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

        if self.direction.x > 0:
            self.right = True
        elif self.direction.x < 0:
            self.right = False


        if keys_just_pressed[KEYBINDS['attack']]:
            self.timers['spell charge'].activate()

        if pg.mouse.get_pressed()[0]:
            self.shoot()



    def shoot(self):
        mouse_pos = pg.mouse.get_pos()
        offset = pg.Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        camera_offset = self.rect.center - offset  # get world offset from camera

        world_mouse_pos = pg.Vector2(mouse_pos) + camera_offset
        direction = world_mouse_pos - self.rect.center

        if direction.length() > 0:
            Projectile(
                pos=self.rect.center,
                direction=direction,
                speed=300,
                max_distance=500,
                groups=self.groups()
            )


    def get_status(self):
        self.status = self.status.split("_")[0]
        keys = pg.key.get_pressed()

        if self.timers['spell charge'].active:
            self.status += "_charge"

        elif self.timers['spell fire'].active:
            self.status += "_attack"

        elif self.direction.magnitude() > 0:
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
        if self.locked: return
        #simple movement on x and y plane
        if self.direction.magnitude() != 0:
            self.direction.normalize_ip()

        self.pos.x += self.direction.x * dt * self.base_speed
        self.pos.y += self.direction.y * dt * self.base_speed
        self.rect.center = self.pos

        
    def spell_charge(self):
        print("charged!")
        self.timers['spell fire'].activate()


    def spell_fire(self):
        print(self.selected_spell)

    def lock_input(self):
        self.locked = True

    def unlock_input(self):
        self.locked = False

    def take_damage(self, damage):
        self.damage = damage
        self.health -= self.damage
        print(self.health)
        
    def death(self):
        print("Game Over!")
        GAME_STATE['PLAYING'] = False
        GAME_STATE['START'] = False
        GAME_STATE['PAUSE'] = False
        GAME_STATE['OVER'] = True

    def update(self, dt):
        self.get_status()
        self.animate(dt)
        self.input()
        self.update_timers(dt)
        self.movement(dt)