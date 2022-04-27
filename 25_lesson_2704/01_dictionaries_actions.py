person = {
    'name': 'John',
    'surname': 'Doe',
    'city': 'Chicago',
    'email': 'johndoe@example.com',
}  # словарь

# print(person['phone'])  <- ошибка KeyError - обращение к ключу, которого нет

# добавить пару "ключ: значение" в словарь
person['phone'] = '+1 499 555 0100'
print(person)

# замена значения (!!!)
person['name'] = 'Patrick'
print(person)

# удаление пары "ключ: значение"
del person['phone']
print(person)
