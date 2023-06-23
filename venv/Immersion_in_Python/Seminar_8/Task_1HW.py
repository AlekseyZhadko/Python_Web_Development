# Напишите функцию, которая получает на вход директорию и рекурсивно
# обходит её и все вложенные директории. Результаты обхода сохраните в
# файлы json, csv и pickle.
# ○ Для дочерних объектов указывайте родительскую директорию.
# ○ Для каждого объекта укажите файл это или директория.
# ○ Для файлов сохраните его размер в байтах, а для директорий размер
# файлов в ней с учётом всех вложенных файлов и директорий.
from pathlib import Path
import os
import json
import csv
import pickle

def dirs(path_dir: str | Path) -> None:
    data = {}
    flag = True
    for dir_path, dir_name, file_names in os.walk(os.getcwd()):
        new_file_names = {}
        for file_name in file_names:
            size_file = os.path.getsize(f'{dir_path}\{file_name}')
            new_file_names[file_name] = f'{size_file} byte'

        new_dir_names = {}
        for dir_nam in dir_name:
            count_files = 0
            count_dirs = 0
            for dir_path_2, dir_name_2, file_names_2 in os.walk(f'{dir_path}\{dir_nam}'):
                count_files += len(file_names_2)
                count_dirs += len(dir_name_2)
            new_dir_names[dir_nam] = f'count dirs: {count_dirs}, count files: {count_files}'

        parents_dir = dir_path.split('\\')[-2]
        if flag:
            flag = False
            data[Path(dir_path).stem] = {'Dir': new_dir_names, 'File': new_file_names}
        else:
            data[f'{parents_dir}\{Path(dir_path).stem}'] = {'Dir': new_dir_names, 'File': new_file_names}

    create_json(data)
    create_pickle(data)
    create_csv(data)


def create_json(data: dict) -> None:
    with open('dirs.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def create_csv(data: dict):
    rows = []
    for path, value in data.items():
        for type, name in value.items():
            rows.append({'path': path, 'type': type, 'info': str(name)})

    with open('out.csv', 'w', newline='', encoding='utf-8') as f:
        fieldnames = ['path', 'type', 'info']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

def create_pickle(data: dict) -> None:
    with open('my_dict.pickle', 'wb') as f:
        pickle.dump(data, f)
