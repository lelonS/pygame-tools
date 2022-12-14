import pygame
from ui_classes.ui_element import UIElement
from ui_classes.label import TextLabel


class Button(UIElement):
    label: TextLabel
    _hovered: bool
    on_click: callable
    on_hover: callable
    on_unhover: callable
