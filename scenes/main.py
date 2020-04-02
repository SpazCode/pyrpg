import csv
import pygame

from base import Vector2D, Colour
from base.game_object import GameObject
from base.scene import Scene
from objects.ball import Ball
from objects.rectangle import Rectangle
from io import StringIO


class Main(Scene):
    BLACK = Colour(0, 0, 0)
    BLUE = Colour(50, 50, 200)
    WHITE = Colour(255, 255, 255)
    RED = Colour(200, 50, 50)

    def __init__(self):
        super().__init__()
        # Build game objects.

        self.maze = Maze("""1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1
        1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1
        1,0,1,1,1,1,1,0,1,0,1,0,1,1,1,1,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,0,1
        1,0,0,0,0,0,1,0,1,0,1,0,1,0,0,0,1,0,1,0,1,0,0,0,0,0,1,0,0,0,0,0,1
        1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,0,1,0,1,1,1,1,1,1,1,0,1,0,1,1,1,0,1
        1,0,1,0,1,0,0,0,1,0,1,0,0,0,1,0,1,0,0,0,1,0,0,0,1,0,1,0,1,0,1,0,1
        1,0,1,0,1,0,1,1,1,0,1,1,1,0,1,0,1,1,1,0,1,0,1,1,1,0,1,0,1,0,1,0,1
        1,0,0,0,1,0,0,0,0,0,0,0,1,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0,1,0,1,0,1
        1,0,1,1,1,1,1,1,1,0,1,0,1,1,1,0,1,0,1,1,1,0,1,1,1,1,1,1,1,0,1,0,1
        1,0,1,0,0,0,0,0,1,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0,1,0,1
        1,0,1,1,1,0,1,1,1,0,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,0,1,0,1
        1,0,0,0,1,0,1,0,0,0,1,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,1,0,0,0,1
        1,1,1,0,1,0,1,1,1,1,1,0,1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,0,1,1,1,0,1
        1,0,1,0,1,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,1
        1,0,1,0,1,0,1,1,1,1,1,0,1,1,1,0,1,0,1,1,1,0,1,1,1,1,1,1,1,0,1,0,1
        1,0,0,0,1,0,1,0,1,0,0,0,1,0,0,0,1,0,1,0,0,0,1,0,0,0,0,0,1,0,1,0,1
        1,0,1,1,1,0,1,0,1,1,1,0,1,1,1,1,1,0,1,0,1,0,1,0,1,1,1,0,1,0,1,0,1
        1,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,1,0,1,0,1,0,0,0,1,0,1,0,1
        1,0,1,0,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,0,1,1,1,1,1,0,1,0,1
        1,0,1,0,1,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,1,0,1,0,0,0,0,0,0,0,1,0,1
        1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,0,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1
        2,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,1,0,0,0,0,0,1
        1,0,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,0,1
        1,0,0,0,0,0,1,0,0,0,1,0,1,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,1,0,1,0,1
        1,0,1,1,1,0,1,1,1,1,1,0,1,1,1,0,1,0,1,0,1,0,1,1,1,1,1,0,1,0,1,0,1
        1,0,1,0,1,0,1,0,0,0,0,0,0,0,1,0,1,0,1,0,1,0,1,0,0,0,1,0,0,0,1,0,1
        1,1,1,0,1,0,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,0,1,1,1,0,1,0,1
        1,0,0,0,0,0,1,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,1,0,1,0,1
        1,1,1,1,1,0,1,0,1,1,1,1,1,0,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,0,1,1,1
        1,0,0,0,1,0,1,0,1,0,0,0,0,0,1,0,0,0,1,0,1,0,0,0,0,0,1,0,1,0,0,0,3
        1,0,1,1,1,0,1,1,1,0,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,0,1,1,1,1,1
        1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1""")
        wall = Maze.Wall(pos=Vector2D(100, 100), scale=Vector2D(50, 50), colour=Colour(101, 67, 33))
        self.player = Explorer(pos=Vector2D(10, 10), scale=Vector2D(10, 10), colour=Main.BLUE, move_speed=1,
                               terrain=self.maze.get_terrain())
        self.player.pos = self.maze.starting_point
        # Add game objects to the scene.
        self.add_object("explorer", self.player, 9)
        #  self.add_object("wall", wall, 4)
        # self.add_object("ball", BouncingBall(pos=Vector2D(225, 225), radius=50, colour=Main.RED), 3)
        for i, wall in enumerate(self.maze.objects):
            self.add_object("wall_" + str(i), wall, 4)

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
        super(BouncingBall, self).update()


