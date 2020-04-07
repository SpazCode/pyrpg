from __future__ import annotations
from base import Colour, Vector2D
from base.scene import Scene
from objects.button import TextButton


class Main(Scene):
    BLACK = Colour(0, 0, 0)
    BLUE = Colour(50, 50, 200)
    WHITE = Colour(255, 255, 255)
    RED = Colour(200, 50, 50)

    def __init__(self):
        super().__init__()
        maze_button = TextButton(pos=Vector2D(105, 150), scale=Vector2D(300, 100), background_colour=Main.BLUE,
                                 border_colour=Main.RED, border_width=5, text="Play the Maze")
        maze_button.set_on_click_handler(self.switch_scene("maze"))
        self.add_ui_object("maze", maze_button, 1)
        ball_button = TextButton(pos=Vector2D(105, 260), scale=Vector2D(300, 100), background_colour=Main.BLUE,
                                 border_colour=Main.RED, border_width=5, text="Play the Bouncing Ball", text_size=26)
        ball_button.set_on_click_handler(self.switch_scene("bouncing"))
        self.add_ui_object("ball", ball_button, 1)

    def switch_scene(self, scene):
        return lambda: self.event_handler.trigger("set_scene", scene)

    def update(self):
        self.screen.fill(Main.WHITE)
        super().update()
