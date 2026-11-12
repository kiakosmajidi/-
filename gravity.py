
import pygame
from sys import exit

pygame.init()

screen = pygame.display.set_mode((800, 400))
clock = pygame.time.Clock()

# Player
player = pygame.Rect(100, 50, 40, 40)

# Physics
gravity = 0.5
velocity_y = 0

bounce_power = -12

ground_y = 300

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Gravity
    velocity_y += gravity
    player.y += velocity_y

    # Ground collision
    if player.bottom >= ground_y:
        player.bottom = ground_y
        velocity_y = bounce_power

    # Draw
    screen.fill('White')

    pygame.draw.rect(screen, 'Red', player)
    pygame.draw.line(screen, 'Black', (0, ground_y), (800, ground_y), 3)

    pygame.display.update()
    clock.tick(60)
