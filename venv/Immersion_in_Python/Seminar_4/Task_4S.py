# ✔ Функция получает на вход список чисел.
# ✔ Отсортируйте его элементы in place без использования встроенных в язык сортировок.
# ✔ Как вариант напишите сортировку пузырьком. Её описание есть в википедии.

def buble_sort(numbers: list[int]) -> list[int]:
    if len(numbers) <= 1:
        return numbers
    for i in range(len(numbers) - 1):
        for j in range(len(numbers) - 1):
            if numbers[j] > numbers[j + 1]:
                temp = numbers[j]
                numbers[j] = numbers[j + 1]
                numbers[j + 1] = temp
    return numbers


print(buble_sort([2, 3, 8, 4, 2]))
