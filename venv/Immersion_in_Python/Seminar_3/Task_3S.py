# ✔ Создайте вручную кортеж содержащий элементы разных типов.
# ✔ Получите из него словарь списков, где:
# ключ — тип элемента,
# значение — список элементов данного типа

def get_type_dict(corteg: tuple) -> dict:
    result = {}
    for i in corteg:
        result.setdefault(type(i), []).append(i)
    return result


print(get_type_dict((5, 12, 2, 2.22, 2.56, 'Hello')))
