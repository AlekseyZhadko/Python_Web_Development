# Возьмите 1-3 задачи из тех, что были на прошлых
# семинарах или в домашних заданиях. Напишите к ним классы исключения с выводом подробной информации.
# Поднимайте исключения внутри основного кода. Например нельзя создавать прямоугольник со сторонами отрицательной длины.
import argparse
import logging

class CustomException(Exception):
    pass


class WidthError(CustomException):
    def __init__(self, width):
        self.width = width

    def __str__(self):
        return f'Ширина прямоугольника не должна быть отрицательной. \n' \
                f'Ваше значение {self.width}'

class HeigthError(CustomException):
    def __init__(self, heigth):
        self.heigth = heigth

    def __str__(self):
        return f'Ширина прямоугольника не должна быть отрицательной. \n' \
               f'Ваше значение {self.heigth}'


class Rectangle:
    """Класс для работы с прямоугольниками."""

    __slots__ = ('_width', '_heigth')

    def __init__(self, width, heigth=None):
        """Определили метод инициализации экземпляра класса."""
        FORMAT = '{levelname:<8} - {asctime}. В модуле "{name}" ' \
        'в строке {lineno:03d} функция "{funcName}()" ' \
        'в {created} секунд записала сообщение: {msg}'
        logging.basicConfig(format=FORMAT, style='{', filename='Rectangle.log',
                            filemode='w', encoding='utf-8', level=logging.INFO)
        logger = logging.getLogger('main')
        self._width = width
        if width < 0:
            logger.warning('Введенная ширина отрицательная')
            raise WidthError(self._width)
        self._heigth = heigth if heigth is not None else width
        if self._heigth < 0:
            logger.warning('Введенная длина отрицательная')
            raise HeigthError(self._heigth)

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
            raise WidthError(value)

    @heigth.setter
    def heigth(self, value):
        if value > 0:
            self._heigth = value
        else:
            raise HeigthError(value)

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

    # print(rectangle_1 == rectangle_2)
    # print(rectangle_1 != rectangle_2)
    # print(rectangle_1 > rectangle_2)
    # print(rectangle_1 <= rectangle_2)
    # print(rectangle_1 < rectangle_2)
    # print(rectangle_1 >= rectangle_2)

    # rectangle_3 = Rectangle(-2, 5)
    # rectangle_4 = Rectangle(5, -10)

    parser = argparse.ArgumentParser(description='Rectangle')
    parser.add_argument('param', metavar='width heigth', type=float, nargs=2,
                        help='enter width heigth separated by a space')
    args = parser.parse_args()
    rectangle_5 = Rectangle(*args)
    print(rectangle_5.square())