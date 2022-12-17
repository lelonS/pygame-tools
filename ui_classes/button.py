import pygame
from ui_classes.ui_element import UIElement, TOP_LEFT, CENTER, get_rect
from ui_classes.label import TextLabel


class HoverBehavior:
    def on_hover(self, button: 'Button'):
        pass

    def on_unhover(self, button: 'Button'):
        pass


class HoverBorderColor(HoverBehavior):
    og_border_color: tuple[int, int, int]
    hover_border_color: tuple[int, int, int]

    def __init__(self, hover_border_color: tuple[int, int, int]):
        self.hover_border_color = hover_border_color

    def on_hover(self, button: 'Button'):
        self.og_border_color = button.border_color
        button.border_color = self.hover_border_color

    def on_unhover(self, button: 'Button'):
        button.border_color = self.og_border_color


class Button(UIElement):
    _hovered: bool
    on_click: callable
    hover_behavior: HoverBehavior

    def __init__(self, rect: pygame.Rect, **kwargs):
        anchor = kwargs.get("anchor", TOP_LEFT)

        r = get_rect(rect.x, rect.y, rect.width, rect.height, anchor)
        super().__init__(r, **kwargs)

        self._hovered = False
        self.on_click = kwargs.get("on_click", None)

        self.hover_behavior = kwargs.get("hover_behavior", None)

    def update(self, event: pygame.event.Event):
        super().update(event)
        if event.type == pygame.MOUSEMOTION:
            if self.rect.collidepoint(event.pos):
                if not self._hovered:
                    self._hovered = True
                    if self.hover_behavior:
                        self.hover_behavior.on_hover(self)
            else:
                if self._hovered:
                    self._hovered = False
                    if self.hover_behavior:
                        self.hover_behavior.on_unhover(self)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                if self.on_click:
                    self.on_click(self)

    def draw(self, surface: pygame.Surface):
        super().draw(surface)


class TextButton(Button):
    label: TextLabel

    def __init__(self, rect: pygame.Rect, text: str, font: pygame.font.Font, **kwargs):
        super().__init__(rect, **kwargs)

        text_color = kwargs.get("text_color", (255, 255, 255))
        scale_text = kwargs.get("scale_text", True)
        scale_rect = kwargs.get("scale_rect", False)
        text_anchor = kwargs.get("text_anchor", CENTER)

        self.label = TextLabel(rect, text, font, text_color=text_color,
                               scale_text=scale_text, scale_rect=scale_rect,
                               text_anchor=text_anchor)

    def update(self, event: pygame.event.Event):
        super().update(event)
        self.label.update(event)

    def draw(self, surface: pygame.Surface):
        super().draw(surface)
        self.label.draw(surface)
