""" Перегруза операторов (магические методы) """


class Flat:
    __count_flat = 0

    def __init__(self, rooms):
        self._rooms = rooms
        Flat.__count_flat += 1

    def __len__(self):
        return len(self._rooms)

    def __add__(self, new_room):
        self._rooms.append(new_room)

    def __str__(self):
        return f'There are next rooms: {self._rooms}'


class District:
    __count_district = 0

    def __init__(self, streets):
        self._streets = streets
        District.__count_district += 1

    def __len__(self):
        return len(self._streets)

    def __add__(self, another_district):
        return District(self._streets + another_district._streets)

    def __str__(self):
        return f'There are next streets: {self._streets}'


first_flat = Flat(['kitchen', 'living room'])
first_flat + 'bathroom'
print(len(first_flat))
print(first_flat)

izmaylovo = District(['Izmailovskaya', 'Leninskaya'])
zuzino = District(['Pervomaiskaya', 'Nahimovskiy'])

print(izmaylovo)
print(zuzino)

new_vasuki = izmaylovo + zuzino

print(new_vasuki)

""" Интерфейс """
# from abc import ABC, abstractmethod
#
#
# class DocsForm(ABC):
#     @abstractmethod
#     def get_passport_data(self, passport):
#         pass
#
#     @abstractmethod
#     def get_credit_story(self):
#         pass
#
#
# class VisaForm(DocsForm):
#     def get_passport_data(self, passport):
#         pass
#
#     def get_credit_story(self):
#         pass
#
#     def print_hi(self):
#         return 'Hi!'
#
#
# vasya = VisaForm()
# print(vasya.print_hi())

""" Декоратор """


# def beautiful_print(func):
#     def b_print(*args):
#         print('* * * * * * * * *')
#         func(*args)
#         print('* * * * * * * * *')
#         return None
#     return b_print
#
#
# @beautiful_print
# def print_hello():
#     print('Hello')
#
#
# @beautiful_print
# def my_sum(a, b):
#     print(a + b)
#
#
# print_hello()
# my_sum(1, 2)

""" Декоратор @property """


# class Mine:
#     def __init__(self):
#         self._x = 42
#
#     @property
#     def x(self):
#         print('property')
#         return self._x
#
#     @x.setter
#     def x(self, value):
#         self._x = value
#
#     @x.deleter
#     def x(self):
#         self._x = None
#
#
# test = Mine()
# print(test.x)
#
# test.x = 4
# print(test.x)
#
# del test.x
# print(test.x)


# class TooManyGoods(ValueError):
#     def __init__(self, number, message):
#         result = number - 42
#         self.message = f'{message}. Remove {result}'
#         super().__init__(self.message)
#
#
# class Box:
#     def __init__(self):
#         self.__weight = 0
#
#     @property
#     def weight(self):
#         return self.__weight
#
#     @weight.setter
#     def weight(self, new_weight):
#         if self.__weight + new_weight > 42:
#             raise TooManyGoods(self.__weight + new_weight, 'Remove some box')
#         self.__weight = self.__weight + new_weight
#
#
# b = Box()
# b.weight = 12
# print(b.weight)
# b.weight = 29
# print(b.weight)
# b.weight = 5
# print(b.weight)

""" Интерфейс итерации """


# class Iterator:
#     def __init__(self, end=0):
#         self.i = 0
#         self.end = end
#         self.result = 0
#
#     def __next__(self):
#         self.i += 1
#         self.result += 1
#         if self.i <= self.end:
#             return self.result
#         else:
#             raise StopIteration
#
#     def __iter__(self):
#         return self
#
#
# iter_test = Iterator(5)
# for el in iter_test:
#     print(el)
