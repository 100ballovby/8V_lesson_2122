import pygame as pg
from pygame.draw import circle

screen = pg.display.set_mode((640, 480))
clock = pg.time.Clock()
end = False

x = 130
y = 240
for i in range(4):
    circle(screen, (143, 143, 143), [x, y], 80, 10)
    x += 120

pg.display.update()
while not end:
    clock.tick(30)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            end = True

    pg.display.update()
