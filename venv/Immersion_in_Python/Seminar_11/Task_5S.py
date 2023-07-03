# Дорабатываем класс прямоугольник из прошлого семинара.
# Добавьте возможность сложения и вычитания.
# При этом должен создаваться новый экземпляр прямоугольника.
# Складываем и вычитаем периметры, а не длинну и ширину.
# При вычитании не допускайте отрицательных значений.
# Добавьте сравнение прямоугольников по площади
# Должны работать все шесть операций сравнения

class Rectangle:
    """Класс для работы с прямоугольниками."""

    def __init__(self, width, heigth=None):
        """Определили метод инициализации экземпляра класса."""
        self.width = width
        self.heigth = heigth if heigth is not None else width

    def perimetr(self):
        """Определили метод вычисления периметра экземпляра класса."""
        return 2 * self.width + 2 * self.heigth

    def square(self):
        """Определили метод вычисления площади экземпляра класса."""
        return self.width * self.heigth

    def __add__(self, other):
        """Определили метод сложения прямоугольников экземпляров класса."""
        new_perimetr = self.perimetr() + other.perimetr()
        new_width = self.width
        new_heigth = new_perimetr / 2 - new_width
        return Rectangle(new_width, new_heigth)

    def __sub__(self, other):
        """Определили метод вычетания прямоугольников экземпляров класса."""
        new_perimetr = abs(self.perimetr() - other.perimetr())
        new_width = min([self.width, self.heigth, other.width, other.heigth])
        new_heigth = new_perimetr / 2 - new_width
        return Rectangle(new_width, new_heigth)

    def __eq__(self, other):
        """Определили метод сравнения на равенство прямоугольников экземпляров класса."""
        return self.square() == other.square()

    def __ne__(self, other):
        """Определили метод сравнения на не равенство прямоугольников экземпляров класса."""
        return self.square() != other.square()

    def __gt__(self, other):
        """Определили метод сравнения на больший прямоугольник экземпляров класса."""
        return self.square() > other.square()

    def __ge__(self, other):
        """Определили метод сравнения на меньший или равный прямоугольник экземпляров класса."""
        return self.square() <= other.square()

    def __lt__(self, other):
        """Определили метод сравнения на меньший прямоугольник экземпляров класса."""
        return self.square() < other.square()

    def __le__(self, other):
        """Определили метод сравнения на больший или равный прямоугольник экземпляров класса."""
        return self.square() >= other.square()

    def __str__(self):
        """Метод печати экземпляра класса для пользователя."""
        return f'Ширина: {self.width}, Высота: {self.heigth}, ' \
               f'Периметр: {self.perimetr()}, Площадь: {self.square()}'

    def __repr__(self):
        """Метод печати экземпляра класса для программиста."""
        return f' Rectangle({self.width}, {self.heigth}, {self.perimetr()}, {self.square()})'


if __name__ == '__main__':
    rectangle_1 = Rectangle(2, 5)
    rectangle_2 = Rectangle(5, 10)

    print(rectangle_1.perimetr())
    print(rectangle_1.square())
    print(rectangle_2.perimetr())
    print(rectangle_2.square())

    res_sum = rectangle_1 + rectangle_2
    print(res_sum.width, res_sum.heigth)
    res_sub = rectangle_1 - rectangle_2
    print(res_sub.width, res_sub.heigth)
    print(rectangle_1 == rectangle_2)
    print(rectangle_1 != rectangle_2)
    print(rectangle_1 > rectangle_2)
    print(rectangle_1 <= rectangle_2)
    print(rectangle_1 < rectangle_2)
    print(rectangle_1 >= rectangle_2)

    print(rectangle_1)
