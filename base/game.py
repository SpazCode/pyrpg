import sys

import pygame

from observable import Observable
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
        self.events = Observable()
        self.events_callbacks = {
            pygame.QUIT: lambda: sys.exit()
        }
        self.key_down_callbacks = {}
        self.key_up_callbacks = {}
        self.key_pressed_callbacks = {}
        self.events.on("set_scene", self.set_scene)
        self.events.on("add_key_down_callback", self.add_key_down_callback)
        self.events.on("add_key_up_callback", self.add_key_up_callback)
        self.events.on("add_key_pressed_callback", self.add_key_pressed_callback)

    # Main game loop
    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type in self.events_callbacks.keys():
                    self.events_callbacks[event.type]()
                if event.type == pygame.KEYDOWN:
                    if event.key in self.key_down_callbacks.keys():
                        self.key_down_callbacks[event.key]()
                if event.type == pygame.KEYUP:
                    if event.key in self.key_up_callbacks.keys():
                        self.key_up_callbacks[event.key]()
            keys = pygame.key.get_pressed()
            for key in self.key_pressed_callbacks.keys():
                if keys[key]:
                    self.key_pressed_callbacks[key]()
            if self.current_scene in self.scenes.keys():
                self.scenes[self.current_scene].update()
            pygame.display.flip()
            self.clock.tick(60)
        pygame.quit()

    def quit(self):
        self.running = False

    def set_scene(self, scene_id: str):
        if scene_id not in self.scenes.keys():
            raise SceneIdNotFoundException()
        self.current_scene = scene_id
        self.scenes[self.current_scene].update_events()

    def add_scene(self, scene_id: str, scene: Scene):
        if scene_id in self.scenes.keys():
            raise SceneIdAlreadyInGame()
        scene.set_screen(self.screen)
        scene.set_event_handler(self.events)
        self.scenes[scene_id] = scene

    def add_key_down_callback(self, key, callback):
        if key in self.key_down_callbacks.keys():
            raise Exception("Key is already in set.")
        self.key_down_callbacks[key] = callback

    def add_key_up_callback(self, key, callback):
        if key in self.key_up_callbacks.keys():
            raise Exception("Key is already in set.")
        self.key_up_callbacks[key] = callback

    def add_key_pressed_callback(self, key, callback):
        if key in self.key_pressed_callbacks.keys():
            raise Exception("Key is already in set.")
        self.key_pressed_callbacks[key] = callback
