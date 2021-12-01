import random as r

lst = []
for i in range(30):
    lst.append(r.randint(0, 100))

a = int(input('Старт диапазона: '))
b = int(input('Конец диапазона: '))
count = 0  # считать элементы
summary = 0  # считать сумму

for element in lst:
    #if element in range(a, b + 1):
    if b >= element >= a:
        count += 1
        summary += element

print(lst)
print(f'Сумма элементов: {summary}')
print(f'Количество элементов: {count}')

