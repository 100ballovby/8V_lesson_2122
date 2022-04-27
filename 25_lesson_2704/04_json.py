import json

with open('series_SUGAR.json') as file:
    answer = json.loads(file.read())
    # loads() преобразовывает строчку json в словарь (или список)
    sugar_data = answer['data']['rates']

for day in sugar_data:
    try:  # попытаться вывести
        print(f'{day}: {sugar_data[day]["SUGAR"] * 0.453592} кг')
    except KeyError:  # если возникает ошибка KeyError
        pass  # ничего не делать
