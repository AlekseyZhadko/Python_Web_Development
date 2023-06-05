# ✔ Продолжаем развивать задачу 2.
# ✔ Возьмите словарь, который вы получили. Сохраните его итераторатор.
# ✔ Далее выведите первые 5 пар ключ-значение, обращаясь к итератору, а не к словарю.

def dict_chr_ord(text: str) -> dict[str:int]:
    res_iter = iter({i: ord(i) for i in text}.items())
    print(next(res_iter))
    print(next(res_iter))
    print(next(res_iter))
    print(next(res_iter))
    print(next(res_iter))

dict_chr_ord('text task seminar')
