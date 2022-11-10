import pygame as pg
from entity import Entity


SPEED = 5


class Player(Entity):
    def __init__(self, groups, pos):
        super(Player, self).__init__(groups, pg.image.load('./imgs/New Piskel-1.png'), pos)
        self.speed: object = pg.math.Vector2()
        self.angle: int = 90

    def input_(self):
        key: object = pg.key.get_pressed()
        if key[pg.K_SPACE]:
            self.speed.y = -SPEED
        else:
            self.speed.y = SPEED


    def move(self):
        self.rect.topleft += self.speed

    def update(self):
        self.input_()
        self.move()
