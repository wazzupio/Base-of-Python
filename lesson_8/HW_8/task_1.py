"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц,
год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""


class Data:

    @classmethod
    def get_int_el(cls, data):
        data_list_str = data.split('-')
        data_list_int = list(map(int, data_list_str))
        return data_list_int

    @staticmethod
    def validation(data):
        data_list_str = data.split('-')
        data_list_int = list(map(int, data_list_str))
        if data_list_int[1] > 12 or data_list_int[1] < 0:
            print('Месяц указан невено!')
        if data_list_int[2] > 3000 or data_list_int[2] < 1000:
            print('Год указан невено!')


Data.get_int_el('25-01-2023')
Data.validation('25-11-3001')
