from base.game_object import GameObject


class Scene(object):
    """
    Abstract class for the game scenes. Controls the game flow and drawing the game objects to the screen.
    """

    def __init__(self):
        super().__init__()
        # The screen object that the Scene should draw to.
        self.screen = None
        self.objects = {}

    # Update the game logic of all objects in the scene the draw them.
    def update(self):
        for obj in self.objects.values():
            if not obj.instance.exists:
                self.remove_object(obj.name)
            obj.instance.update()
        self.draw()

    # Terminate all objects in the scene then the scene so it can be cleaned up.
    def terminate(self):
        for obj in self.objects.values():
            obj.instance.terminate()
        self.terminate()

    # Draw in order the objects in the scene.
    def draw(self):
        ordered_obj = self.objects.values()
        sorted(ordered_obj, key=lambda o: o.level)
        for obj in ordered_obj:
            obj.instance.draw(self.screen)

    def set_screen(self, screen):
        self.screen = screen

    def add_object(self, name: str, obj: GameObject, level: int):
        self.objects[name] = self.SceneObject(name, obj, level)

    def remove_object(self, name: str):
        self.objects.pop(name)

    class SceneObject(object):
        """
        Wrapper for every object in the scenes.

        @param name The unique name for this object in the scenes.
        @param instance The instance of the game object.
        @param level The depth in the scenes that the object should be drawn at.
        """

        def __init__(self, name: str, instance: GameObject, level: int):
            self.name = name
            self.instance = instance
            self.level = level
