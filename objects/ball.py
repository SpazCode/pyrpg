import pygame

from base import Vector2D, Colour
from base.game_object import GameObject


class Ball(GameObject):

    def __init__(self, pos: Vector2D = (0, 0), radius=3, colour: Colour = (0, 0, 0)):
        super().__init__(pos)
        self.radius = radius
        self.colour = colour

    def draw(self, screen):
        pygame.draw.circle(screen, self.colour, self.pos, self.radius)
