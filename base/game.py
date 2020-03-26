import sys

import pygame

from base.scene import Scene
from errors import SceneIdNotFoundException, SceneIdAlreadyInGame


class Game(object):
    """
    Game object that represents a currently running game state. Holds the Scenes that are in the game and handles some
    of the global interactions.

    :param config A config object that can be used to define information for the entire game state.
    """

    def __init__(self, config=None):
        if config is None:
            config = {
                'x': 500,
                'y': 500
            }
        pygame.init()
        self.clock = pygame.time.Clock()
        self.running = True
        self.screen = pygame.display.set_mode([config['x'], config['y']])
        self.scenes = {}
        self.current_scene = ''

    # Main game loop
    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            if self.current_scene in self.scenes.keys():
                self.scenes[self.current_scene].update()
            pygame.display.flip()
            print("tick " + str(pygame.time.get_ticks()))
            self.clock.tick(60)
        pygame.quit()

    def quit(self):
        self.running = False

    def set_scene(self, scene_id: str):
        if scene_id not in self.scenes.keys():
            raise SceneIdNotFoundException()
        self.current_scene = scene_id

    def add_scene(self, scene_id: str, scene: Scene):
        if scene_id in self.scenes.keys():
            raise SceneIdAlreadyInGame()
        scene.set_screen(self.screen)
        self.scenes[scene_id] = scene
