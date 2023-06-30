# Создайте класс Сотрудник.
# Воспользуйтесь классом человека из прошлого задания.
# У сотрудника должен быть:
# ○ шестизначный идентификационный номер
# ○ уровень доступа вычисляемый как остаток от деления суммы цифр id на семь
import random


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


class Employee(Human):
    def __init__(self, profession: str, fristname: str, lastname: str, age: int, gender: str):
        super().__init__(fristname, lastname, age, gender)
        self.id = self._gen_number()
        self.sec_level = self._secure_level()
        self.profession = profession

    def _gen_number(self):
        MIN_NUMBER = 1_000_000
        MAX_NUMBER = 10_000_000
        return random.randint(MIN_NUMBER, MAX_NUMBER)

    def _secure_level(self):
        LEVEL_NUM = 7
        sec_id = self.id
        level_num = 0
        while sec_id > 0:
            last_num = sec_id % 10
            level_num += last_num
            sec_id /= 10
        return level_num % LEVEL_NUM

    def __str__(self):
        return f'{self.id} {self.sec_level} {self.profession} {self.fristname} ' \
               f'{self.lastname} {self.get_age()} {self.gender}'


if __name__ == '__main__':
    human_1 = Employee('Master', 'Alex', 'Petrov', 22, 'male')
    print(human_1)