"""
7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""


class ComplexNum:
    def __init__(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2

    # Перегрузка метода сложения. Результатом будет один экземпляр класса со вторыми передаваемыми аргументами.

    def __add__(self, other):
        return ComplexNum(self.num_2, other.num_2)

    # Перегрузка метода умножения. Результатом будет попарное произведение аргументов.

    def __mul__(self, other):
        return ComplexNum(self.num_1 * other.num_1, self.num_2 * other.num_2)

    def __str__(self):
        return f'{self.num_1}, {self.num_2}'


complex_num_1 = ComplexNum(10, 20)
complex_num_2 = ComplexNum(30, 40)

complex_sum = complex_num_1 + complex_num_2
complex_prod = complex_num_1 * complex_num_2

print(complex_sum)
print(complex_prod)
