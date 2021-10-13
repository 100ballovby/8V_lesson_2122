import math  # самый простой вид импорта

print(math.sqrt(49))  # посчитать квадратный корень

import requests as r  # импортирую библиотеку с именем r

print(r.get('https://vk.com/'))  # обращение к функции только по краткому имени библиотеки

from math import ceil, fabs, factorial, floor, atan, cos

print(fabs(-121))
print(ceil(2.37))

from random import *  # импортировать все
# ^ не используем
print(randint(1, 7))
