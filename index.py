import pygame

# Initialize Pygame
pygame.init()

# Set the screen dimensions
screen_width = 800
screen_height = 600
clock = pygame.time.Clock()
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the window title
pygame.display.set_caption("My Python Game Screen")

# Set the background color
background_color = (255, 255, 255)

# Start the main game loop
running = True
while running:
    # Clear the screen with the background color
    screen.fill(background_color)

    # Process events (keyboard, mouse, etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the screen
    pygame.display.flip()
    clock.tick(60)

# Quit Pygame
pygame.quit()