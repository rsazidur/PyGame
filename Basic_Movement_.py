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
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


pygame.quit()
