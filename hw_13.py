# Написать класс и реализовать его методы: (основа - ДЗ № 11)

import os

from utils.files import create_empty_file, create_dir


class WorkWithFolder:
    # 1. Инициализация класса с одним параметром - имя директории.
    def __init__(self, dir_name: str):
        self.dir_name = dir_name
        self.objects_dict = self.get_objects_from_dir()

    # 2. Написать метод экземпляра класса, который создает атрибут экземпляра класса в ввиде словаря
    # {'filenames': [список файлов в папке], 'dirnames': [список всех подпапок в папке]}.
    # Подпапки учитывать только первого уровня вложения. Папка в папке в папке - такое не брать ))

    def get_objects_from_dir(self) -> dict:
        dir_list = os.listdir(self.dir_name)
        file_list = []
        sub_dir_list = []
        for file_name in dir_list:
            if os.path.isfile(os.path.join(self.dir_name, file_name)):
                file_list.append(file_name)
            elif os.path.isdir(os.path.join(self.dir_name, file_name)):
                sub_dir_list.append(file_name)
        return {'filenames': file_list, 'dirnames': sub_dir_list}

    # 2. Написать метод экземпляра класса, которая получает булевое значение (True/False).
    # Функция возвращает тот же словарь, но с отсортированными именами файлов и папок в соответствующих списках.
    # Булевое значение True означает, что порядок сортировки алфавитный, False - обратный порядок.

    def sorted_objects_from_dir(self, sort_type: bool) -> dict:
        for value in self.objects_dict.values():
            value.sort() if sort_type else value.sort(reverse=True)
        return self.objects_dict

    # 3. Написать метод экземпляра класса, которая получает строку, которая может быть
    # или именем файла, или именем папки. (В имени файла должна быть точка).
    # В зависимости от того, что функция получила (имя файла или имя папки) - записать его в соответствующий список
    # и вернуть обновленный словарь.

    def add_str_to_dict(self, file_name: str) -> dict:
        file_key = 'filenames'
        dir_key = 'dirnames'
        self.objects_dict[file_key].append(file_name) if '.' in file_name else self.objects_dict[dir_key].append(
            file_name)
        return self.objects_dict

    # 4* (*сдавать не обязательно, но если будете сдавать, то ошибки будут учитываться тоже).
    # Написать метод экземпляра класса, которая получает имя директории.
    # Функция проверяет соответствие полученного словаря и реальной файловой системы в полученной папке и,
    # если надо, создает нужные папки и пустые файлы, в соответствии со структурой словаря.

    def add_absent_object_from_dict(self, dir_name: str) -> None:
        file_in_child_dir = WorkWithFolder(dir_name).get_objects_from_dir()
        absent_file = list(set(self.objects_dict['filenames']) - set(file_in_child_dir['filenames']))
        absent_dir = list(set(self.objects_dict['dirnames']) - set(file_in_child_dir['dirnames']))
        for file_name_value in absent_file:
            create_empty_file(dir_name, file_name_value)
        for dir_name_value in absent_dir:
            create_dir(dir_name, dir_name_value)


# 1
path = 'resources'
worker = WorkWithFolder(path)

# 2
obj_dict = worker.objects_dict
print(f'Task 1: {obj_dict =}')

# 2
sort_alphabet_type = False  # False - DESC
worker.sorted_objects_from_dir(sort_alphabet_type)
print(f'Task 2: {obj_dict =}')

# 3
name_str = "names_1111txt"
worker.add_str_to_dict(name_str)
print(f'Task 3: {obj_dict =}')

# 4
child_dir_name = 'temp'
worker.add_absent_object_from_dict(child_dir_name)
child_obj_dict = WorkWithFolder(child_dir_name).objects_dict
print(f'Task 4: {child_obj_dict =}')
