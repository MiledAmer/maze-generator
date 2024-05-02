import pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Text Rendering Example')

# Set up fonts
font = pygame.font.Font(None, 36)  # Choose the font and font size

# Render text onto a surface
text_surface = font.render('Hello, Pygame!', True, (255, 255, 255))  # Text, antialiasing, color

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the text surface onto the screen
    screen.blit(text_surface, (300, 250))

    # Update the display
    pygame.display.flip()

pygame.quit()
