import pygame as pg

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720


KEYBINDS = {
    'up' : pg.K_w,
    'down' : pg.K_s,
    'left' : pg.K_a,
    'right' : pg.K_d,
    'mana charge' : pg.K_e,
}

LAYERS = {
    'main' : 7,
    'ground' : 1,
}

GAME_STATE = {
    'START' : True,
    'PLAYING' : False,
    'PAUSE' : False,
    'OVER' : False,
}