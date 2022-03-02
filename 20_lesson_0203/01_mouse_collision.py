import pygame as pg
from pygame.draw import rect, circle, polygon
from random import randint

W = 640
H = 640
screen = pg.display.set_mode((W, H))
clock = pg.time.Clock()

white = (255, 255, 255)
blue = (97, 158, 255)
purple = (227, 143, 255)

x = W // 2
y = H // 2
player = pg.Rect(x, y, 50, 50)

finished = False
while not finished:
    clock.tick(30)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True
        if event.type == pg.MOUSEMOTION:  # если мышь двигается
            if player.collidepoint(event.pos):  # если player касается мыши
                player.x = randint(0, W - 50)
                player.y = randint(0, H - 50)

    screen.fill(white)
    rect(screen, purple, player)  # рисую квадрат на области player
    pg.display.update()