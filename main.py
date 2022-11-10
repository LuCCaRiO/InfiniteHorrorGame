import pygame as pg
from player import Player
import sys
from settings import *


class Game:
    def __init__(self):
        self.screen: object = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pg.display.set_caption(GAME_NAME)

        self.visible_group = pg.sprite.Group()

        Player(self.visible_group, (SCREEN_WIDTH // 7, SCREEN_HEIGHT // 2))

    def run(self):
        clock: object = pg.time.Clock()
        while True:
            Game.handle_events()
            self.visible_group.update()
            self.render()
            clock.tick(FPS)

    @staticmethod
    def handle_events():
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()

    def render(self):
        self.screen.fill('lime')
        self.visible_group.draw(self.screen)
        pg.display.update()


if __name__ == '__main__':
    Game().run()
