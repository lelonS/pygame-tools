import pygame
from ui_classes.ui_element import UIElement


class TextLabel(UIElement):
    _text: str
    _font: pygame.font.Font
    _text_color: tuple[int, int, int]
    _rendered_text: pygame.Surface

    def __init__(self,
                 rect: pygame.Rect,
                 text: str,
                 font: pygame.font.Font,
                 text_color: tuple[int, int, int] = (255, 255, 255),
                 background_color: tuple[int, int, int] = (0, 0, 0),
                 draw_background: bool = True):

        super().__init__(rect, background_color, draw_background)

        self._text = text
        self._font = font
        self._text_color = text_color

    def render_text(self):
        self._rendered_text = self._font.render(
            self._text, True, self._text_color)
        self.rect.size = self._rendered_text.get_size()

    def set_text(self, text: str):
        if text != self._text:
            self._text = text
            self.render_text()

    def set_color(self, color: tuple[int, int, int]):
        if color != self._text_color:
            self._text_color = color
            self.render_text()

    def set_font(self, font: pygame.font.Font):
        if font != self._font:
            self._font = font
            self.render_text()

    def draw(self, surface: pygame.Surface):
        super().draw(surface)
        surface.blit(self._rendered_text, self.rect)
