import pygame
from GameObject import GameObject

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720), vsync = 1)
clock = pygame.time.Clock()
running = True

# Objects setup
player_character = GameObject('little_dino.png', [0, 0], scale_factor=4)

dt = 0

while running:

    # 1) Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_character.set_location(player_character.get_location()[0], player_character.get_location()[1] - 300 * dt)
    if keys[pygame.K_s]:
        player_character.set_location(player_character.get_location()[0], player_character.get_location()[1] + 300 * dt)
    if keys[pygame.K_a]:
        player_character.set_location(player_character.get_location()[0] - 300 * dt, player_character.get_location()[1])
    if keys[pygame.K_d]:
        player_character.set_location(player_character.get_location()[0] + 300 * dt, player_character.get_location()[1])

    # 2) Update game objects/state
    screen.fill((255, 255, 255))
    screen.blit(player_character.surface, player_character.location)


    # 3) Render / Update screen
    pygame.display.flip()


    # 4) Tick
    dt = clock.tick(60)/1000
    dt = max(0.001, min(0.1, dt))
pygame.quit()