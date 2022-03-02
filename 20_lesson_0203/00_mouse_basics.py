import pygame as pg
from pygame.draw import rect, circle, polygon

W = 640
H = 640
screen = pg.display.set_mode((W, H))
clock = pg.time.Clock()


finished = False
while not finished:
    clock.tick(30)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True
        if event.type == pg.MOUSEBUTTONDOWN:
            print(f'Нажата кнопка мыши {event.button}')
            print(f'Координаты. X: {event.pos[0]}, Y: {event.pos[1]}')
            x = event.pos[0]
            y = event.pos[1]
            if event.button == 1:  # если нажали на ЛКМ
                screen.fill((255, 0, 0))
                # рисовался квадрат белого цвета в тех координатах, где вы кликнули мышью
                #circle(screen, (255, 255, 255), event.pos, 50)
                polygon(screen, (255, 255, 255), [[x, y], [x + 50, y], [x + 25, y - 60]])
            elif event.button == 2:  # если нажали на колесо
                screen.fill((0, 0, 0))
            elif event.button == 3:  # если нажали на ПКМ
                screen.fill((0, 0, 255))
                #circle(screen, (101, 181, 255), event.pos, 50)
                polygon(screen, (255, 255, 255), [[x, y], [x + 25, y + 60], [x - 25, y + 60]])


    # рисуем тут
    pg.display.update()