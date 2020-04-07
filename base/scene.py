from typing import Dict, NamedTuple

from observable import Observable

from base.game_object import GameObject, UiObject


class Scene(object):
    """
    Abstract class for the game scenes. Controls the game flow and drawing the game objects to the screen.
    """

    def __init__(self):
        super().__init__()
        # The screen object that the Scene should draw to.
        self.screen = None
        self.game_objects: Dict[str, Scene.SceneGameObject] = {}
        self.ui_objects: Dict[str, Scene.SceneUiObject] = {}
        self.event_handler = None

    # Update the game logic of all objects in the scene the draw them.
    def update(self):
        for obj in self.game_objects.values():
            obj.instance.update()
        for obj in self.ui_objects.values():
            obj.instance.update()
        self.draw()

    # Terminate all objects in the scene then the scene so it can be cleaned up.
    def terminate(self):
        for obj in self.game_objects.values():
            obj.instance.terminate()
        self.terminate()

    # Draw in order the objects in the scene.
    def draw(self):
        ordered_obj = list(self.game_objects.values())
        ordered_obj.sort(key=lambda o: o.level)
        for obj in ordered_obj:
            obj.instance.draw(self.screen)
        ordered_obj = list(self.ui_objects.values())
        ordered_obj.sort(key=lambda o: o.level)
        for obj in ordered_obj:
            obj.instance.draw(self.screen)

    def set_screen(self, screen):
        self.screen = screen

    def add_game_object(self, name: str, obj: GameObject, level: int):
        self.game_objects[name] = Scene.SceneGameObject(obj, level)

    def remove_game_object(self, name: str):
        self.game_objects.pop(name)

    def add_ui_object(self, name: str, obj: UiObject, level: int):
        self.ui_objects[name] = Scene.SceneUiObject(obj, level)

    def remove_ui_object(self, name: str):
        self.ui_objects.pop(name)

    def set_event_handler(self, event_handler: Observable):
        self.event_handler = event_handler

    def update_events(self):
        for obj in self.game_objects.values():
            obj.instance.set_event_handler(self.event_handler)
            obj.instance.update_events()
        for obj in self.ui_objects.values():
            obj.instance.set_event_handler(self.event_handler)
            obj.instance.update_events()

    class SceneGameObject(NamedTuple):
        """
        Wrapper for every Game Object in the scenes.

        :param instance The instance of the GameObject.
        :param level The depth in the scenes that the object should be drawn at.
        """
        instance: GameObject
        level: int

    class SceneUiObject(NamedTuple):
        """
        Wrapper for every Ui Object in the scenes.

        :param instance The instance of the UiObject.
        :param level The depth in the scenes that the object should be drawn at.
        """
        instance: UiObject
        level: int
