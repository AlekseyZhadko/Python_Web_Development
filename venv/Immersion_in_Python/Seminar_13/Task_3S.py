# Создайте класс с базовым исключением и дочерние классы исключения:
# ○ ошибка уровня,
# ○ ошибка доступа.
#
# Вспоминаем задачу из семинара 8 про сериализацию данных, где в бесконечном цикле запрашивали имя, личный
# идентификатор и уровень доступа (от 1 до 7) сохраняя информацию в JSON файл.
# Напишите класс пользователя, который хранит эти данные в свойствах экземпляра.
# Отдельно напишите функцию, которая считывает информацию из JSON файла и формирует множество пользователей.
#
# вход в систему - требует указать имя и id пользователя. Для проверки наличия пользователя в множестве используйте
# магический метод проверки на равенство пользователей.
# Если такого пользователя нет, вызывайте исключение доступа. А если пользователь есть, получите его уровень из
# множества пользователей.
# добавление пользователя. Если уровень пользователя меньше, чем ваш уровень, вызывайте исключение уровня доступа.
import json


class CustomException(Exception):
    pass


class LevelError(CustomException):
    pass


class AccessError(CustomException):
    pass


class User:
    def __init__(self, level, user_id, name):
        self.level = level
        self.user_id = user_id
        self.name = name

    def __str__(self):
        return f'{self.level} {self.user_id} {self.name}'

    def __eq__(self, other):
        return self.user_id == other.user_id and self.name == other.name


class Access():
    def __init__(self):
        FILE_NAME = 'data.json'
        self.data = self._parse_data(self._read_json(FILE_NAME))

    def _read_json(self, file_name):
        with open(file_name, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data

    def _parse_data(self, data: dict):
        user_list = []
        for level, dict_users in data.items():
            for user_id, name in dict_users.items():
                user_list.append(User(int(level), int(user_id), name))
        return user_list

    def enter_system(self, user_id: str, name: str):
        temp_user = User(0, user_id, name)
        if temp_user in self.data:
            for user in self.data:
                if temp_user == user:
                    return user.level
        else:
            raise AccessError


if __name__ == '__main__':
    access = Access()
    print(*access.data)
    print(access.enter_system(3, 'Андрей'))
