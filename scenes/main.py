import operator

from base import Vector2D, Colour
from base.scene import Scene
from objects.ball import Ball


class Main(Scene):
    BLACK = Colour(0, 0, 0)
    BLUE = Colour(50, 50, 200)
    WHITE = Colour(255, 255, 255)

    def __init__(self):
        super().__init__()
        self.add_object("ball", BouncingBall(pos=Vector2D(225, 225), radius=50, colour=Main.BLUE), 1)

    def update(self):
        self.screen.fill(Main.WHITE)
        super().update()


class BouncingBall(Ball):
    def __init__(self, pos: Vector2D = (0, 0), radius=3, colour: Colour = (0, 0, 0), gravity=3):
        super().__init__(pos, radius, colour)
        self.gravity = gravity
        self.speed = Vector2D(0, 0)

    def update(self):
        if self.pos.y < 500 - self.radius:
            if self.speed.y < 15:
                self.speed += Vector2D(0, self.gravity)
        else:
            self.speed = Vector2D(0, -50)
        self.pos += self.speed
        print(self.pos)
