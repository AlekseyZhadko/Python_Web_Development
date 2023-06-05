# ✔ Функция получает на вход строку из двух чисел через пробел.
# ✔ Сформируйте словарь, где ключом будет символ из Unicode, а значением — целое число.
# ✔ Диапазон пар ключ-значение от наименьшего из введённых пользователем чисел до наибольшего включительно.

def format_str(text: str) -> dict:
    list_word = list(text.replace(' ', ''))
    result = {}
    for i in list_word:
        result.setdefault(ord(i), i)
    return sorted(result.items(), key=lambda x: x[1])


print(format_str('4 2'))
