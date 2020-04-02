import pygame

from base import Vector2D, Colour
from base.collision_object import CollisionObject
from base.game_object import GameObject


class Rectangle(GameObject):
    def __init__(self, pos: Vector2D = (0, 0), scale: Vector2D = (0, 0), colour: Colour = Colour(0, 0, 0)):
        self.pos = pos
        self.scale = scale
        self.colour = colour
        self.exists = True
        self.hitbox = CollisionObject(pos=pos, scale=scale)

    # Game logic for this object that needs to be updated every frame.
    def update(self):
        self.hitbox.pos = self.pos

    # Mark this object that is to be terminated.
    def terminate(self):
        self.exists = False

    # How to Draw the object to the screen.
    def draw(self, screen):
        rect = (self.pos.x, self.pos.y, self.scale.x, self.scale.y)
        pygame.draw.rect(screen, self.colour, rect)
        self.hitbox.draw(screen)
