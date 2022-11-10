import pygame as pg


class Entity(pg.sprite.Sprite):
    def __init__(self, groups, image, position):
        super(Entity, self).__init__(groups)
        self.image: object = image
        self.rect: object = self.image.get_rect(topleft=position)
