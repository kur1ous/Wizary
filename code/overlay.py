import pygame as pg
from settings import *


class Button:
    def __init__(self, text, pos, size, callback, font, bg_colour = (100,100,100), text_colour = (255,255,255)):
        self.rect = pg.Rect(pos, size)
        self.colour = bg_colour
        self.text = text
        self.font = font
        self.text_colour = text_colour
        self.callback = callback

        self.rendered_text = self.font.render(self.text, True, self.text_colour)
        self.text_rect = self.rendered_text.get_rect(center=self.rect.center)

    def draw(self, surface):
        pg.draw.rect(surface, self.colour, self.rect)
        surface.blit(self.rendered_text, self.text_rect)


    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.callback()

class Overlay:
    def __init__(self, player):
        self.player = player
        self.font = pg.font.SysFont("Arial",36)
        self.buttons = []


        if GAME_STATE['START']:
            self.create_start_menu()
        
    def create_start_menu(self):
        self.buttons = []
        start_button = Button("start", (SCREEN_WIDTH/2, SCREEN_HEIGHT/2), (200, 60), self.start_game, self.font)
        self.buttons.append(start_button)

    def start_game(self):
        GAME_STATE['START'] = False
        GAME_STATE['PLAYING'] = True

    def handle_event(self, event):
        if GAME_STATE['START']:
            for button in self.buttons:
                button.handle_event(event)

    def draw(self, surface):
        if GAME_STATE['START']:
            surface.fill((0,0,0))
            for button in self.buttons:
                button.draw(surface)
    def update(self):
        pass