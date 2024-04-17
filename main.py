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

ball_x = 100
ball_y = 100

dx = 3
dy = 3

# Game loop
while gameIsRunning:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameIsRunning = False

		# Clear the screen
    screen.fill((0, 0, 0))

    ball_x = ball_x + dx
    ball_y = ball_y + dy

    if ball_x+20 >= 800 or ball_x-20 <= 0:
        dx = -dx

    if ball_y + 20 >= 600 or ball_y - 20 <= 0:
        dy = -dy
        
    pygame.draw.circle(screen, (255, 255, 255), (ball_x, ball_y), 20)

    # Flip the display
    pygame.display.flip()

    # Limit the frame rate to 30 FPS
    clock.tick(FPS)


pygame.quit()
sys.exit()