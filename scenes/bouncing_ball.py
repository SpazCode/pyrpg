from __future__ import annotations
from base import Colour, Vector2D
from base.scene import Scene
from objects.ball import Ball
from objects.button import TextButton


class BouncingBallScene(Scene):
    BLACK = Colour(0, 0, 0)
    BLUE = Colour(50, 50, 200)
    WHITE = Colour(255, 255, 255)
    RED = Colour(200, 50, 50)

    def __init__(self):
        super().__init__()
        self.add_game_object("ball", BouncingBall(pos=Vector2D(225, 225), radius=50, colour=BouncingBallScene.RED), 3)
        back_button = TextButton(pos=Vector2D(0, 0), scale=Vector2D(75, 50),
                                 background_colour=BouncingBallScene.BLACK,
                                 border_colour=BouncingBallScene.WHITE, border_width=5, text="< BACK",
                                 text_size=16, text_colour=BouncingBallScene.WHITE)
        back_button.set_on_click_handler(self.switch_scene("main"))
        self.add_ui_object("back", back_button, 1)

    def switch_scene(self, scene):
        return lambda: self.event_handler.trigger("set_scene", scene)

    def update(self):
        self.screen.fill(BouncingBallScene.WHITE)
        super().update()


class BouncingBall(Ball):
    def __init__(self, pos: Vector2D = (0, 0), radius=3, colour: Colour = (0, 0, 0), gravity=3):
        super().__init__(pos, radius, colour)
        self.gravity = gravity
        self.speed = Vector2D(0, 0)
        self.hitbox.visible = True

    def update(self):
        if self.pos.y < 500 - self.radius:
            if self.speed.y < 15:
                self.speed += Vector2D(0, self.gravity)
        else:
            self.speed = Vector2D(0, -50)
        self.pos += self.speed
        super().update()
