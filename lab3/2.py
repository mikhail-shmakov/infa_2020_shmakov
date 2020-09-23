import pygame

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

# outside
pygame.draw.rect(screen, (170, 238, 255), (0, 0, 800, 300))
pygame.draw.rect(screen, GREEN, (0, 300, 800, 800))

# man
pygame.draw.ellipse(screen, BLUE, (130, 180, 160, 280))
pygame.draw.circle(screen, WHITE, (210, 150), 50)
# hands
pygame.draw.line(screen, BLACK, [160, 210], [70, 330])
pygame.draw.line(screen, BLACK, [260, 210], [350, 330])
# feet
pygame.draw.line(screen, BLACK, [230, 450], [230, 550])
pygame.draw.line(screen, BLACK, [190, 450], [190, 550])
pygame.draw.line(screen, BLACK, [190, 550], [160, 550])
pygame.draw.line(screen, BLACK, [230, 550], [260, 550])
# ice cream
pygame.draw.polygon(screen, YELLOW, [[90, 350], [40, 330],	[60, 290]])
pygame.draw.circle(screen, WHITE, (40, 320), 15)
pygame.draw.circle(screen, RED, (60, 300), 15)
pygame.draw.circle(screen, BLACK, (40, 300), 15)

# woman
pygame.draw.polygon(screen, PINK, [[550, 180], [450, 450], [650, 450]])
pygame.draw.circle(screen, WHITE, (550, 150), 50)
# hands
pygame.draw.line(screen, BLACK, [540, 210], [350, 330])
pygame.draw.line(screen, BLACK, [560, 210], [620, 260])
pygame.draw.line(screen, BLACK, [620, 260], [700, 220])
# feet
pygame.draw.line(screen, BLACK, [530, 450], [530, 550])
pygame.draw.line(screen, BLACK, [570, 450], [570, 550])
pygame.draw.line(screen, BLACK, [530, 550], [510, 550])
pygame.draw.line(screen, BLACK, [570, 550], [590, 550])
# balloon
pygame.draw.line(screen, BLACK, [690, 250], [720, 140])
pygame.draw.polygon(screen, RED, [[720, 140], [720, 80], [760, 90]])
pygame.draw.circle(screen, RED, (730, 83), 15)
pygame.draw.circle(screen, RED, (750, 88), 15)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
