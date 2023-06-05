# ✔ Функция получает на вход список чисел и два индекса.
# ✔ Вернуть сумму чисел между между переданными индексами.
# ✔ Если индекс выходит за пределы списка, сумма считается до конца и/или начала списка.

def sum_list(numbers: list, index_start: int, index_out: int) -> int:
    if index_start > 0:
        if index_out < len(numbers):
            return sum(numbers[index_start:index_out])
        else:
            return sum(numbers[index_start:])
    else:
        return sum(numbers[:index_out])

print(sum_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2, 5))
print(sum_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2, 20))
print(sum_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], -3, 5))
print(sum_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], -3, 20))