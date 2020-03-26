# Main pygame class
import pygame

from base.game import Game
from scenes.main import Main

if __name__ == "__main__":
    game = Game()
    game.add_scene("main", Main())
    game.set_scene("main")
    game.run()
