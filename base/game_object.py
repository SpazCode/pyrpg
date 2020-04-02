from observable import Observable

from base import Vector2D


class GameObject(object):
    """
    Interface for the base objects in a game.
    """
    def __init__(self, pos: Vector2D = (0, 0), scale: Vector2D = (0, 0)):
        self.event_handler = None
        self.pos = pos
        self.scale = scale
        self.exists = True

    # Game logic for this object that needs to be updated every frame.
    def update(self):
        pass

    # Mark this object that is to be terminated.
    def terminate(self):
        self.exists = False

    # How to Draw the object to the screen.
    def draw(self, screen):
        pass

    # Event handler for the current game object.
    def set_event_handler(self, event_handler: Observable):
        self.event_handler = event_handler

    # Update the registered event, trigger events in this method. This is called after the object is added to a scene.
    def update_events(self):
        pass
