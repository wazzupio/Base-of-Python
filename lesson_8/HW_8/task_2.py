"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в качестве
делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class MyError(Exception):
    def __init__(self, txt):
        self.txt = txt


first_num = int(input('Введите первое число: '))
second_num = int(input('Введите второе число: '))

try:
    result = first_num / second_num
    if first_num == 0 or second_num == 0:
        raise MyError('Нельзя делить на 0!!!')
except MyError as err:
    print(err)
else:
    print(result)
