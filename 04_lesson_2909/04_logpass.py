"""Написать псевдоклон системы логина"""
# пользовательские данные
login = input('Введите логин: ')
password = input('Введите пароль: ')

# валидные данные
correct_login = 'Zodiac123'
correct_password = '123456qwerty'
'''
Каскадное условие (говнокод)
if login == correct_login:
    if password == correct_password:
        print('Добро пожаловать!') '''
if (login == correct_login) and (password == correct_password):
    # ^ проверка двух выражений: логин правильный И пароль правильный
    print('Добро пожаловать!')
else:  # если что-то не совпадает
    print('Доступ запрещен')



