import pygame

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((320, 180), vsync = 1)
clock = pygame.time.Clock()
running = True

dt = 0

while running:

    # 1) Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 2) Update game objects/state
    screen.fill((255, 255, 255))


    # 3) Render / Update screen
    pygame.display.flip()


    # 4) Tick
    dt = clock.tick(60)/1000

pygame.quit()