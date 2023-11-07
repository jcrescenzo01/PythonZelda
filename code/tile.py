import pygame
from settings import *

# assets: https://github.com/clear-code-projects/Zelda

class Tile(pygame.sprite.Sprite)
    def __init__(self, pos, groups):
        super().__init__(groups)  # initiating pygame.sprite.Sprite, passing groups into it as well
        self.image = pygame.image.load('../graphics/test/rock.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)