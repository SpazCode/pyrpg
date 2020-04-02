import pygame
from pygame.rect import Rect

from base import Vector2D, Colour


class CollisionObject(object):
    def __init__(self, label="Default", pos: Vector2D = Vector2D(0, 0), scale: Vector2D = Vector2D(0, 0),
                 center: Vector2D = Vector2D(0, 0),
                 colour: Colour = (0, 0, 0)):
        self.label = label
        self.pos: Vector2D = pos
        self.scale: Vector2D = scale
        self.center: Vector2D = center
        self.colour: Colour = colour
        self.visible = False
        global_pos: Vector2D = self.pos + self.center
        self.rect = Rect(global_pos.x, global_pos.y, self.scale.x, self.scale.y)

    def update(self):
        global_pos: Vector2D = self.pos + self.center
        self.rect = Rect(global_pos.x, global_pos.y, self.scale.x, self.scale.y)

    def draw(self, screen):
        if self.visible:
            pygame.draw.rect(screen, self.colour, self.rect, 5)

    def is_colliding(self, other):
        return self.rect.colliderect(other.rect)

    def is_colliding_any(self, others: list):
        return self.rect.collidelist(others)

    def is_colliding_all(self, others: list):
        return self.rect.collidelistall(others)
