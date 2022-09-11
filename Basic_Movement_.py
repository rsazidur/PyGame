import pygame
pygame.init()

screen = pygame.display.set_mode((500, 500))

pygame.display.set_caption("First Game")

x = 50
y = 50
height = 60
width = 40
vel = 5

run = True
while run:
    pygame.time.delay(100)

    # pygame.event do everything we press and do with our keyboard and mouse
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # with draw. we can draw something like circle or rect anything it took 3 parameter
    pygame.draw.rect(screen, (255, 0, 0), (x, y, height, width))
    # to see the draw.rect we have to update it, so we can do that by
    pygame.display.update()

pygame.quit()
