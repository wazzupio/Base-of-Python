"""
4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево)
. А также методы: go, stop, turn(direction), которые должны сообщать,
что машина поехала, остановилась, повернула (куда). Опишите несколько дочерних классов:
TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, который должен показывать текущую
скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Car:

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} поехала')

    def stop(self):
        print(f'{self.name} остановилась')

    def turn(self, direction):
        if direction == 'a':
            print(f'{self.name} повернула налево')
        if direction == 'd':
            print(f'{self.name} повернула направо')

    def show_speed(self):
        print(f'Текущая скорость {self.name}: {self.speed}')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'{self.name} !!! Превышение скорости > 60')
        super().show_speed()


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'{self.name} !!! Превышение скорости > 40')
        super().show_speed()


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, is_police=True)


town = TownCar(speed=50, color='Розовый', name='Сюзана')
town_speedy = TownCar(speed=70, color='Синий', name='Скорость')
sport = SportCar(speed=120, color='Желтый', name='Фурия')
work = WorkCar(speed=40, color='Белый', name='Каблук')
work_speedy = WorkCar(speed=200, color='Черный', name='Работяга')
police = PoliceCar(speed=90, color='Полицейский', name='Патруль')
police_fake = PoliceCar(speed=90, color='Полицейский-Fake', name='Патруль-Fake')
