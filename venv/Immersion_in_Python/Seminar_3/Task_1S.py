# ✔ Вручную создайте список с целыми числами, которые повторяются. Получите новый список, который содержит
# уникальные (без повтора) элементы исходного списка.
# ✔ *Подготовьте два решения, короткое и длинное, которое не использует другие коллекции помимо списков.

def uniq(numbers: list) -> list:
    result = []
    for i in numbers:
        if i not in result:
            result.append(i)
    return result


def uniq_2(numbers: list) -> list:
    return list(set(numbers))


print(uniq([1, 2, 3, 4, 5, 6, 1, 2, 6, 12, 12, 15]))
print(uniq_2([1, 2, 3, 4, 5, 6, 1, 2, 6, 12, 12, 15]))
