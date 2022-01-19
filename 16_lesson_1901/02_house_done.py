import pygame as pg
from pygame.draw import circle, polygon, rect

FPS = 30  # переменная отвечает за количество кадров в секунду
WIN_WIDTH = 720  # ширина окна
WIN_HEIGHT = 640  # высота окна

# описываю цвета
SKY_BLUE = (206, 255, 254)
BLUE = (121, 132, 255)
BRICK = (243, 203, 162)
DARK_BRICK = (219, 165, 110)
GRASS = (105, 204, 86)
RED = (224, 130, 101)
DARK_RED = (206, 90, 54)
BROWN = (107, 72, 19)
YELLOW = (227, 227, 50)
TREE = (35, 141, 67)
DARK_GREEN = (23, 94, 44)

# настроим окошко программы
screen = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))  # 640px в ширину и 480px в высоту
clock = pg.time.Clock()  # отвечает за сменяемость кадров
pg.display.set_caption('Моя первая игра на PyGame')  # название окошка
finished = False  # флаг, отвечающий за работу игры


# нарисую небо
rect(screen, SKY_BLUE, [0, 0, WIN_WIDTH, WIN_HEIGHT])
# нарисую землю
rect(screen, GRASS, [0, WIN_HEIGHT * 0.6, WIN_WIDTH, WIN_HEIGHT * 0.4])
# нарисую коробку дома
house_x = WIN_WIDTH * 0.2
house_y = WIN_HEIGHT * 0.5
rect(screen, BRICK, [house_x, house_y, 150, 120])
rect(screen, DARK_BRICK, [house_x - 5, house_y - 5, 160, 130], 5)

# нарисую крышу
polygon(screen, RED, [
    [house_x - 30, house_y],
    [house_x + 180, house_y],
    [house_x + 75, house_y - 80]
                      ])
polygon(screen, DARK_RED, [
    [house_x - 35, house_y],
    [house_x + 185, house_y],
    [house_x + 75, house_y - 80]
                      ], 5)

# нарисую дверь
rect(screen, BROWN, [house_x + 40, house_y + 40, 40, 85])
# ручка двери
circle(screen, YELLOW, [house_x + 70, house_y + 90], 4)

# окно
rect(screen, BLUE, [house_x + 100, house_y + 40, 40, 50])
rect(screen, DARK_BRICK, [house_x + 95, house_y + 35, 50, 60], 5)

# солнце
circle(screen, YELLOW, [WIN_WIDTH * 0.8, WIN_HEIGHT * 0.15], 70)

# ёлка
tree_x = WIN_WIDTH * 0.7
tree_y = WIN_HEIGHT * 0.5
for triangle in range(3):
    polygon(screen, TREE, [
        [tree_x, tree_y],
        [tree_x + 100, tree_y],
        [tree_x + 50, tree_y - 70]
    ])
    tree_y += 40
# ствол ёлки
rect(screen, BROWN, [tree_x + 35, tree_y - 40, 30, 50])

# если до начала цикла надо что-то отобразить
pg.display.update()  # обновляем экран

while not finished:  # пока игра не окончена

    clock.tick(FPS)  # задержка

    for event in pg.event.get():  # для каждого события в очереди событий
        if event.type == pg.QUIT:  # если нажали на крестик
            finished = True

    pg.display.update()  # обновляем экран внутри цикла программы

