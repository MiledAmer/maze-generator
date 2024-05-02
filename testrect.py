import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Draw Rectangle")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(WHITE)

    # Draw a rectangle (surface, color, (x, y, width, height), thickness)
    pygame.draw.rect(screen, BLACK, (100, 100, 200, 150), 2)  # Change the dimensions and thickness as needed

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
