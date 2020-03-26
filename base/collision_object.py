import pygame

from base import Vector2D, Colour


class CollisionObject(object):
    def __init__(self, pos: Vector2D = (0, 0), scale: Vector2D = (0, 0), center: Vector2D = (0, 0),
                 colour: Colour = (0, 0, 0)):
        self.pos: Vector2D = pos
        self.scale: Vector2D = scale
        self.center: Vector2D = center
        self.colour: Colour = colour
        self.visible = False

    def draw(self, screen):
        if self.visible:
            global_pos: Vector2D = self.pos + self.center
            rect = (global_pos.x, global_pos.y, self.scale.x, self.scale.y)
            pygame.draw.rect(screen, self.colour, rect, width=4)

    def is_colliding(self, other):
        if self.pos.y < other.pos.y <= (self.pos.y + self.scale.y):
            if self.pos.x < other.pos.x <= (self.pos.x + self.scale.x):
                return True
        return False
