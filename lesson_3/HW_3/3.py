"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""


def my_func(num1, num2, num3):
    if num1 < num2 and num1 < num3:
        return num2 + num3
    if num2 < num1 and num2 < num3:
        return num1 + num3
    if num3 < num1 and num3 < num2:
        return num1 + num2


print(my_func(8, 2, 3))
