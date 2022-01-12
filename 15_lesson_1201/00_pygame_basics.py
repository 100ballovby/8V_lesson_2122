import pygame as pg

# настроим окно программы
screen = pg.display.set_mode((640, 480))  # размер окна программы 640x480px
clock = pg.time.Clock()  # отвечает за сменяемость кадров
end = False  # отвечает за работу игры. когда end = True, игра останавливается
a
# если на экране нужно что-то отобразить до начала игры
pg.display.update()  # обновляет кадры на экране
while not end:  # пока игра не окончена
    clock.tick(30)  # задержка сменяемости кадров FPS
    for event in pg.event.get():  # для каждого события в очереди событий
        if event.type == pg.QUIT:  # когда нажали на крестик
            end = True

    pg.display.update()  # обновляю кадры игры внутри цикла
