import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Menu Example")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SELECTED = (219, 15, 204)

# Font
font = pygame.font.Font(None, 36)

# Menu items
menu_items = ["Start Game", "Options", "Quit"]
selected_item = 0  # Index of the currently selected item

# Function to display menu items
def display_menu():
    screen.fill("black")
    for i, item in enumerate(menu_items):
        color = WHITE if i != selected_item else SELECTED
        text_surface = font.render(item, True, color)
        text_rect = text_surface.get_rect(center=(WIDTH/2, HEIGHT/2 + i*50))
        screen.blit(text_surface, text_rect)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                selected_item = (selected_item - 1) % len(menu_items)
            elif event.key == pygame.K_DOWN:
                selected_item = (selected_item + 1) % len(menu_items)
            elif event.key == pygame.K_RETURN:
                if selected_item == 0:
                    print("Start Game")
                    # Start your game here
                elif selected_item == 1:
                    print("Options")
                    # Show options menu
                elif selected_item == 2:
                    print("Quit")
                    pygame.quit()
                    sys.exit()
    
    screen.fill("black")

    # Display menu
    display_menu()

    pygame.display.flip()

pygame.quit()
