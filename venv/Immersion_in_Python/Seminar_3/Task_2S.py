# Пользователь вводит данные. Сделайте проверку данных и преобразуйте если возможно в один из вариантов ниже:
# ✔ Целое положительное число
# ✔ Вещественное положительное или отрицательное число
# ✔ Строку в нижнем регистре, если в строке есть хотя бы одна заглавная буква
# ✔ Строку в нижнем регистре в остальных случаях

def reformat(text: str) -> (int, float, str):
    result = None
    if text.isdigit():
        result = int(text)
    elif text.count('-') and text.index('-') == 0:
        if text.replace(".", "").replace("-", "").isdigit():
            if text.count('.') > 0:
                result = float(text)
            else:
                result = text.upper()
        else:
            if text.lower() != text:
                result = text.lower()
            else:
                result = text.upper()
    elif text.lower() != text:
        result = text.lower()
    else:
        result = text.upper()
    return result


print(reformat('12'))
print(reformat('-12'))
print(reformat('12.12'))
print(reformat('-12.12'))
print(reformat('heLlo'))
print(reformat('hello'))
print(reformat('hello-world'))
print(reformat('hello.'))
print(reformat('-hello.'))