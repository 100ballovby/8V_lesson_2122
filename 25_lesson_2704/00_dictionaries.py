person = {
    'name': 'John',
    'surname': 'Doe',
    'city': 'Chicago',
    'email': 'johndoe@example.com'
}  # словарь

print(person)  # вывод всего словаря
print(person['email'])  # обращение к элементам словаря происходит по ключам

# вывод всех ключей словаря
for key in person.keys():  # перебрать все ключи словаря
    print(f'Ключ: {key}')

# вывод всех значений словаря
for value in person.values():  # перебрать все значения словаря
    print(f'Значение: {value}')

# вывод ВСЕГО содержимого словаря
for key, value in person.items():  # перебираю одновременно ключ и значения
    print(f'Ключ: "{key}", значение: "{value}".')
