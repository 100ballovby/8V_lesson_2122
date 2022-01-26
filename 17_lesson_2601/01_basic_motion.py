import pygame as pg
from pygame.draw import circle

W = 640
H = 480
circle_x = W // 2
circle_y = H // 2
rad = 40

RIGHT = 'right'
LEFT = 'left'
STOP = 'stop'
motion = STOP

s = pg.display.set_mode((W, H))  # 640pх - ширина и 480px - высота
clock = pg.time.Clock()  # добавление задержки в главный цикл

finished = False
while not finished:
    clock.tick(30)  # частота обновления 30 кадров в секунду
    for event in pg.event.get():  # для каждого события в списке событий
        if event.type == pg.QUIT:
            finished = True
        elif event.type == pg.KEYDOWN:  # если нажали на кнопку
            if event.key == pg.K_LEFT:  # и это кнопка стрелка влево
                motion = LEFT
            elif event.key == pg.K_RIGHT:  # и это кнопка стрелка вправо
                motion = RIGHT
        elif event.type == pg.KEYUP:
            if event.key == pg.K_RIGHT or event.key == pg.K_LEFT:
                motion = STOP

    if motion == LEFT:
        circle_x -= 5  # уменьшаю x (иду влево)
    elif motion == RIGHT:
        circle_x += 5  # увеличиваю х (иду вправо)

    s.fill((181, 241, 112))
    circle(s, (0, 76, 234), [circle_x, circle_y], rad)
    pg.display.update()