import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
win_width = 800
win_height = 600
win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Bouncing Ball")

# Set up the ball
ball_width = 50
ball_height = 50
ball_x = random.randint(0, win_width - ball_width)
ball_y = random.randint(0, win_height - ball_height)
ball_speed = 5
ball_color = (255, 0, 0)

# Set up the game loop
run = True
clock = pygame.time.Clock()

while run:

    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Move the ball
    ball_x += ball_speed
    if ball_x + ball_width > win_width or ball_x < 0:
        ball_speed *= -1
    ball_y += ball_speed
    if ball_y + ball_height > win_height or ball_y < 0:
        ball_speed *= -1

    # Draw the ball
    win.fill((255, 255, 255))
    pygame.draw.rect(win, ball_color, (ball_x, ball_y, ball_width, ball_height))
    pygame.display.update()

    # Delay the game to control the ball speed
    clock.tick(60)

# Quit Pygame
pygame.quit()
quit()
