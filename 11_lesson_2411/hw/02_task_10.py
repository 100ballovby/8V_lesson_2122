numbers = [4, 5, 7, 2, 63, 2, 34, 1, 9, 92, -16, -7, 12, -11]

low = numbers[0]  # за наименьший беру первый

for element in numbers:  # перебираю каждый элемент списка
    if (element < low) and (element % 2 != 0):  # если какой-то элемент меньше минимального И он нечетный
        low = element  # заменяю минимальный на этот элемент

print(f'Наименьший элемент: {low}')