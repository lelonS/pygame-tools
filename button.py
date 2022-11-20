import pygame


class Button:
    def __init__(self, x, y, width, height, text, color, text_color, hover_color, font_size, font, on_click):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.text_color = text_color
        self.hover_color = hover_color
        self.font_size = font_size
        self.font = font
        self.on_click = on_click
        self.default_color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        font = pygame.font.SysFont(self.font, self.font_size)
        text = font.render(self.text, True, self.text_color)
        text_rect = text.get_rect(center=self.rect.center)
        screen.blit(text, text_rect)

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.on_click()

    def is_hovered(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            return True
        return False

    def update(self, screen, event):
        if self.is_hovered():
            self.color = self.hover_color
        else:
            self.color = self.default_color
        self.draw(screen)
        self.is_clicked(event)


# Test button
if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    clock = pygame.time.Clock()
    running = True
    button = Button(100, 100, 100, 50, 'Click Me', (255, 255, 255),
                    (0, 0, 0), (0, 0, 255), 20, 'arial', lambda: print('Clicked'))
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            button.update(screen, event)
        pygame.display.update()
        clock.tick(60)
    pygame.quit()
