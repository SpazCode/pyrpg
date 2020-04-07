from __future__ import annotations

import pygame
import pygame.gfxdraw
from base import Vector2D, Colour
from base.game_object import UiObject


class Button(UiObject):
    def __init__(self, pos: Vector2D = (0, 0)):
        super().__init__(pos=pos)
        self.click_callback = None
        self.rect = None

    def update(self):
        if self.rect is not None and self.click_callback is not None and self.is_clicked():
            self.click_callback()

    def is_clicked(self) -> bool:
        return pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos())

    def set_on_click_handler(self, callback):
        self.click_callback = callback


class TextButton(Button):
    def __init__(self, pos: Vector2D = Vector2D(0, 0), scale: Vector2D = Vector2D(0, 0),
                 background_colour: Colour = None, border_colour: Colour = None, border_width: int = 1,
                 text: str = None, text_size: int = 32, text_font: str = "freesansbold.ttf",
                 text_colour: Colour = Colour(0, 0, 0)):
        super().__init__(pos)
        self.text_colour: Colour = text_colour
        self.text: str = text
        self.border_width: int = border_width
        self.border_colour: Colour = border_colour
        self.background_colour: Colour = background_colour
        self.scale: Vector2D = scale
        self.font = pygame.font.Font(text_font, text_size)

    def draw(self, screen):
        if self.background_colour is None:
            raise Exception()
        rect_tup = (self.pos.x, self.pos.y, self.scale.x, self.scale.y)
        self.rect = pygame.draw.rect(screen, self.background_colour, rect_tup)
        if self.border_colour is not None:
            self.draw_rect_outline(screen, rect_tup, self.border_colour, self.border_width)
        if self.text is not None:
            text = self.font.render(self.text, True, self.text_colour)
            text_rect = text.get_rect()
            text_rect.center = (self.pos.x + self.scale.x / 2, self.pos.y + self.scale.y / 2)
            screen.blit(text, text_rect)

    @staticmethod
    def draw_rect_outline(screen, rect, color, width=1):
        x, y, w, h = rect
        width = max(width, 1)  # Draw at least one rect.
        width = min(min(width, w // 2), h // 2)  # Don't overdraw.

        # This draws several smaller outlines inside the first outline. Invert
        # the direction if it should grow outwards.
        for i in range(width):
            pygame.gfxdraw.rectangle(screen, (x + i, y + i, w - i * 2, h - i * 2), color)
