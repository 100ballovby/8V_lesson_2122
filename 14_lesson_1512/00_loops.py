"""Функция range() - генератор арифметических последовательностей
range(x) <- 0...x - 1 (x не входит в последовательность)
range(y, x) <- y...x - 1
range(1, 10, 2) <- 1, 3, 5, 7, 9
"""
stop = []
start_stop = []
start_stop_step = []

for i in range(10):  # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
    stop.append(i)  # добавление в список

print(stop)

for i in range(17, 34):  # 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33,
    start_stop.append(i)

print(start_stop)

for i in range(1, 15, 3):  # 1, 4, 7, 10, 13,
    start_stop_step.append(i)

print(start_stop_step)