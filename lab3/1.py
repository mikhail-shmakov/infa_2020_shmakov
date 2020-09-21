import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (225, 225, 0)
WHITE = (255, 255, 255)

rect(screen, WHITE, (0, 0, 400, 400))
circle(screen, YELLOW, (200, 200), 150)
circle(screen, RED, (150, 150), 30)
circle(screen, RED, (250, 150), 30)
circle(screen, BLACK, (150, 150), 20)
circle(screen, BLACK, (250, 150), 20)
line(screen, BLACK, [100, 270], [300, 270], 20)
line(screen, BLACK, [50, 50], [180, 130], 15)
line(screen, BLACK, [350, 50], [220, 130], 15)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
