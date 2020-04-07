# Main pygame class
import sys

from base.game import Game
from scenes.bouncing_ball import BouncingBallScene
from scenes.main import Main
from scenes.maze import MazeScene

if __name__ == "__main__":
    game = Game(config={
        'x': 510,
        'y': 510
    })
    game.add_scene("maze", MazeScene())
    game.add_scene("bouncing", BouncingBallScene())
    game.add_scene("main", Main())
    game.set_scene("main")
    game.run()
    sys.exit()
