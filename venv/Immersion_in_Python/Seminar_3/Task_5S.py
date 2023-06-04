# ✔ Создайте вручную список с повторяющимися целыми числами.
# ✔ Сформируйте список с порядковыми номерами нечётных элементов исходного списка.
# ✔ Нумерация начинается с единицы.


def my_list_index(numbers: list[int]) -> list[int]:
    return [i for i, j in filter(lambda x: x[1] % 2 != 0, enumerate(numbers, 1))]


print(my_list_index([1, 2, 3, 4, 5, 6, 1, 2, 6, 12, 12, 15]))
