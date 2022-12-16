"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def division(a, b):
    if a == 0 or b == 0:
        return print("Делить на 0 нельзя!")
    product = a / b
    print(f'{a} / {b} = {product}')
    return product


num1 = int(input("Введите число первое число: "))
num2 = int(input("Введите число второе чсило: "))

division(num1, num2)

# Решение через try \ except

# def division(a, b):
#     try:
#         product = a / b
#     except ZeroDivisionError:
#         return print("Делить на 0 нельзя!")
#     print(f'{a} / {b} = {product}')
#     return product
#
#
# num1 = int(input("Введите число первое число: "))
# num2 = int(input("Введите число второе чсило: "))
#
# division(num1, num2)
