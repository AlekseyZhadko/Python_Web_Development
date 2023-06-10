import random as rnd


def gen_fnc(low: int = 1, hight: int = 100, count: int = 10):
    num = rnd.randint(low, hight + 1)
    search_count = 0
    while search_count < count:
        number = int(input(f"Введите число от {low} до {hight}: "))
        if number == num:
            print("Вы выиграли!")
            break
        elif number < num:
            print("Введенное число меньше загаданного")
            start = number
        else:
            print("Введенное число больше загаданного")
            end = number
        search_count += 1
        if search_count == count:
            print("Вы проиграли!")
