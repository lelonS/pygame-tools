import pygame
from ui_classes.ui_element import UIElement
from ui_classes.label import TextLabel

pygame.init()
screen = pygame.display.set_mode((800, 600))


ui_elements = []

# Create UIElement
ui_element = UIElement(pygame.Rect(10, 10, 200, 200), (255, 0, 0))
ui_elements.append(ui_element)

# Create TextLabel
text_label = TextLabel(pygame.Rect(220, 10, 200, 200),
                       "Hello World",
                       pygame.font.Font(None, 100),
                       background_color=(0, 255, 0))

ui_elements.append(text_label)


# Game loop
running = True
while running:
    for event in pygame.event.get():
        for element in ui_elements:
            element.update(event)
        if event.type == pygame.QUIT:
            running = False

    for element in ui_elements:
        element.draw(screen)
    pygame.display.update()

pygame.quit()
