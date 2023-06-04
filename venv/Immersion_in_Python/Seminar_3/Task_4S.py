# ✔ Создайте вручную список с повторяющимися элементами.
# ✔ Удалите из него все элементы, которые встречаются дважды.

def not_uniq(numbers: list) -> list:
    return list(filter(lambda x: numbers.count(x) != 2, numbers))


print(not_uniq([1, 2, 3, 4, 5, 6, 1, 2, 6, 12, 12, 15]))
