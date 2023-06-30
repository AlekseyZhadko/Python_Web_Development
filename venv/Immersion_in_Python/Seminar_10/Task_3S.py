# Напишите класс для хранения информации о человеке: ФИО, возраст и т.п. на ваш выбор.
# У класса должны быть методы birthday для увеличения возраста на год, full_name для вывода полного ФИО и т.п. на
# ваш выбор.
# Убедитесь, что свойство возраст недоступно для прямого изменения, но есть возможность получить текущий возраст.

class Human:
    def __init__(self, fristname: str, lastname: str, age: int, gender: str):
        self.fristname = fristname
        self.lastname = lastname
        self.__age = age
        self.gender = gender

    def get_age(self):
        return self.__age

    def birthday(self):
        self.__age += 1

    def full_name(self):
        return self.fristname + self.lastname

    def __str__(self):
        return f'{self.fristname} {self.lastname} {self.get_age()} {self.gender}'

if __name__ == '__main__':
    human_1 = Human('Alex', 'Petrov', 22, 'male')
    print(human_1.get_age())
    print(human_1.birthday())
    print(human_1.get_age())
    print(human_1.full_name())
