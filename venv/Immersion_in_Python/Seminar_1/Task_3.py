# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа должна подсказывать
# “больше” или “меньше” после каждой попытки. Для генерации случайного числа используйте код:
from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1001

num = randint(LOWER_LIMIT, UPPER_LIMIT)
count = 0

start = LOWER_LIMIT
end = UPPER_LIMIT - 1

while count < 10:
    number = int(input(f"Введите число от {start} до {end}: "))
    if number == num:
        print("Вы выиграли!")
        break
    elif number < num:
        print("Введенное число меньше загаданного")
        start = number
    else:
        print("Введенное число больше загаданного")
        end = number
    count += 1
    if count == 10:
        print("Вы проиграли!")
