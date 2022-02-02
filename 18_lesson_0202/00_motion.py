import pygame as pg
from pygame.draw import rect
from random import randrange  # случайный промежуток

pg.font.init()  # чтобы отображался текст на экране
score_font = pg.font.SysFont('comicsans', 20)
# делаем переменную для шрифта (название, размер)

score = 0  # очки

W = 640
H = 480
screen = pg.display.set_mode((W, H))
clock = pg.time.Clock()

RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

x1 = 200
y1 = 200
block = 10

enemy_x = round(randrange(0, W - block) / 10) * 10
enemy_y = round(randrange(0, H - block) / 10) * 10

x_change = 0
y_change = 0

finished = False
while not finished:
    clock.tick(25)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RIGHT:
                x_change = block
                y_change = 0
            elif event.key == pg.K_LEFT:
                x_change = -block
                y_change = 0
            elif event.key == pg.K_UP:
                x_change = 0
                y_change = -block
            elif event.key == pg.K_DOWN:
                x_change = 0
                y_change = block

    x1 += x_change
    y1 += y_change

    screen.fill(WHITE)
    rect(screen, BLUE, [x1, y1, block, block])
    rect(screen, RED, [enemy_x, enemy_y, block, block])

    if x1 == enemy_x and y1 == enemy_y:
        enemy_x = round(randrange(0, W - block) / 10) * 10
        enemy_y = round(randrange(0, H - block) / 10) * 10

        score += 1

    show_score = score_font.render(f'Your score: {score}', True, (0, 0, 0))
    screen.blit(show_score, [0, 0])

    if (x1 >= W or x1 < 0) or (y1 >= H or y1 < 0):
        finished = True

    pg.display.update()
