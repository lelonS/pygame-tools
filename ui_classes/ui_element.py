import pygame


'''
x,y
top, left, bottom, right
topleft, bottomleft, topright, bottomright
midtop, midleft, midbottom, midright
center, centerx, centery
'''

TOP_LEFT = 0
TOP_RIGHT = 1
BOTTOM_LEFT = 2
BOTTOM_RIGHT = 3
MID_TOP = 4
MID_LEFT = 5
MID_BOTTOM = 6
MID_RIGHT = 7
CENTER = 8


def get_rect(x, y, width, height, anchor=TOP_LEFT):
    if anchor == TOP_LEFT:
        return pygame.Rect(x, y, width, height)
    elif anchor == TOP_RIGHT:
        return pygame.Rect(x - width, y, width, height)
    elif anchor == BOTTOM_LEFT:
        return pygame.Rect(x, y - height, width, height)
    elif anchor == BOTTOM_RIGHT:
        return pygame.Rect(x - width, y - height, width, height)
    elif anchor == MID_TOP:
        return pygame.Rect(x - width // 2, y, width, height)
    elif anchor == MID_LEFT:
        return pygame.Rect(x, y - height // 2, width, height)
    elif anchor == MID_BOTTOM:
        return pygame.Rect(x - width // 2, y - height, width, height)
    elif anchor == MID_RIGHT:
        return pygame.Rect(x - width, y - height // 2, width, height)
    elif anchor == CENTER:
        return pygame.Rect(x - width // 2, y - height // 2, width, height)
    else:
        raise ValueError('Invalid anchor position')


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
