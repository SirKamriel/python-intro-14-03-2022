import os
from utils.files import create_empty_file, create_dir

# Все пункты являются частью одного задания, поэтому можно использовать функции несколько раз и не дублировать код.
# Если хотите, можете использовать значения по умолчанию и аннотацию типов.
#
# 1. Написать функцию, которая получает один параметр - имя директории и возвращает словарь вида
# {'filenames': [список файлов в папке], 'dirnames': [список всех подпапок в папке]}.
# Подпапки учитывать только первого уровня вложения. Папка в папке в папке - такое не брать ))

path = 'resources'


def get_filenames_from_dir(dir_name: str) -> dict:
    dir_list = os.listdir(dir_name)
    file_list = []
    sub_dir_list = []
    for file_name in dir_list:
        if os.path.isfile(os.path.join(dir_name, file_name)):
            file_list.append(file_name)
        elif os.path.isdir(os.path.join(dir_name, file_name)):
            sub_dir_list.append(file_name)
    return {'filenames': file_list, 'dirnames': sub_dir_list}


dir_dict = get_filenames_from_dir(path)
print(f'Task 1: {dir_dict =}')

# 2. Написать функцию, которая получает два параметра - словарь, описанный в пункте 1
# и булевое значение (True/False) - можно сделать параметром по умолчанию.
# Функция возвращает тот же словарь, но с отсортированными именами файлов и папок в соответствующих списках.
# Булевое значение True означает, что порядок сортировки алфавитный, False - обратный порядок.

asc_sort = False  # False - DESC


def sort_dict_by_alpha(input_dict: dict, sort_type: bool) -> dict:
    for value in input_dict.values():
        value.sort() if sort_type else value.sort(reverse=True)
    return input_dict


sort_dict = dict_sort_by_value = sort_dict_by_alpha(dir_dict, asc_sort)
print(f'Task 2: {sort_dict =}')

# 3. Написать функцию, которая получает два параметра - словарь, описанный в пункте 1 и строку, которая может быть
# или именем файла, или именем папки. (В имени файла должна быть точка).
# В зависимости от того, что функция получила (имя файла или имя папки) - записать его в соответствующий список
# и вернуть обновленный словарь.

name_str = "names_1111txt"


def add_str_to_dict(input_dict: dict, file_name: str) -> dict:
    file_key = 'filenames'
    dir_key = 'dirnames'
    input_dict[file_key].append(file_name) if '.' in file_name else input_dict[dir_key].append(file_name)
    return input_dict


new_dict = add_str_to_dict(dir_dict, name_str)
print(f'Task 3: {new_dict =}')

# 4* (*сдавать не обязательно, но если будете сдавать, то ошибки будут учитываться тоже).
# Написать функцию, которая получает два параметра - словарь, описанный в пункте 1 и имя директории.
# Функция проверяет соответствие полученного словаря и реальной файловой системы в полученной папке и,
# если надо, создает нужные папки и пустые файлы, в соответствии со структурой словаря.

child_dir_name = 'temp'


def add_absent_file_from_dict(input_dict: dict, dir_name: str) -> None:
    file_in_child_dir = get_filenames_from_dir(dir_name)
    absent_file = list(set(input_dict['filenames']) - set(file_in_child_dir['filenames']))
    absent_dir = list(set(input_dict['dirnames']) - set(file_in_child_dir['dirnames']))
    for file_name_value in absent_file:
        create_empty_file(dir_name, file_name_value)
    for dir_name_value in absent_dir:
        create_dir(dir_name, dir_name_value)


add_absent_file_from_dict(dir_dict, child_dir_name)
created_dict = get_filenames_from_dir(child_dir_name)
print(f'Task 4: {created_dict =}')
