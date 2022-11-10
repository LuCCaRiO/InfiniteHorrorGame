import pygame as pg
import sys
from settings import *


class Game:
    def __init__(self):
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pg.display.set_caption(GAME_NAME)

    def run(self):
        clock = pg.time.Clock()
        while True:
            self.handle_events()
            clock.tick(FPS)

    @staticmethod
    def handle_events():
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()


if __name__ == '__main__':
    Game().run()
