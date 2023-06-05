# ✔ Напишите функцию, которая принимает на вход строку — абсолютный путь до файла. Функция возвращает кортеж из трёх
# элементов: путь, имя файла, расширение файла.

text = "C:/Users/Admin/Desktop/Gb/Python/task.py"


def make_path(text: str) -> tuple[str]:
    *path, file = (i for i in text.split('/'))
    file, expansion = (i for i in file.split('.'))
    return ['/'.join(path), file, expansion]


print(make_path(text))
