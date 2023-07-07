# Доработайте класс прямоугольник из прошлых семинаров.
# Добавьте возможность изменять длину и ширину
# прямоугольника и встройте контроль недопустимых значений (отрицательных).
# Используйте декораторы свойств.

class Rectangle:
    """Класс для работы с прямоугольниками."""
    
    __slots__ = ('_width', '_heigth')

    def __init__(self, width, heigth=None):
        """Определили метод инициализации экземпляра класса."""
        self._width = width
        self._heigth = heigth if heigth is not None else width

    @property
    def width(self):
        return self._width

    @property
    def heigth(self):
        return self._heigth

    @width.setter
    def width(self, value):
        if value > 0:
            self._width = value
        else:
            raise ValueError('Ширина должна быть положительной')

    @heigth.setter
    def heigth(self, value):
        if value > 0:
            self._heigth = value
        else:
            raise ValueError('Длина должна быть положительной')

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
