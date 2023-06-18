# ✔ Напишите функцию, которая открывает на чтение созданные в прошлых задачах файлы с числами и именами.
# ✔ Перемножьте пары чисел. В новый файл сохраните имя и произведение:
# ✔ если результат умножения отрицательный, сохраните имя записанное строчными буквами и произведение по модулю
# ✔ если результат умножения положительный, сохраните имя прописными буквами и произведение округлённое до целого.
# ✔ В результирующем файле должно быть столько же строк, сколько в более длинном файле.
# ✔ При достижении конца более короткого файла, возвращайтесь в его начало

from pathlib import Path
from typing import TextIO


def _read_or_begin(fd: TextIO) -> str:
    line = fd.readline()
    if not line:
        fd.seek(0)
        return _read_or_begin(fd)
    return line[:-1]


def gen_new_file(file_1: Path, file_2: Path, result: Path) -> None:
    with (open(file_1, 'r', encoding='utf-8') as nums,
          open(file_2, 'r', encoding='utf-8') as words,
          open(result, 'w', encoding='utf-8') as res
          ):
        len_numbers = sum(1 for _ in nums)
        len_word = sum(1 for _ in words)
        for _ in range(max(len_numbers, len_word)):
            num = _read_or_begin(nums)
            word = _read_or_begin(words)
            num_a, num_b = num.split('|')
            mult = int(num_a) * float(num_b)
            if mult < 0:
                res.write(f'{word.lower()} {abs(mult)} \n')
            elif mult > 0:
                res.write(f'{word.upper()} {int(mult)} \n')
