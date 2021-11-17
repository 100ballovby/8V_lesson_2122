number = input('Введите число: ')
mult = 1

for digit in number:  # перебираю каждую цифру числа (число сейчас строчка)
    print(f'{mult} * {digit} = {mult * int(digit)}')
    mult *= int(digit)  # привожу каждое цифру в целочисленный вид (меняю тип данных)


