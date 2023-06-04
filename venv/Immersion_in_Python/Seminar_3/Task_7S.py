# ✔ Пользователь вводит строку текста.
# ✔ Подсчитайте сколько раз встречается каждая буква в строке без использования метода count и с ним.
# ✔ Результат сохраните в словаре, где ключ — символ, а значение — частота встречи символа в строке.
# ✔ Обратите внимание на порядок ключей.
# Объясните почему они совпадают или не совпадают в ваших решениях.
from collections import Counter


def get_dict_2(text: str):
    list_word = list(text.lower().replace(' ', ''))
    result = dict(Counter(list_word))
    print(sorted(result.items(), key=lambda x: x[1], reverse=True))


def get_dict(text: str):
    list_word = list(set(text.lower().replace(' ', '')))
    result = {}
    for i in list_word:
        result.setdefault(i, text.count(i))
    print(sorted(result.items(), key=lambda x: x[1], reverse=True))


get_dict('hello world and galaxy')
get_dict_2('hello world and galaxy')
