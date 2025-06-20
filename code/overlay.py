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

    def create_end_menu(self):
        self.buttons = []
        restart_button = Button("Restart", (SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 40), (200, 60), self.restart_game, self.font)
        quit_button = Button("Quit", (SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 40), (200, 60), self.quit_game, self.font)
        self.buttons.extend([restart_button, quit_button])

    def restart_game(self):
        GAME_STATE['START'] = False
        GAME_STATE['PLAYING'] = True
        GAME_STATE['OVER'] = False
        pg.event.post(pg.event.Event(pg.USEREVENT, {'action': 'RESTART'}))

    def quit_game(self):
        pg.quit()
        exit()

    def start_game(self):
        GAME_STATE['START'] = False
        GAME_STATE['PLAYING'] = True

    def handle_event(self, event):
        if GAME_STATE['START']:
            for button in self.buttons:
                button.handle_event(event)

    def draw_bar(self, surface, current, max_val, top_left, width, height, color, bg_color):
        pg.draw.rect(surface, bg_color, (*top_left, width, height)) #unpack tuple
        ratio = max(current / max_val, 0)
        pg.draw.rect(surface, color, (*top_left, width * ratio, height))

    def draw(self, surface):
        if GAME_STATE['START']:
            surface.fill((0, 0, 0))
            for button in self.buttons:
                button.draw(surface)

        if GAME_STATE['PLAYING']:
            bar_width, bar_height = 200, 20
            padding = 10
            self.draw_bar(surface, self.player.health, 100, (padding, padding), bar_width, bar_height, (255, 0, 0), (60, 60, 60)) #health
            self.draw_bar(surface, self.player.mana.current_mana, self.player.mana.mana_cap, (padding, padding + bar_height + 5), bar_width, bar_height, (0, 0, 255), (60, 60, 60)) #mana
    def update(self):
        pass