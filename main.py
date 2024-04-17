import pygame
import sys

# Initialize Pygame
pygame.init()

# Set the dimensions of the window
screen = pygame.display.set_mode((800, 600))

# Set the title of the window
pygame.display.set_caption("My Game")

# Set the FPS
FPS = 30
clock = pygame.time.Clock()

gameIsRunning = True

# Game loop
while gameIsRunning:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameIsRunning = False

		# Clear the screen
    screen.fill((0, 0, 0))

    # Flip the display
    pygame.display.flip()

    # Limit the frame rate to 30 FPS
    clock.tick(FPS)


pygame.quit()
sys.exit()