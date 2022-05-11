string = 'Hello! There is my first string!'

"""
.isupper() - проверяет, является ли символ в строке большой буквой
.islower() - проверяет, является ли символ в строке маленькой буквой
.isdigit() - проверяет, является ли символ в строке цифрой
"""
lower_count = 0
for symbol in string:  # просматриваю каждую букву в строке
    if symbol.islower():  # если символ - маленькая буква
        lower_count += 1

print(lower_count)