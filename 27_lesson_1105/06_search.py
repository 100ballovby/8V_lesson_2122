string = 'Hello! There is my first string!'

print('o' in string)  # True
print('Hello!' in string)  # True

signs_count = 0
for symbol in string:
    if symbol in ' !,?.':  # если символ строки находится в строке со специальными симваоолами
        signs_count += 1

print(signs_count)