class Explorer(Rectangle):
    def __init__(self, pos: Vector2D = (0, 0), scale: Vector2D = (0, 0), colour: Colour = Colour(0, 0, 0),
                 move_speed=2, terrain=[]):
        super().__init__(pos=pos, scale=scale, colour=colour)
        self.move_speed = move_speed
        self.x_velocity = 0
        self.y_velocity = 0
        self.terrian = terrain
        self.direction = [False, False, False, False]

    def update(self):
        self.pos += Vector2D(self.x_velocity, self.y_velocity)
        self.hitbox.pos = self.pos
        self.hitbox.update()
        directions = {
            "LEFT": not self.direction[0] and not self.direction[1] and not self.direction[2] and self.direction[3],
            "UP": self.direction[0] and not self.direction[1] and not self.direction[2] and not self.direction[3],
            "RIGHT": not self.direction[0] and self.direction[1] and not self.direction[2] and not self.direction[3],
            "DOWN": not self.direction[0] and not self.direction[1] and self.direction[2] and not self.direction[3],
            "UP_LEFT": self.direction[0] and not self.direction[1] and not self.direction[2] and self.direction[3],
            "DOWN_LEFT": not self.direction[0] and not self.direction[1] and self.direction[2] and self.direction[3],
            "UP_RIGHT": self.direction[0] and self.direction[1] and not self.direction[2] and not self.direction[3],
            "DOWN_RIGHT": not self.direction[0] and self.direction[1] and self.direction[2] and not self.direction[3],
        }

        indexes = self.hitbox.is_colliding_all(self.terrian)
        for ind in indexes:
            t = self.terrian[ind]
            if self.pos.x < t.pos.x + t.scale.x and directions["LEFT"]:
                self.pos = Vector2D(t.pos.x + t.scale.x, self.pos.y)
            elif self.pos.x + self.scale.x > t.pos.x and directions["RIGHT"]:
                self.pos = Vector2D(t.pos.x - self.scale.x, self.pos.y)
            elif self.pos.y < t.pos.y + t.scale.y and directions["DOWN"]:
                self.pos = Vector2D(self.pos.x, t.pos.y - self.scale.y)
            elif self.pos.y + self.scale.y > t.pos.y and directions["UP"]:
                self.pos = Vector2D(self.pos.x, t.pos.y + t.scale.y)
            elif directions["UP_LEFT"]:
                if abs(self.pos.x - (t.pos.x + t.scale.x)) > abs(self.pos.y - (t.pos.y + t.scale.y)):
                    self.pos = Vector2D(self.pos.x, t.pos.y + t.scale.y)
                elif abs(self.pos.x - (t.pos.x + t.scale.x)) < abs(self.pos.y - (t.pos.y + t.scale.y)):
                    self.pos = Vector2D(t.pos.x + t.scale.x, self.pos.y)
                else:
                    self.pos = Vector2D(t.pos.x + t.scale.x, t.pos.y + t.scale.y)
            elif directions["UP_RIGHT"]:
                if abs((self.pos.x + self.scale.x) - t.pos.x) > abs(self.pos.y - (t.pos.y + t.scale.y)):
                    self.pos = Vector2D(self.pos.x, t.pos.y + t.scale.y)
                elif abs((self.pos.x + self.scale.x) - t.pos.x) < abs(self.pos.y - (t.pos.y + t.scale.y)):
                    self.pos = Vector2D(t.pos.x - self.scale.x, self.pos.y)
                else:
                    self.pos = Vector2D(t.pos.x - self.scale.x, t.pos.y + t.scale.y)
            elif directions["DOWN_LEFT"]:
                if abs(self.pos.x - (t.pos.x + t.scale.x)) > abs((self.pos.y + self.scale.y) - t.pos.y):
                    self.pos = Vector2D(self.pos.x, t.pos.y - self.scale.y)
                elif abs(self.pos.x - (t.pos.x + t.scale.x)) < abs((self.pos.y + self.scale.y) - t.pos.y):
                    self.pos = Vector2D(t.pos.x + t.scale.x, self.pos.y)
                else:
                    self.pos = Vector2D(t.pos.x + t.scale.x, t.pos.y - self.scale.y)
            elif directions["DOWN_RIGHT"]:
                if abs((self.pos.x + self.scale.x) - t.pos.x) > abs((self.pos.y + self.scale.y) - t.pos.y):
                    self.pos = Vector2D(self.pos.x, t.pos.y - self.scale.y)
                elif abs((self.pos.x + self.scale.x) - t.pos.x) < abs((self.pos.y + self.scale.y) - t.pos.y):
                    self.pos = Vector2D(t.pos.x - self.scale.x, self.pos.y)
                else:
                    self.pos = Vector2D(t.pos.x - self.scale.x, t.pos.y - self.scale.y)
        self.x_velocity = 0
        self.y_velocity = 0
        self.direction = [False, False, False, False]
        super().update()

    def update_events(self):
        self.event_handler.trigger("add_key_pressed_callback", pygame.K_RIGHT, self.move_right)
        self.event_handler.trigger("add_key_pressed_callback", pygame.K_LEFT, self.move_left)
        self.event_handler.trigger("add_key_pressed_callback", pygame.K_UP, self.move_up)
        self.event_handler.trigger("add_key_pressed_callback", pygame.K_DOWN, self.move_down)

    def move_right(self):
        self.direction[1] = True
        self.direction[3] = False
        self.x_velocity += self.move_speed

    def move_left(self):
        self.direction[1] = False
        self.direction[3] = True
        self.x_velocity -= self.move_speed

    def move_up(self):
        self.direction[0] = True
        self.direction[2] = False
        self.y_velocity -= self.move_speed

    def move_down(self):
        self.direction[0] = False
        self.direction[2] = True
        self.y_velocity += self.move_speed


class Maze(object):
    def __init__(self, layout):
        self.objects = []
        self.starting_point = Vector2D(0, 0)
        # Build the maze objects.
        f = StringIO(layout)
        reader = csv.reader(f, delimiter=',')
        y_offset = 0
        for row in reader:
            x_offset = 0
            for cell in row:
                x = 7 + (15 * x_offset)
                y = 7 + (15 * y_offset)
                if cell.strip() == '1':
                    self.objects.append(
                        Maze.Wall(pos=Vector2D(x, y), scale=Vector2D(15, 15), colour=Colour(101, 67, 33)))
                if cell.strip() == '2':
                    self.starting_point = Vector2D(x, y)
                x_offset += 1
            y_offset += 1

    def get_terrain(self):
        return [o.hitbox for o in self.objects]

    class Wall(Rectangle):
        def __init__(self, pos: Vector2D = (0, 0), scale: Vector2D = (0, 0), colour: Colour = Colour(0, 0, 0)):
            super().__init__(pos, scale, colour)
