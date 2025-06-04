import pygame
from settings import *

class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()

    def draw(self, surface, offset):
        # print(offset)
        offset = pygame.Vector2(offset)
        offset -= pygame.Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

        for layer in LAYERS.values():
            for sprite in sorted(self.sprites(), key=lambda spr: (spr.z, spr.rect.centery)):
                blit_pos = sprite.rect.topleft - offset
                surface.blit(sprite.image, blit_pos)
                hitbox = sprite.rect.copy()
                hitbox.topleft -= offset
                pygame.draw.rect(surface, "red", hitbox, 2)