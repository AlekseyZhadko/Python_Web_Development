# ✔ Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. В результирующем списке
# не должно быть дубликатов.

def uniq(numbers: list) -> list:
    return list(set(numbers) - set(list(filter(lambda x: numbers.count(x) != 2, numbers))))


print(uniq([1, 2, 3, 4, 5, 6, 1, 2, 6, 12, 12, 15]))
