import pygame
from ui_classes.ui_element import UIElement, TOP_LEFT, CENTER, get_rect
from ui_classes.label import TextLabel


class Button(UIElement):
    _hovered: bool
    on_click: callable
    on_hover: callable
    on_unhover: callable

    def __init__(self, rect: pygame.Rect, **kwargs):
        anchor = kwargs.get("anchor", TOP_LEFT)
        background_color = kwargs.get("background_color", (0, 0, 0))
        draw_background = kwargs.get("draw_background", True)

        r = get_rect(rect.x, rect.y, rect.width, rect.height, anchor)
        super().__init__(r, background_color, draw_background)

        self._hovered = False
        self.on_click = kwargs.get("on_click", None)
        self.on_hover = kwargs.get("on_hover", None)
        self.on_unhover = kwargs.get("on_unhover", None)

    def update(self, event: pygame.event.Event):
        super().update(event)
        if event.type == pygame.MOUSEMOTION:
            if self.rect.collidepoint(event.pos):
                if not self._hovered:
                    self._hovered = True
                    if self.on_hover:
                        self.on_hover()
            else:
                if self._hovered:
                    self._hovered = False
                    if self.on_unhover:
                        self.on_unhover()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                if self.on_click:
                    self.on_click()

    def draw(self, surface: pygame.Surface):
        super().draw(surface)
