# Напишите программу, которая решает квадратные уравнения даже если дискриминант отрицательный.
# ✔ Используйте комплексные числа для извлечения квадратного корня.

def task_5S(a: int, b: int, c: int) -> tuple[complex, complex]:
    d = b ** 2 - 4 * a * c
    x1 = (-b - d ** .5) / 2 / a
    x2 = (-b + d ** .5) / 2 / a
    return x1, x2


print(task_5S(5, -10, -400))
print(task_5S(5, -10, 400))
