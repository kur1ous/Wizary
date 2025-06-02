import pygame as pg
from settings import *


class Button:
    def __init__(self, text, pos, size, callback, font, bg_color = (100,100,100), text_colour = (255,255,255)):
        self.rect = pg.Rect(pos, size)
        self.colour = bg_color
        self.text = text
        self.font = font
        self.text_colour = text_colour
        self.callback = callback

        self.rendered_text = self.font.render(self.text, True, self.text_colour)
        self.text_rect = self.rendered_text.get_rect(center=self.rect.center)

    def draw(self, surface):
        pg.draw.rect(surface, self.color, self.rect)
        surface.blit(self.rendered_text, self.text_rect)


    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.callback()

class Overlay:
    def __init__(self, player):
        self.player = player

        if GAME_STATE['START']:
            pass

    def draw(self, surface):
        pass
    def update(self):
        pass