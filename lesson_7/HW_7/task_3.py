"""
3. Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка.
В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__()),
вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).Данные методы должны применяться только к клеткам
и выполнять увеличение, уменьшение, умножение и обычное (не целочисленное) деление клеток, соответственно.
В методе деления должно осуществляться округление значения до целого числа.
Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток больше
нуля, иначе выводить соответствующее сообщение.
Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек этих
двух клеток.
Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества
ячеек этих двух клеток.
В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку:
*****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку:
*****\n*****\n*****.
"""


class Error(ValueError):
    def __init__(self, message):
        self.message = f'{message}'


class Nucleus:
    def __init__(self, quantity_cell):
        self.quantity_cell = quantity_cell

    def __add__(self, other):
        return Nucleus(self.quantity_cell + other.quantity_cell)

    def __sub__(self, other):
        diff = self.quantity_cell - other.quantity_cell
        if diff <= 0:
            raise Error('Количество ячеек меньше 0!')
        return Nucleus(diff)

    def __mul__(self, other):
        return Nucleus(self.quantity_cell * other.quantity_cell)

    def __truediv__(self, other):
        if self.quantity_cell == 0 or other.quantity_cell == 0:
            raise Error('Делить на 0 нельзя!')
        return Nucleus(self.quantity_cell // other.quantity_cell)

    def make_order(self, quantity_cell_in_row):
        quantity_cell_in_row = quantity_cell_in_row
        result = ''
        j = 0
        for i in range(self.quantity_cell):
            if j != quantity_cell_in_row:
                result += '*'
                j += 1
            if j == quantity_cell_in_row:
                result += '\n'
                j = 0
        return result


nucleus_1 = Nucleus(12)
nucleus_2 = Nucleus(3)

nucleus_sum = nucleus_1 + nucleus_2
nucleus_diff = nucleus_1 - nucleus_2
nucleus_mull = nucleus_1 * nucleus_2
nucleus_truediv = nucleus_1 / nucleus_2

print(nucleus_sum.quantity_cell)
print(nucleus_diff.quantity_cell)
print(nucleus_mull.quantity_cell)
print(nucleus_truediv.quantity_cell)

print(nucleus_1.make_order(5))
