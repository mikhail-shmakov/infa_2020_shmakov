import pygame
from pygame.draw import *

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
LIGHT_BLUE = (64, 128, 255)
BLUE = (0, 0, 255)
GREEN = (0, 200, 64)
YELLOW = (225, 225, 0)
PINK = (230, 50, 230)
RED = (255, 0, 0)

FPS = 30
screen = pygame.display.set_mode((800, 600))

rect(screen, LIGHT_BLUE, (0, 0, 800, 300))
rect(screen, GREEN, (0, 300, 800, 800))
ellipse(screen, BLUE, (130, 180, 160, 280))
circle(screen, WHITE, (210, 150), 50)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
