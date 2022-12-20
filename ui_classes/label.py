import pygame
from ui_classes.ui_element import UIElement, get_rect, get_point_in_rect,\
    TOP_LEFT, CENTER

# TODO - USE CORRECT FONT WHEN RESIZING TO FIT RECT
# TODO - USE KWARGS TO SET DEFAULTS


class TextLabel(UIElement):
    _text: str
    _font: pygame.font.Font
    _text_color: tuple[int, int, int]
    _rendered_text: pygame.Surface

    scale_text: bool
    scale_rect: bool
    text_anchor: int

    def __init__(self,
                 rect: pygame.Rect,
                 text: str,
                 font: pygame.font.Font,
                 **kwargs):

        anchor = kwargs.get("anchor", TOP_LEFT)
        background_color = kwargs.get("background_color", (0, 0, 0))
        draw_background = kwargs.get("draw_background", False)
        text_color = kwargs.get("text_color", (255, 255, 255))
        scale_text = kwargs.get("scale_text", True)
        scale_rect = kwargs.get("scale_rect", False)
        text_anchor = kwargs.get("text_anchor", CENTER)

        r = get_rect(rect.x, rect.y, rect.width, rect.height, anchor)
        super().__init__(r, background_color=background_color, draw_background=draw_background)

        self._text = text
        self._font = font
        self._text_color = text_color
        self.scale_text = scale_text
        self.scale_rect = scale_rect
        self.text_anchor = text_anchor
        self.render_text()

    def render_text(self):
        self._rendered_text = self._font.render(
            self._text, True, self._text_color)
        if self.scale_text:
            self.fit_text_to_rect()
        if self.scale_rect:
            self.rect = self._rendered_text.get_rect()

    def fit_text_to_rect(self):
        w, h = self._rendered_text.get_size()
        r_text = self._rendered_text
        if self._text == "":
            return

        h = self.rect.height * 2
        while w > self.rect.width or h > self.rect.height:
            self._font = pygame.font.Font(None, h - 1)
            r_text = self._font.render(self._text, True, self._text_color)
            w, h = r_text.get_size()
        self._rendered_text = r_text

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
        if self._rendered_text is None:
            return
        x, y = get_point_in_rect(self.rect, self.text_anchor)
        text_rect = get_rect(
            x, y, *self._rendered_text.get_size(), self.text_anchor)
        surface.blit(self._rendered_text, text_rect)


class MultiLineTextLabel(TextLabel):
    _rendered_texts: list[pygame.Surface]
    line_height: int

    def __init__(self,
                 rect: pygame.Rect,
                 text: str,
                 font: pygame.font.Font,
                 **kwargs):

        super().__init__(rect, text, font, **kwargs)

        self.line_height = kwargs.get("line_height", 0)
        self._rendered_text = None
        self._rendered_texts = []
        self.render_texts()

    def render_texts(self):
        self._rendered_texts = []
        for line in self._text.splitlines():
            text = self._font.render(line, True, self._text_color)
            self._rendered_texts.append(text)
        # TODO - SCALE TEXT TO FIT RECT

    def fit_rect_to_text(self):
        pass

    def draw(self, surface: pygame.Surface):
        super().draw(surface)
        for i, text in enumerate(self._rendered_texts):
            x, y = get_point_in_rect(self.rect, self.text_anchor)
            text_rect = get_rect(
                x, y + (i * self.line_height), *text.get_size(), self.text_anchor)
            surface.blit(text, text_rect)
