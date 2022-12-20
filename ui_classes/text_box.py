from ui_classes.ui_element import UIElement, CENTER, UIElementBehavior
from ui_classes.button import TextButton
from ui_classes.label import TextLabel
import pygame


class TextBox(TextButton):
    focused: bool
    text: str
    text_color: tuple[int, int, int]
    default_text: str
    default_color: tuple[int, int, int]

    label: TextLabel
    default_label: TextLabel

    focus_behavior: UIElementBehavior

    def __init__(self, rect: pygame.Rect, default_text: str, font: pygame.font.Font, **kwargs):
        super().__init__(rect, default_text, font, **kwargs)
        self.default_text = default_text
        self.text = ""

        text_color = kwargs.get("text_color", (255, 255, 255))
        scale_text = kwargs.get("scale_text", False)
        scale_rect = kwargs.get("scale_rect", False)
        text_anchor = kwargs.get("text_anchor", CENTER)
        self.focused = False
        self.focus_behavior = kwargs.get("focus_behavior", None)

        self.label = TextLabel(rect, default_text, font, text_color=text_color,
                               scale_text=scale_text, scale_rect=scale_rect,
                               text_anchor=text_anchor)

        self.default_color = kwargs.get("default_color", text_color)
        self.default_text = kwargs.get("default_text", default_text)

        self.default_label = TextLabel(rect, self.default_text, font, text_color=self.default_color,
                                       scale_text=scale_text, scale_rect=scale_rect,
                                       text_anchor=text_anchor)

    def update(self, event: pygame.event.Event):
        super().update(event)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.focused = True
                if self.focus_behavior:
                    self.focus_behavior.enter(self)
            else:
                self.focused = False
                if self.focus_behavior:
                    self.focus_behavior.exit(self)
        if event.type == pygame.KEYDOWN:
            if self.focused:
                if event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                self.label.set_text(self.text)
                # print(self.text)

    def draw(self, surface: pygame.Surface):
        super().draw(surface)
        if self.text == "":
            self.default_label.draw(surface)
        else:
            self.label.draw(surface)
