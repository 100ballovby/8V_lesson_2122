# написать программу, которая суммирует все числа, вводимые пользователем
summary = 0

for i in range(5):
    n = int(input(f'Введите число №{i + 1}: '))
    summary += n

print(summary)
"""
Инкремент - увеличение с присваиванием (+=, *=, **=)
Декремент - уменьшение с присваиванием (-=, /=, //=, %=)

x = 2 
x *= 6 (x = 12)
x += 7 (x = 19)
x -= 3 (x = 16)
x /= 2 (x = 8)
"""


