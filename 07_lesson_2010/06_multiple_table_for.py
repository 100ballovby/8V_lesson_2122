"""Вывести таблицу умножения для числа n в формате:
n * i = z

n = 5
5 * 1 = 5
...
5 * 10 = 50
"""
n = int(input('Введи число: '))

for number in range(1, 11):
    print(f'{n} * {number} = {n * number};')


