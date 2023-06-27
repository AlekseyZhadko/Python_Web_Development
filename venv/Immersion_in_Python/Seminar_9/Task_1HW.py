# Напишите следующие функции:
# ○ Нахождение корней квадратного уравнения
# ○ Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
# ○ Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
# ○ Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.
import random
import csv
import json

from typing import Callable


def deco(func: Callable):
    def wrapper(*args, **kwargs):
        with open('coefficients.csv', 'r', newline='') as f:
            csv_file = csv.reader(f)
            for i, line in enumerate(csv_file):
                if i != 0:
                    func(int(line[0]), int(line[1]), int(line[2]))
        return

    return wrapper


def deco_json(func: Callable):
    with open(f'{func.__name__}.json', 'r') as f:
        final_dict = json.load(f)

    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print(res)
        final_dict.update({str(res[0]): 'x1: ', str(res[1]): 'x2: '})
        with open(f'{func.__name__}.json', 'w') as f:
            json.dump(final_dict, f, indent=2)
        return func(*args, **kwargs)

    return wrapper


@deco
@deco_json
def roots_quadratic_equation(a: int, b: int, c: int) -> tuple[complex, complex]:
    d = b ** 2 - 4 * a * c
    x1 = (-b - d ** .5) / 2 / a
    x2 = (-b + d ** .5) / 2 / a
    return x1, x2


roots_quadratic_equation()


def create_csv(count_line: int):
    MIN = 0
    MAX = 100
    rows = []
    for i in range(count_line):
        rows.append({'num_a': random.randint(MIN, MAX),
                     'num_b': random.randint(MIN, MAX),
                     'num_c': random.randint(MIN, MAX)})

    with open('coefficients.csv', 'w', newline='', encoding='utf-8') as f:
        fieldnames = ['num_a', 'num_b', 'num_c']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


create_csv(20)
