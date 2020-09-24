import pygame

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_BLUE = (64, 128, 255)
BLUE = (0, 0, 255)
GREEN = (0, 200, 64)
YELLOW = (225, 225, 0)
PINK = (230, 50, 230)
RED = (255, 0, 0)
SKY = (170, 238, 255)
SKIN = (244, 227, 215)

FPS = 30
screen = pygame.display.set_mode((1000, 750))

# outside
pygame.draw.rect(screen, SKY, (0, 0, 1000, 375))
pygame.draw.rect(screen, GREEN, (0, 375, 1000, 750))

# man1
# hands
pygame.draw.line(screen, BLACK, (180, 375), (105, 465))
pygame.draw.line(screen, BLACK, (235, 370), (300, 460))
# feet
pygame.draw.line(screen, BLACK, (190, 520), (150, 630))
pygame.draw.line(screen, BLACK, (150, 630), (125, 631))
pygame.draw.line(screen, BLACK, (230, 520), (245, 625))
pygame.draw.line(screen, BLACK, (245, 625), (285, 629))
# body head
pygame.draw.ellipse(screen, PINK, (160, 350, 100, 200))
pygame.draw.circle(screen, SKIN, (210, 330), 30)

# women1
# hands
pygame.draw.line(screen, BLACK, (300, 460), (410, 380))
pygame.draw.line(screen, BLACK, (430, 370), (470, 410))
pygame.draw.line(screen, BLACK, (470, 410), (520, 380))
# feet
pygame.draw.line(screen, BLACK, (440, 540), (440, 630))
pygame.draw.line(screen, BLACK, (440, 630), (460, 635))
pygame.draw.line(screen, BLACK, (400, 540), (400, 630))
pygame.draw.line(screen, BLACK, (400, 630), (370, 630))
# body head
pygame.draw.polygon(screen, BLUE, [[420, 330], [360, 540],	[490, 540]])
pygame.draw.circle(screen, SKIN, (420, 330), 30)

# women2
# hands
pygame.draw.line(screen, BLACK, (610, 380), (570, 405))
pygame.draw.line(screen, BLACK, (570, 405), (520, 380))
pygame.draw.line(screen, BLACK, (630, 370), (730, 460))
# feet
pygame.draw.line(screen, BLACK, (640, 540), (640, 630))
pygame.draw.line(screen, BLACK, (640, 630), (660, 630))
pygame.draw.line(screen, BLACK, (600, 540), (600, 630))
pygame.draw.line(screen, BLACK, (600, 630), (570, 635))
# body head
pygame.draw.polygon(screen, BLUE, [[620, 330], [560, 540],	[690, 540]])
pygame.draw.circle(screen, SKIN, (620, 330), 30)

# man1
# hands
pygame.draw.line(screen, BLACK, (780, 375), (730, 460))
pygame.draw.line(screen, BLACK, (835, 370), (905, 460))
# feet
pygame.draw.line(screen, BLACK, (790, 520), (750, 630))
pygame.draw.line(screen, BLACK, (750, 630), (725, 631))
pygame.draw.line(screen, BLACK, (830, 520), (845, 625))
pygame.draw.line(screen, BLACK, (845, 625), (885, 629))
# body head
pygame.draw.ellipse(screen, PINK, (760, 350, 100, 200))
pygame.draw.circle(screen, SKIN, (810, 330), 30)

# ice cream1
pygame.draw.polygon(screen, YELLOW, [[900, 460], [912, 370], [970, 410]])
pygame.draw.circle(screen, BLACK, (930, 375), 20)
pygame.draw.circle(screen, RED, (960, 400), 20)
pygame.draw.circle(screen, WHITE, (957, 370), 20)

# balloons
pygame.draw.line(screen, BLACK, (520, 380), (530, 200))
pygame.draw.polygon(screen, YELLOW, [[530, 200], [590, 90], [480, 100]])
pygame.draw.circle(screen, BLACK, (505, 85), 30)
pygame.draw.circle(screen, RED, (563, 80), 30)
pygame.draw.circle(screen, WHITE, (530, 60), 30)

# ice cream2
pygame.draw.line(screen, BLACK, (105, 465), (66, 330))
pygame.draw.polygon(screen, RED, [[66, 330], [23, 250], [100, 240]])
pygame.draw.circle(screen, RED, (80, 230), 25)
pygame.draw.circle(screen, RED, (40, 234), 25)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
