# Создайте класс прямоугольник.
# Класс должен принимать длину и ширину при создании экземпляра.
# У класса должно быть два метода, возвращающие периметр и площадь.
# Если при создании экземпляра передаётся только одна сторона, считаем что у нас квадрат.

class Rectangle:

    def __init__(self, width, heigth=None):
        self.width = width
        self.heigth = heigth if heigth is not None else width

    def perimetr(self):
        return 2 * self.width + 2 * self.heigth

    def square(self):
        return self.width * self.heigth


if __name__ == '__main__':
    rectangle_1 = Rectangle(3, 4)
    rectangle_2 = Rectangle(3)

    print(rectangle_1.perimetr())
    print(rectangle_1.square())
    print(rectangle_2.perimetr())
    print(rectangle_2.square())
