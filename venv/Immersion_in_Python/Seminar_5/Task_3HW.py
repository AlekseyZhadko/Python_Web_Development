# ✔ Создайте функцию генератор чисел Фибоначчи (см. Википедию).

def fib(n):
    num_1, num_2 = 0, 1
    for _ in range(n):
        yield num_1
        num_1, num_2 = num_2, num_1 + num_2


print(list(fib(10)))
