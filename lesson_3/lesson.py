# Примеры встроенных функций (range, ord, sorted)
words = ["banana", "Apple", "berry", "strawberry", "Blueberry", "apricot"]
chars = ['a', 'b', 'c']

words_sorted = sorted(words, key=str.lower)
chars_ord = list(map(ord, chars))

print(words)
print(words_sorted)
print(chars_ord)

# Пример функции
# alice = "Alice"
# b = 'Bob'
#
#
# def print_names(name1, name2="Bob"):
#     print(f'Hello, {name1}! Hello, {name2}!')
#     # return None
#
#
# print_names(alice)


# *args and **kwargs

# def print_many_args(*args):
#     for name in args:
#         print(f'Hello, {name}!')
#
#
# print_many_args('Bill', 'Basil', 'Bob')
#
#
# def print_many_kwargs(**kwargs):
#     for name in kwargs:
#         print(f'Hello, {name, kwargs[name]}!')
#
#
# print_many_kwargs(g1='Alice', g2='Kate', g3='Nelly')


# def user_info(name, mobile, email=None, phone=None):
#     print(f'User info: {name}, {mobile}, {email}, {phone}')
#
#
# user_info('Bob', '000')


# def random_func(x, y):
#     z = x + y
#     return chr(z)
#
#
# print(random_func(25, 36))

# Анонимные функции (lambda) и функция sorted

features = [{'название': 'computer', 'цена': '500', 'количество': '3'},
            {'название': 'tv', 'цена': '200', 'количество': '5'},
            {'название': 'printer', 'цена': '350', 'количество': '1'}]

features_sorted_price = sorted(features, key=lambda x: x['цена'])

prices = list(map(lambda x: x['цена'], features))

print(features_sorted_price)
print(prices)
