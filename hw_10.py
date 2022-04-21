from datetime import datetime
from string import ascii_letters


def get_lines_from_file(filename):
    with open(filename, 'r') as input_file:
        lines_list = input_file.read().splitlines()
    return lines_list


# Все пункты сделать как отдельные функции и их вызовы.
# 1. Написать функцию, которая получает в виде параметра имя файла названия интернет доменов (domains.txt)
# и возвращает их в виде списка строк (названия возвращать без точки).

domains_file = 'resources/domains.txt'


def get_domain_names_from_file(filename):
    data_from_file = get_lines_from_file(filename)
    dom_list = [value.replace('.', '') for value in data_from_file]
    return dom_list


domains_list = get_domain_names_from_file(domains_file)
print(domains_list)

# 2. Написать функцию, которая получает в виде параметра имя файла (names.txt)
# и возвращает список всех фамилий из него.
# Каждая строка файла содержит номер, фамилию, страну, некоторое число (таблица взята с википедии).
# Разделитель - символ табуляции "\t"

names_file = 'resources/names.txt'


def get_last_names_from_file(filename):
    data_from_file = get_lines_from_file(filename)
    ln_list = [line.split('\t')[1] for line in data_from_file if line]
    return ln_list


last_names_list = get_last_names_from_file(names_file)
print(last_names_list)

# 3. Написать функцию, которая получает в виде параметра имя файла (authors.txt) и возвращает список
# словарей вида {"date": date}
# в которых date - это дата из строки (если есть),
# Например [{"date": "1st January 1919", "date": "8th February 1828"},  ...]


authors_file = 'resources/authors.txt'


def get_date_dict_from_file(filename):
    data_from_file = get_lines_from_file(filename)
    new_data = [{'date': line.split(' - ')[0]} for line in data_from_file if line and '-' in line]
    return new_data


date_list = get_date_dict_from_file(authors_file)
print(date_list)


# По просьбам некоторых студентов начну включать дополнительные задания.
# 4* (*сдавать не обязательно, но если будете сдавать, то ошибки будут учитываться тоже).
# Написать функцию, которая получает в виде параметра имя файла (authors.txt) и возвращает список
# словарей вида {"date_original": date_original, "date_modified": date_modified}
# в которых date_original - это дата из строки (если есть),
# а date_modified - эта же дата, представленная в формате "dd/mm/yyyy" (d-день, m-месяц, y-год)
# Например [{"date_original": "8th February 1828", "date_modified": 08/02/1828},  ...]


def get_date_modified_from_file(filename):
    mod_date_list = get_date_dict_from_file(filename)
    date_key = 'date'
    mod_date_key = date_key + '_modified'
    for date in mod_date_list:
        mod_date = date[date_key].split()
        mod_date_len = len(mod_date)
        if mod_date_len == 3:
            mod_date[0] = mod_date[0].strip(ascii_letters)
            strp_time_format = '%d %B %Y'
            strf_time_format = '%d/%m/%Y'
        elif mod_date_len == 2:
            strp_time_format = '%B %Y'
            strf_time_format = '%m/%Y'
        mod_date = ' '.join(mod_date)
        date_dt_format = datetime.strptime(mod_date, strp_time_format)
        date[mod_date_key] = date_dt_format.strftime(strf_time_format)
    return mod_date_list


date_list = get_date_modified_from_file(authors_file)
print(date_list)
