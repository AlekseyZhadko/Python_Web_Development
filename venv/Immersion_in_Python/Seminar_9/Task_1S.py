# Создайте функцию-замыкание, которая запрашивает два целых числа:
# ○ от 1 до 100 для загадывания,
# ○ от 1 до 10 для количества попыток
# Функция возвращает функцию, которая через консоль просит угадать загаданное число за указанное число попыток.

from typing import Callable


def two_numbers(count: int, num: int) -> Callable[[], None]:
    def random_numbers():
        for i in range(1, count + 1):
            user_input = int(input(f'Введите число для отгадывания от 1 до {num}: '))
            if user_input == num:
                print(f'Вы угадали с {i} попытки')
                break
        else:
            print('Вы не угадали')

    return random_numbers


two_numbers(3, 20)()
