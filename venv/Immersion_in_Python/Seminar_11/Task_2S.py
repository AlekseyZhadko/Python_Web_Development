# Создайте класс Архив, который хранит пару свойств. Например, число и строку.
# При нового экземпляра класса, старые данные из ранее
# созданных экземпляров сохраняются в пару списковархивов list-архивы также являются свойствами экземпляра

class Archive:
    """Сохраняем данные каждого экземпляра класса в списки numbers и values."""
    numbers = []
    values = []

    def __new__(cls, number: int, value: str):
        """Переопределили метод new для сохранения аргументов в списки."""
        instance = super().__new__(cls)
        cls.numbers.append(number)
        cls.values.append(value)
        return instance

    def __init__(self, number: int, value: str):
        """Определили метод инициализации экземпляра класса."""
        self.number = number
        self.value = value

    def __str__(self):
        """Метод печати экземпляра класса для пользователя."""
        return f'Номер: {self.number}, Значение: "{self.value}"'

    def __repr__(self):
        """Метод печати экземпляра класса для программиста."""
        return f' Archive({self.number}, "{self.value}")'


if __name__ == '__main__':
    a_1 = Archive(1, "Один")
    a_2 = Archive(2, "Два")
    print(f'{a_1.numbers} {a_1.values}')
    print(f'{a_2.numbers} {a_2.values}')
    a_3 = Archive(3, "Три")
    print(f'{a_3.numbers} {a_3.values}')
    help(Archive)
    print(f'{a_1 =}')
    print(a_1)
