"""
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix(двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с
первым элементом первой строки второй матрицы и т.д.
"""


class Matrix:
    def __init__(self, my_list):
        self.my_list = my_list

    def __str__(self):
        my_matrix_str = ''
        for i in range(len(self.my_list)):
            for j in self.my_list[i]:
                my_matrix_str += str(j) + ' '
            my_matrix_str += '\n'
        return my_matrix_str

    def __add__(self, other):
        quantity_pow = len(self.my_list)
        quantity_column = len(self.my_list[0])
        my_matrix = [[0] * quantity_column for _ in range(quantity_pow)]
        for i in range(len(self.my_list)):
            for j in range(len(self.my_list[i])):
                my_matrix[i][j] = self.my_list[i][j] + other[i][j]
        return Matrix(my_matrix)

    def __getitem__(self, item):
        return self.my_list[item]


my_matrix_1 = Matrix([[1, 10, 3], [2, 3, 50], [5, 11, 100]])
my_matrix_2 = Matrix([[2, 11, 4], [3, 4, 51], [6, 12, 101]])

my_matrix_sum = my_matrix_1 + my_matrix_2

print(my_matrix_sum)
