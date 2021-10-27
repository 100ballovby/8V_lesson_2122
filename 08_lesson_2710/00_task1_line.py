"""Даны числа А и В. Нужно вывести все числа от
А до В включительно, если A < B. Или вывести
в порядке убывания, если A > B."""
a = int(input('введите число: '))  # Ctrl+D
b = int(input('введите число: '))
# 1, 2, 3, 4
if a < b:
    for number in range(a, b + 1):
        print(number)
else:
    for number in range(a, b - 1, -1):
        print(number)

