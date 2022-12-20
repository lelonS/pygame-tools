import pygame
from ui_classes.ui_element import UIElement, BorderBehavior
from ui_classes.label import TextLabel
from ui_classes.button import TextButton

pygame.init()
screen = pygame.display.set_mode((800, 600))


ui_elements = []

# Create UIElement
ui_element = UIElement(pygame.Rect(10, 10, 200, 200),
                       background_color=(255, 0, 0))
ui_elements.append(ui_element)

# Create TextLabel
text_label = TextLabel(pygame.Rect(220, 10, 200, 200),
                       "Hello World",
                       pygame.font.Font(None, 100),
                       background_color=(0, 255, 0),
                       draw_background=True)

ui_elements.append(text_label)

# Create TextButton
hover_behavior = BorderBehavior((0, 255, 0), 5)
text_button = TextButton(pygame.Rect(430, 10, 200, 200),
                         "Click Me",
                         pygame.font.Font(None, 100),
                         hover_behavior=hover_behavior,
                         on_click=lambda button: print("Clicked!"),
                         border_width=2,
                         border_color=(255, 0, 0),
                         background_color=(100, 0, 123))
ui_elements.append(text_button)

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
