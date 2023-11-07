import pygame, sys
from settings import *  # importing everything from settings.py
from level import Level

# from debug import debug     # debugger so we can track game stuff

class Game:
    def __init__(self):  # this stuff is the usual basic setup for pygame
        # general setup
        pygame.init()  # we initiate pygame
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))  # we create a display surface
        ##myadditions_start
        pygame.display.set_caption("Swordguy I guess?")
        icon = pygame.image.load('halberd.png')
        pygame.display.set_icon(icon)
        ##myadditions_end
        self.clock = pygame.time.Clock()  # created a clock
        self.level = Level()    # instance of level created
    def run(self):  # run
        while True:
            for event in pygame.event.get():  # event/game loop
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill('black')  # filling the screen black
            self.level.run()    # level running in loop
            # debug('hello!')    # debug, used here, would print hello! at the top left of the screen
            pygame.display.update()  # updating the screen
            self.clock.tick(FPS)  # controlling the framerate


if __name__ == '__main__':  # check if its the main file
    game = Game()  # create an instance of the Game() class
    game.run()  # use the method run() from class Game()
