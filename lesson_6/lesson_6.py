"""Класс, объект, атрибут"""


class Car:
    color = 'red'
    model = 'camry'
    __count = 0

    def print_info(self):
        return f'print info - {self.color}, {self.model}'
        # print(self.__form_description())

    # def __form_description(self):
    #      return f'print info - {self.color}, {self.model}'

    def car_returned(self):
        Car.__count -= 1
        print(f'count - {Car.__count}')

    def __str__(self):
        return f'__str__ - {self.color}, {self.model}'

    def __init__(self, color, model):
        self.color = color
        self.model = model
        Car.__count += 1
        print(f'self - {self.color}, {self.model}')
        print(f'count - {Car.__count}')


print(f'class -  {Car.color}, {Car.model}')

test1_car = Car(color='pink', model='bmw')
test2_car = Car(color='blue', model='nissan')
test3_car = Car(color='yellow', model='audi')

# test1_car.print_info()
# test2_car.print_info()
# test3_car.car_returned()
print(test1_car)
# test1_car.print_info()
# test2_car.print_info()
# test3_car.car_returned()

# print(f'count - {Car.__count}')

# Car.__count = 0

# print(f'count - {Car.__count}')


"""Инициализация и методы"""


class Shape:

    def __init__(self, color, param_1, param_2):
        self.color = color
        self.param_1 = param_1
        self.param_2 = param_2

    def square(self):
        return self.param_1 * self.param_2


class Rectangle(Shape):
    def __init__(self, color, param_1, param_2, rectangle_p):
        super().__init__(color, param_1, param_2)
        self.rectangle_p = rectangle_p

    def get_r_p(self):
        return self.rectangle_p


class Triangle(Shape):
    def __init__(self, color, param_1, param_2, triangle_p):
        super().__init__(color, param_1, param_2)
        self.triangle_p = triangle_p

    def get_t_p(self):
        return self.triangle_p


r = Rectangle("white", 10, 20, True)
print(r.color)
print(r.square())
print(r.get_r_p())
t = Triangle("red", 30, 40, False)
print(t.color)
print(t.square())
print(t.get_t_p())

"""Публичный, защищенный, приватный (инкапсуляция)"""

"""Наследование"""

"""Полиморфизм и перегрузка методов"""
