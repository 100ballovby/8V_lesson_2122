import pygame as pg
from pygame.draw import rect, circle, polygon  # функции для рисования

screen = pg.display.set_mode((640, 480))
clock = pg.time.Clock()
end = False

rect(screen, (191, 255, 255), [10, 20, 100, 70])
rect(screen, (213, 55, 25), [120, 20, 100, 70], 1)
# где_рисуем, (цвет в RGB), [х, у, ширина, высота], толщина_линии

circle(screen, (91, 51, 178), [50, 150], 30)
circle(screen, (191, 151, 178), [150, 150], 30, 4)
# где_рисуем, (цвет в RGB), [х, у], радиус, толщина_линии

polygon(screen, (67, 89, 111), [[350, 100], [600, 100], [500, 20]])
polygon(screen, (67, 89, 111), [[350, 100], [600, 100], [500, 180]], 3)
# где_рисуем, (цвет в RGB), [[х1, у1], [х2, у2], [х3, у3]], толщина_линии

# рисую узор из квадратов
x_cor = 10
y_cor = 250
for i in range(14):
    rect(screen, (191, 98, 250), [x_cor, y_cor, 40, 40], 4)
    circle(screen, (255, 255, 255), [x_cor + 20, y_cor + 20], 10)
    polygon(screen, (191, 98, 250), [[x_cor, y_cor],
                                     [x_cor + 40, y_cor],
                                     [x_cor + 20, y_cor - 30]])
    polygon(screen, (191, 98, 250), [[x_cor, y_cor + 40],
                                     [x_cor + 40, y_cor + 40],
                                     [x_cor + 20, y_cor + 60]])
    x_cor += 45

pg.display.update()
while not end:
    clock.tick(30)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            end = True

    pg.display.update()
