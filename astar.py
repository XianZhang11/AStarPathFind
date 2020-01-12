import pygame
import cell as cell

pygame.init()
screen = pygame.display.set_mode((800, 600))
done = False
clock = pygame.time.Clock()

cells = []

opon =[]

close = []


def updateGUI():

    pass
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill((255, 255, 255))
    updateGUI()
    pygame.display.flip()
    clock.tick(60)
