array = [1, 5, 0, 2, 6, 7, 0, 8, 11, 0]
# заменить нули на None
for index in range(len(array)):  # по индексам
    if array[index] == 0:  # если элемент списка с индексом равен 0
        array[index] = None  # заменить его на None

print(array)
