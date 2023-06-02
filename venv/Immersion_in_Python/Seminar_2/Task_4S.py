# Напишите программу, которая вычисляет площадь круга и длину окружности по введённому диаметру.
# ✔ Диаметр не превышает 1000 у.е.
# ✔ Точность вычислений должна составлять не менее 42 знаков после запятой.

import math
import decimal


def circle(d: decimal) -> tuple[decimal, decimal]:
    decimal.getcontext().prec = 42
    _pi = decimal.Decimal(math.pi)
    if d <= 1000:
        s = (_pi * d ** 2) / 4
        p = _pi * d
        return decimal.Decimal(s), decimal.Decimal(p)


print(circle(decimal.Decimal(20)))
