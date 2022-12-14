from ui_classes.ui_element import UIElement
from ui_classes.button import TextButton
import pygame


class TextBox(TextButton):
    focused: bool
    text: str
    default_text: str

    def __init__(self, rect: pygame.Rect, text: str, font: pygame.font.Font, **kwargs):
        super().__init__(rect, text, font, **kwargs)
        self.default_text = text
        self.text = text
