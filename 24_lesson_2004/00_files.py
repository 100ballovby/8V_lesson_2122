with open('pi_digits.txt') as file:
    # открыть файл и присвоить его переменной file
    # file.read() <- чтение файла (вывод его содержимого)
    pi_string = ''
    for line in file:
        pi_string += line.strip()  # strip() убирает пробелы по краям строки
    print(pi_string)
    print(f'Тип данных: {type(pi_string)}')


