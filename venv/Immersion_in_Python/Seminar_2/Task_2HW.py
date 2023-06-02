# Напишите программу, которая принимает две строкивида “a/b” — дробь с числителем и знаменателем.
# Программа должна возвращать сумму и *произведение дробей. Для проверки своего кода используйте модуль fractions.
import fractions


def task_2HW(x: str, y: str) -> tuple[str, str]:
    a = x.split('/')
    b = y.split('/')
    if a[1] == b[1]:
        if (int(a[0]) + int(b[0])) % int(a[1]) == 0:
            sum = str((int(a[0]) + int(b[0])) // int(a[1]))
        else:
            sum = str(int(a[0]) + int(b[0])) + '/' + str(int(a[1]))
        div = str(int(a[0]) * int(b[0])) + '/' + str(int(a[1]) * int(b[1]))
    else:
        sum = str(int(a[0]) * int(b[1]) + int(a[1]) * int(b[0])) + '/' + str(int(a[1]) * int(b[1]))
        if (int(a[1]) * int(b[1])) % (int(a[0]) * int(b[0])) == 0:
            z = (int(a[0]) * int(b[0]))
            div = str((int(a[0]) * int(b[0])) // z) + '/' + str((int(a[1]) * int(b[1])) // z)
        else:
            div = str(int(a[0]) * int(b[0])) + '/' + str(int(a[1]) * int(b[1]))
    return sum, div


print('Case 1: a = 1/2, b = 1/2')
print(task_2HW('1/2', '1/2'))
print(fractions.Fraction(1, 2) + fractions.Fraction(1, 2))
print(fractions.Fraction(1, 2) * fractions.Fraction(1, 2))

print('Case 2: a = 4/3, b = 1/3')
print(task_2HW('4/3', '1/3'))
print(fractions.Fraction(4, 3) + fractions.Fraction(1, 3))
print(fractions.Fraction(4, 3) * fractions.Fraction(1, 3))

print('Case 3: a = 1/3, b = 1/2')
print(task_2HW('1/3', '1/2'))
print(fractions.Fraction(1, 3) + fractions.Fraction(1, 2))
print(fractions.Fraction(1, 3) * fractions.Fraction(1, 2))

print('Case 4: a = 2/3, b = 1/2')
print(task_2HW('2/3', '1/2'))
print(fractions.Fraction(2, 3) + fractions.Fraction(1, 2))
print(fractions.Fraction(2, 3) * fractions.Fraction(1, 2))
