
import pygame
from sys import exit
import time

pygame.init()

screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("My First Game")

clock = pygame.time.Clock()

sky_surface = pygame.image.load(
    r'C:\Users\CeBit\Desktop\pygame\images\FRdq8ZbPetwNDRV9R3hYpP-1920-80 (1).jpg'
)

ground_surface = pygame.image.load(
    r'C:\Users\CeBit\Desktop\pygame\images\terrain_7.png'
)

score_font = pygame.font.Font(
    r'C:\Users\CeBit\Downloads\Pixeltype.ttf', 50
)

renderer = score_font.render('My Game', False, 'Green')
score_rect = renderer.get_rect(center = (400,50))
# Load images
player_surf = pygame.image.load(
    r'C:\Users\CeBit\Desktop\pygame\images\player_walk_1.png'
).convert_alpha()

snail_surface = pygame.image.load(
    r'C:\Users\CeBit\Desktop\pygame\images\snail1.png'
).convert_alpha()

# Collision rectangles
player_rect = player_surf.get_rect(topleft=(80, 220))
snail_rect = snail_surface.get_rect(topleft=(600, 270))

gravity = 0
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
         if event.key == pygame.K_SPACE:
            gravity = -20

    # Background
    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(renderer, (score_rect))
    
    # Snail movement
    snail_rect.x -= 4

    if snail_rect.right < 0:
        snail_rect.left = 800

    # Player movement
    if player_rect.colliderect(snail_rect):
        print("collision")

    

    # Draw images
    
    screen.blit(snail_surface, snail_rect)
    #player
    gravity += 1
    player_rect.y += gravity
    screen.blit(player_surf, player_rect)

    # Collision detection
    #mouse_pos = pygame.mouse.get_pos()
    #if player_rect.collidepoint((mouse_pos)):
        #print(pygame.mouse.get_pressed())
    #keys = pygame.key.get_pressed()
    #if keys[pygame.K_SPACE]:
        #print("jump")

    # Debug collision boxes (optional)
    # pygame.draw.rect(screen, 'Red', player_rect, 2)
    # pygame.draw.rect(screen, 'Blue', snail_rect, 2)

    pygame.display.update()
    clock.tick(60)
