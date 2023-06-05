# ✔ Напишите функцию, которая принимает строку текста.
# ✔ Сформируйте список с уникальными кодами Unicode каждого символа введённой строки отсортированный по убыванию.

def get_dict(text: str) -> list:
    result = set()
    for i in text:
        result.add(ord(i))
    return sorted(result, reverse=True)


print(get_dict('hello world and galaxy'))
