# ✔ Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
# ✔ Напишите функцию, которая при запуске заменяет содержимое переменных
# оканчивающихся на s (кроме переменной из одной буквы s) на None.
# ✔ Значения не удаляются, а помещаются в одноимённые переменные без s на конце.

def param(s, fgs, ren, fe, ga):
    new_params = {}
    for key, value in locals().items():
        if key != 'new_params':
            if len(key) > 1 and str(key[-1]) == 's':
                new_params.setdefault(key[:-1], None)
                new_params.setdefault(key, value)
            else:
                new_params.setdefault(key, value)
    return new_params


print(param(1, 2, 3, 4, 5))
