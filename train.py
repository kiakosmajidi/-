import pygame
from sys import exit
pygame.init()

screen = pygame.display.set_mode((800,400))
time = pygame.time.Clock()
pygame.display.set_caption("jump!")
icon = pygame.image.load(r"C:\Users\CeBit\Desktop\pygame\images\WIN_20261112_10_44_14_Pro.jpg")
pygame.display.set_icon(icon)
player_surf = pygame.image.load(r"c:\Users\CeBit\Desktop\pygame\images\player_walk_1.png")
player_rect = player_surf.get_rect(topleft = (80,220))
gravity = 0

snail_surf = pygame.image.load(r"C:\Users\CeBit\Desktop\pygame\images\snail1.png")
snail_rect = snail_surf.get_rect(topleft = (600,270))

sky_surf = pygame.image.load(r"C:\Users\CeBit\Desktop\pygame\images\FRdq8ZbPetwNDRV9R3hYpP-1920-80.jpg")
ground_surf = pygame.image.load(r"C:\Users\CeBit\Desktop\pygame\images\terrain_7.png")
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                gravity = -20
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
    
    
    snail_rect.x -= 4
    gravity += 1
    player_rect.y += gravity
    if snail_rect.right < 0:
        snail_rect.left = 800
    if player_rect.colliderect(snail_rect):
        print("collisiojs")
    screen.blit(sky_surf,(0,0))
    screen.blit(ground_surf,(0,300))
    screen.blit(snail_surf,snail_rect)
    screen.blit(player_surf,player_rect)
    time.tick(60)
    pygame.display.update()