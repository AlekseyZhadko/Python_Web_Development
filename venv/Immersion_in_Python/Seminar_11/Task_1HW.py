# Создайте класс Матрица. Добавьте методы для:
# ○ вывода на печать,
# ○ сравнения,
# ○ сложения,
# ○ *умножения матриц
import random


class Matrix:
    """Класс для работы с матрицами."""

    def __init__(self, rows: int, cols: int):
        """Определили метод инициализации экземпляра класса."""
        self.rows = rows
        self.cols = cols
        self.new_matrix = [[random.randint(0, 100) for i in range(rows)] for j in range(cols)]

    def __str__(self):
        """Метод печати экземпляра класса для пользователя."""
        return f'Матрица: {[i for i in self.new_matrix]}'

    def __repr__(self):
        """Метод печати экземпляра класса для программиста."""
        return f' Matrix({self.new_matrix})'

    def __eq__(self, other):
        """Определили метод сравнения на равенство матриц экземпляров класса."""
        count = self.rows * self.cols
        for i in range(self.rows):
            for j in range(self.cols):
                if (self.new_matrix[i][j] == other.new_matrix[i][j]):
                    count -= 1
        return count == 0

    def __add__(self, other):
        """Определили метод сложения матриц экземпляров класса."""
        sum_matrix = [[0 for i in range(self.rows)] for j in range(self.cols)]
        for i in range(self.rows):
            for j in range(self.cols):
                sum_matrix[i][j] = self.new_matrix[i][j] + other.new_matrix[i][j]
        return sum_matrix


if __name__ == '__main__':
    matrix_1 = Matrix(2, 2)
    print(matrix_1)
    print(f'{matrix_1 =}')
    matrix_2 = Matrix(2, 2)
    print(matrix_2)
    print(f'{matrix_2 =}')
    print(matrix_1 == matrix_2)
    print(matrix_1 + matrix_2)