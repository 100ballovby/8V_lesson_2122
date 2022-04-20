with open('pi_million_digits.txt') as file:
    pi_string = ''
    for line in file:
        pi_string += line.strip()  # strip() убирает пробелы по краям строки
    print(pi_string[:52])  # вывести все символы строки до 52

    birthday = input('Введите дату рождения (ДДММГГ): ')  # 120308 <> 12 марта 2008

    if birthday in pi_string:
        print('Дата твоего рождения есть в числе π!')
    else:
        print('Даты твоего рождения нет в числе π. Бот.')


