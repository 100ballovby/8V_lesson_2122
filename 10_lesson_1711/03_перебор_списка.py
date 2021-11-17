filled_list = [4, 5, 12, 67, 9, 1]

# перебор через индекс
for i in range(len(filled_list)):  # 0 ... <длина списка>
    print(f'Индекс: {i}, элемент: {filled_list[i]}')

# перебор через элемент
for element in filled_list:  # перебираю КАЖДЫЙ элемент списка
    print(element, end=', ')


