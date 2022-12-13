import pygame


class UIElement:
    rect: pygame.Rect
    background_color: tuple[int, int, int]
    draw_background: bool

    def __init__(self,
                 rect: pygame.Rect,
                 background_color: tuple[int, int, int] = (0, 0, 0),
                 draw_background: bool = True):

        self.rect = rect
        self.background_color = background_color
        self.draw_background = draw_background

    def draw(self, surface: pygame.Surface):
        if self.draw_background:
            pygame.draw.rect(surface, self.background_color, self.rect)

    def update(self, event: pygame.event.Event):
        pass
