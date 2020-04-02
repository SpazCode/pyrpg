# Main pygame class
import sys

from base.game import Game
from scenes.main import Main

if __name__ == "__main__":
    game = Game(config = {
                'x': 510,
                'y': 510
            })
    game.add_scene("main", Main())
    game.set_scene("main")
    game.run()
    sys.exit()
