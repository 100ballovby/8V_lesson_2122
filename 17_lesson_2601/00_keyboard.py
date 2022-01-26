import pygame as pg

# создаю объект окна программы
s = pg.display.set_mode((640, 480))  # 640pх - ширина и 480px - высота
clock = pg.time.Clock()  # добавление задержки в главный цикл

finished = False
while not finished:
    clock.tick(30)  # частота обновления 30 кадров в секунду
    for event in pg.event.get():  # для каждого события в списке событий
        if event.type == pg.QUIT:
            finished = True
        elif event.type == pg.KEYDOWN:
            print(f'Button "{pg.key.name(event.key)}" pressed!')
            if event.key == pg.K_p:
                s.fill((255, 166, 204))
            elif event.key == pg.K_c:
                s.fill((89, 147, 255))
        elif event.type == pg.KEYUP:
            print(f'Button "{pg.key.name(event.key)}" released!')
            if event.key == pg.K_p:
                s.fill((0, 0, 0))
            elif event.key == pg.K_c:
                s.fill((0, 0, 0))

    pg.display.update()