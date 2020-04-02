from collections import namedtuple
from typing import NamedTuple

Colour = namedtuple('Color', ('r', 'b', 'g'))


class Vector2D(NamedTuple):
    x: int
    y: int

    def __add__(self, other):
        if not isinstance(other, Vector2D):
            raise TypeError()
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        if not isinstance(other, Vector2D):
            raise TypeError()
        return Vector2D(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if not isinstance(other, Vector2D):
            raise TypeError()
        return Vector2D(self.x * other.x, self.y * other.y)
