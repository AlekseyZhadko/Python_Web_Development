# Создайте класс-функцию, который считает факториал числа при вызове экземпляра.
# Экземпляр должен запоминать последние k значений.
# Параметр k передаётся при создании экземпляра.
# Добавьте метод для просмотра ранее вызываемых значений и их факториалов.
# Создайте менеджер контекста, который при выходе сохраняет значения в JSON файл.
import json


class Fact:
    def __init__(self, k: int):
        self.k = k
        self.save_dict = {}

    def __call__(self, value):
        res = 1
        for i in range(2, value + 1):
            res *= i
            if len(self.save_dict) >= self.k:
                self.save_dict.pop(next(iter(self.save_dict)))
                self.save_dict[i] = res
            else:
                self.save_dict[i] = res
        return self.save_dict

    def __str__(self):
        return f'{self.save_dict}'

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        with open('json_res.json', 'a') as f:
            json.dump(self.save_dict, f)


if __name__ == '__main__':
    with Fact(5) as fact:
        # fact = Fact(5)
        print(fact(5))
        print(fact(6))
        print(fact(7))
        print(fact(8))
        print(fact(9))
        print(fact(10))
        print(fact)
