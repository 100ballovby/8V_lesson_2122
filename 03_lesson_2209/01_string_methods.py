# .lower(), .upper()
login = 'zodiac'
login2 = 'Zodiac'
print(login == login2)  # False
print(login2.lower(), login == login2.lower())

print(login.upper())

# .islower(), .isupper(), .isdigit()
print('f'.islower())  # True
print('F'.isupper())  # True
print('3.45'.isdigit())  # False

# .replace(x, y) - заменяет в строке символы х символом y
phrase = 'Привет! Я разработчик!'
print(phrase.replace('а', '@'))
print(phrase.replace('разработчик', 'пианист'))
print(phrase.replace('?', 'пианист'))