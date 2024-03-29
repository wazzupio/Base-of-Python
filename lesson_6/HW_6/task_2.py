"""
2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна. Использовать формулу:
длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
толщиной в 1 см * число см толщины полотна. Проверить работу метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т
"""


class Road:
    __width = int()
    __length = int()

    def __init__(self, width, length):
        self.__width = width
        self.__length = length

    def weight_asphalt(self, kg=25, h=5):
        return (self.__width * self.__length * kg * h) / 1000


new_road = Road(width=20, length=5000)
print(f'Для покрытия всего дорожного полотна масса асфальта: {new_road.weight_asphalt()} тонн.')
