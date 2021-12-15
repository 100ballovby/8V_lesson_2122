"""Посчитать количество цифр в числе"""
number = int(input('Число: '))
count = 0  # счетчик

while number > 0:  # пока number не уменьшился до нуля
    number //= 10
    count += 1

print(f'В числе {count} цифр.')

