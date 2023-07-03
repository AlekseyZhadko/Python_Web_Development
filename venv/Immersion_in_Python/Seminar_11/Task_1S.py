# Создайте класс Моя Строка, где:
# будут доступны все возможности str
# дополнительно хранятся имя автора строки и время создания (time.time)
from time import time


class MyString(str):
    """Рассширяем класс str."""

    def __new__(cls, value: str, name: str):
        """Расширяем метод new параметрами value и name."""
        instance = super().__new__(cls, value)
        instance.name = name
        instance.created_at = time()
        return instance

    def __str__(self):
        """Метод печати экземпляра класса для пользователя."""
        return f'Текст: {self.name}, Время: {self.created_at}'

    def __repr__(self):
        """Метод печати экземпляра класса для программиста."""
        return f' MySring({self.name}, {self.created_at})'


if __name__ == '__main__':
    mystr = MyString('name', 'text')
    print(mystr)
    print(mystr.name)
    print(mystr.created_at)
    print(mystr.upper())
    help(MyString)
    print(f'{mystr =}')
    print(mystr)
