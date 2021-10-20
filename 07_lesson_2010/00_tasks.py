month = int(input('Введите номер месяца: '))
year = ('январь', 'февраль', 'март', 'апрель',
        'май', 'июнь', 'июль', 'август',
        'сентябрь', 'октябрь', 'ноябрь', 'декабрь',)

if month in (12, 1, 2):
    if month == 12:
        print(year[11])
    elif month == 1:
        print(year[0])
    else:
        print(year[1])
    print('зима')

elif month in (3, 4, 5):
    print('весна')
elif month in (6, 7, 8):
    print('лето')
elif month in (9, 10, 11):
    print('лето')
else:
    print('Такого номера месяца нет!')
