person = {
    'name': 'John',
    'surname': 'Doe',
    'city': 'Chicago',
    'email': {
        'work': 'johndoe@example.com',
        'private': 'john@company.com'
    },
    'social': [
        {'username': 'JohnTwi',
         'link': 'twitter.com'},
        {'username': 'JohnNagibator',
         'link': 'warthunder.com'},
    ]
}  # словарь

print(person['email']['private'])
print(person['social'])  # получаю список со словарями
print(person['social'][0])  # получаю словарь с ключами и значениями
print(person['social'][0]['username'])  # получаю значение ключа username
