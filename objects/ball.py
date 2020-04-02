import pygame

from base import Vector2D, Colour
from base.collision_object import CollisionObject
from base.game_object import GameObject


class Ball(GameObject):

    def __init__(self, pos: Vector2D = (0, 0), radius=3, colour: Colour = (0, 0, 0)):
        super().__init__(pos)
        self.radius = radius
        self.colour = colour
        self.hitbox = CollisionObject(pos=pos, scale=Vector2D(x=int(radius * 2 * 0.9), y=int(radius * 2 * 0.9)),
                                      center=Vector2D(-int(radius * 0.9), -int(radius * 0.9)))
        self.hitbox.visible = True

    def update(self):
        self.hitbox.pos = self.pos

    def draw(self, screen):
        pygame.draw.circle(screen, self.colour, self.pos, self.radius)
        self.hitbox.draw(screen)
