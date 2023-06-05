# ✔ Функция получает на вход словарь с названием компании в качестве ключа
# и списком с доходами и расходами (3-10 чисел) в качестве значения.
# ✔ Вычислите итоговую прибыль или убыток каждой компании. Если все компании прибыльные, верните истину,
# а если хотя бы одна убыточная — ложь.

def profitable_company(company: dict) -> bool:
    profitable_list = []
    for key, value in company.items():
        profitable_list.append(sum(value))
    return all(map(lambda x: x > 0, profitable_list))


dict_company = {'apple': [12, 13, -5, 4],
                'bork': [-5, 20, 10, -3],
                'samsung': [12, 25, -5, 4], }
print(profitable_company(dict_company))
