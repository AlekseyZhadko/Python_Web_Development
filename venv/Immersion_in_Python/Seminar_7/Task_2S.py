# ✔ Напишите функцию, которая генерирует псевдоимена.
# ✔ Имя должно начинаться с заглавной буквы,состоять из 4-7 букв, среди которых обязательно должны быть гласные.
# ✔ Полученные имена сохраните в файл

from pathlib import Path
from random import randint, choice

VOWES = 'qeyuioaj'
CONSTONATS = 'wrtpsdfghklzxcvbnm'
LEN_MIN = 4
LEN_MAX = 7


def gen_name(count: int, file_name: str | Path) -> None:
    with open(file_name, 'a', encoding='utf-8') as f:
        for i in range(count):
            rad_str = ''.join(choice(VOWES) if i % 3 == 0 else choice(CONSTONATS)
                              for j in range(randint(LEN_MIN, LEN_MAX)))
            f.write(f'{rad_str.capitalize()} \n')
