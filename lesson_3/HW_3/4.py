"""
4. Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.

Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
"""


# Решение с помощью оператора **
# def my_func(x, y):
#     return x ** y
#
#
# num1 = int(input('Введите положительное число: '))
# num2 = int(input('Введите отрицательное число: '))
#
# print(my_func(num1, num2))


# Решение через анонимную функцию lambda
# print((lambda x, y: x ** y)(int(input('Введите положительное число: ')), int(input('Введите отрицательное число: '))))


#  Решение без оператора **
def my_func(x, y):
    answer = 1
    for i in range(abs(y)):
        answer = answer / x
    return answer


num1 = int(input('Введите положительное число: '))
num2 = int(input('Введите отрицательное число: '))

print(my_func(num1, num2))