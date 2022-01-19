import pygame as pg
from pygame.draw import circle, rect, polygon

SKY_BLUE = (230, 254, 255)
GREEN = (40, 176, 81)

WIN_WIDTH = 640
WIN_HEIGHT = 480

s = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
clock = pg.time.Clock()

# рисуем тут

# рисую фон
rect(s, SKY_BLUE, [0, 0, WIN_WIDTH, WIN_HEIGHT * 0.6])
rect(s, GREEN, [0, WIN_HEIGHT * 0.6, WIN_WIDTH, WIN_HEIGHT * 0.4])

pg.display.update()
finished = False
while not finished:
    clock.tick(30)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True