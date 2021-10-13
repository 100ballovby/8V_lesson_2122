import random as r

a = r.randint(1, 50)  # Ctrl+D
b = r.randint(1, 50)
c = r.randint(1, 50)

if (a + b > c) and (b + c > a) and (c + a > b):
    print(f'a = {a}, b = {b}, c = {c}')  # буква f перед строкой и {} позволяют вставить значение переменной внутрь строки
    print('Существует!')
else:
    print(f'a = {a}, b = {b}, c = {c}')
    print('Не существует!')

