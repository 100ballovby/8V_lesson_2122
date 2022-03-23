import pygame as pg
from pygame.draw import rect
import random as r

GREEN = (78, 181, 47)
GRAY = (89, 89, 89)
WHITE = (255, 255, 255)
SAND = (255, 243, 204)
RED = (255, 25, 75)

W = 800
H = 720

img = pg.image.load('car.png')
img_rect = img.get_rect()
img_rect.center = W // 2, H * 0.8
car = img
car_rect = img_rect

tree = pg.image.load('tree-3.png')
tree_rect = tree.get_rect()
tree = pg.transform.scale(tree, [W * 0.1, H * 0.2])
tree_rect.x = 20
tree_rect.y = -H * 0.2

car_speed = 0
angle = 0

screen = pg.display.set_mode((W, H))
clock = pg.time.Clock()
end = False

road = pg.Rect(0, 0, W // 2, H)
road.center = W // 2, H // 2
road_width = road.width  # измеряю ширину дороги
left_side = pg.Rect(road.x - road_width * 0.2, 0, road_width * 0.2, H)
right_side = pg.Rect(road.right, 0, road_width * 0.2, H)
paddle1 = pg.Rect(road.x, -50, road_width * 0.3, 30)
paddle2 = pg.Rect(road.x, -H // 2, road_width * 0.3, 30)


def paddle_x(obj, surf):
    x = r.randint(1, 3)
    if x == 1:
        obj.x = surf.x
    elif x == 2:
        obj.center = surf.center
    else:
        obj.right = surf.right


while not end:
    clock.tick(30)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            end = True
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RIGHT:
                car_speed += 10
                angle = -10
            if event.key == pg.K_LEFT:
                car_speed -= 10
                angle = 10
            car = pg.transform.rotate(img, angle)
        if event.type == pg.KEYUP:
            if event.key == pg.K_RIGHT:
                car_speed -= 10
            if event.key == pg.K_LEFT:
                car_speed += 10
            angle = 0
            car = pg.transform.rotate(img, angle)

    screen.fill(GREEN)
    rect(screen, GRAY, road)  # рисую дорогу
    rect(screen, SAND, left_side)  # левая обочина
    rect(screen, SAND, right_side)  # правая обочина
    rect(screen, RED, paddle1)  # первое препятствие
    rect(screen, RED, paddle2)  # второе препятствие

    screen.blit(car, car_rect)
    screen.blit(tree, tree_rect)
    pg.display.update()

    car_rect.x += car_speed
    if car_rect.right >= right_side.left:
        car_rect.right = right_side.left - 5
    if car_rect.left <= left_side.right:
        car_rect.left = left_side.right + 5

    paddle1.y += 10
    if paddle1.y >= H:
        paddle_x(paddle1, road)
        paddle1.y = -50

    paddle2.y += 10
    if paddle2.y >= H:
        paddle_x(paddle2, road)
        paddle2.y = paddle1.y - H // 2

    tree_rect.y += 10
    if tree_rect.y > H:
        tree_rect.y = -H * 0.2



