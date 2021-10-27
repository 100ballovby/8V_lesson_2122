""" Нужно посчитать среднее арифметическое
оценок 10 учеников. Оценки должны вводиться
пользователем. """
summary = 0  # здесь храню числа
students = int(input('Количество учеников: '))
for mark in range(students):
    m = int(input(f'Введите оценку {mark + 1} ученика: '))
    summary += m

print(f'Среднее арифметическое {summary / students}.')

