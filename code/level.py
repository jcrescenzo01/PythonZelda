"""
    level.py is important, the central part of the game. The container that contains all of the
essential game elements. It will handle and manage hundreds of sprites effectively. Key concepts
are different groups portraying different functionality types of sprites
- visible_sprites = group of sprites that will be drawn on the screen
- obstacle_sprites = group for sprites that the player can collide with
Main Point: You can put sprites into different groups, they can be in multiple groups at once, and
depending on the group its in, it will interact with its enviornment differently
"""
import pygame

class Level:
    def __init__(self):
        # get the display surface
        self.display_surface = pygame.display.get_surface()
        # Sprite Group Setup
        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()

    def run(self):
        # update and draw the game
        pass