import random as r

question = input('Задай вопрос: ')
answer = ['Да!', 'Нет!', 'Наверное...', 'Подумай еще.',
          'Не стоит!', 'Определенно, да!']

print(r.choice(answer))  # выбрать случайный ответ из списка ответов и вывести его
