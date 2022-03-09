import pygame as pg
from pygame.draw import rect, circle, polygon

W = 1200
H = 700
screen = pg.display.set_mode((W, H))
clock = pg.time.Clock()

img = pg.image.load('pikachu.png').convert_alpha()  # загружаю картинку
img_rect = img.get_rect()  # включить коллизию картинке
img_rect.center = W // 2, H // 2  # поставить изображение посередине

img1 = img
img_rect1 = img_rect
angle = 0
scale = 1

finished = False
while not finished:
    clock.tick(30)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True

    keys = pg.key.get_pressed()
    if keys[pg.K_w]:
        img_rect.y -= 3
    elif keys[pg.K_s]:
        img_rect.y += 3
    elif keys[pg.K_d]:
        img_rect.x += 3
    elif keys[pg.K_a]:
        img_rect.x -= 3
    elif keys[pg.K_e]:
        angle += 1
        img1 = pg.transform.rotozoom(img, angle, scale)   # вращает изображение на градус angle
    elif keys[pg.K_q]:
        angle -= 1
        img1 = pg.transform.rotozoom(img, angle, scale)
    elif keys[pg.K_m]:
        scale *= 1.1
        img1 = pg.transform.rotozoom(img, angle, scale)  # увеличивать картинку
    elif keys[pg.K_n]:
        scale /= 1.1
        img1 = pg.transform.rotozoom(img, angle, scale)

    screen.fill((255, 255, 255))
    screen.blit(img1, img_rect1)
    pg.display.update()