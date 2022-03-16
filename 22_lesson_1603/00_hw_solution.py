import pygame as pg
from pygame.draw import rect

GREEN = (78, 181, 47)
GRAY = (89, 89, 89)
WHITE = (255, 255, 255)
SAND = (255, 243, 204)

W = 640
H = 640

img = pg.image.load('car.png')
img_rect = img.get_rect()
img_rect.center = W // 2, H // 2

car = img
car_rect = img_rect

car_speed = 0
angle = 0

screen = pg.display.set_mode((W, H))
clock = pg.time.Clock()
end = False

road = pg.Rect(0, 0, 400, H)
road.center = W // 2, H // 2
left_side = pg.Rect(road.x - 40, 0, 40, H)
right_side = pg.Rect(road.right, 0, 40, H)



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

    screen.blit(car, car_rect)
    rect(screen, (255, 0, 0), car_rect, 1)  # квадрат вокруг машинки
    pg.display.update()

    car_rect.x += car_speed
    if car_rect.right >= right_side.left:
        car_rect.right = right_side.left - 5
    if car_rect.left <= left_side.right:
        car_rect.left = left_side.right + 5



