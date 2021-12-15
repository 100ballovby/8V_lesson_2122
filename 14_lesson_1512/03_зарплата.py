persons = ['Иван', 'Олег', 'Петр']
fee = []

for i in persons:  # перебираю имена в списке
    a = int(input(f'Введите з/п {i}а: '))
    fee.append(a)

print(f'Разница: {max(fee) - min(fee)}')

