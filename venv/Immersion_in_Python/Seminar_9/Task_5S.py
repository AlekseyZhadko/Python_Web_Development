# Объедините функции из прошлых задач. Функцию угадайку задекорируйте:
# ○ декораторами для сохранения параметров,
# ○ декоратором контроля значений и
# ○ декоратором для многократного запуска.
# Выберите верный порядок декораторов.
from typing import Callable
import Task_1S as t1
import Task_3S as t3
import Task_4S as t4

@t4.count
@t3.deco
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
