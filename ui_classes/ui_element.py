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


def get_point_in_rect(rect: pygame.Rect, point: int = TOP_LEFT):
    if point == TOP_LEFT:
        return rect.topleft
    elif point == TOP_RIGHT:
        return rect.topright
    elif point == BOTTOM_LEFT:
        return rect.bottomleft
    elif point == BOTTOM_RIGHT:
        return rect.bottomright
    elif point == MID_TOP:
        return rect.midtop
    elif point == MID_LEFT:
        return rect.midleft
    elif point == MID_BOTTOM:
        return rect.midbottom
    elif point == MID_RIGHT:
        return rect.midright
    elif point == CENTER:
        return rect.center
    else:
        raise ValueError('Invalid anchor position')


class UIElementBehavior:
    def enter(self, sender: 'UIElement'):
        pass

    def exit(self, sender: 'UIElement'):
        pass


class BorderBehavior(UIElementBehavior):
    color: tuple[int, int, int]
    width: int
    original_border_color: tuple[int, int, int]
    original_border_width: int

    def __init__(self, color: tuple[int, int, int], width: int):
        self.color = color
        self.width = width

    def enter(self, sender: 'UIElement'):
        self.original_border_color = sender.border_color
        self.original_border_width = sender.border_width
        sender.border_color = self.color
        sender.border_width = self.width

    def exit(self, sender: 'UIElement'):
        sender.border_color = self.original_border_color
        sender.border_width = self.original_border_width


class UIElement:
    rect: pygame.Rect
    background_color: tuple[int, int, int]
    draw_background: bool
    border_color: tuple[int, int, int]
    border_width: int

    def __init__(self,
                 rect: pygame.Rect,
                 **kwargs):

        self.rect = rect
        self.background_color = kwargs.get("background_color", (0, 0, 0))
        self.draw_background = kwargs.get("draw_background", True)
        self.border_color = kwargs.get("border_color", (0, 0, 0))
        self.border_width = kwargs.get("border_width", 0)

        print(self.rect, self.background_color, self.draw_background)

    def draw(self, surface: pygame.Surface):
        if self.draw_background:
            pygame.draw.rect(surface, self.background_color, self.rect)
        if self.border_width > 0:
            pygame.draw.rect(surface, self.border_color,
                             self.rect, self.border_width)

    def update(self, event: pygame.event.Event):
        pass
