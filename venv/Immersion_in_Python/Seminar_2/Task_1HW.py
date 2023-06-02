# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное
# строковое представление. Функцию hex используйте для проверки своего результата.

def task_3S(num: int, mode: int) -> str:
    result: str = ''
    while num >= 1:
        res = num % mode
        match res:
            case 10:
                result = "a" + result
            case 11:
                result = "b" + result
            case 12:
                result = "c" + result
            case 13:
                result = "d" + result
            case 14:
                result = "e" + result
            case 15:
                result = "f" + result
            case _:
                result = str(res) + result
        num //= mode
    return result


print(hex(1234567))
print(task_3S(1234567, 16))
