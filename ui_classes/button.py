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
        self.on_click = None
        self.on_hover = None
        self.on_unhover = None
