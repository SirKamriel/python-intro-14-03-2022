# 1. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list по следующему правилу:
# Если строка стоит на нечетном месте в my_list, то ее заменить на
# перевернутую строку. "qwe" на "ewq".
# Если на четном - оставить без изменения.
# Задание сделать с использованием enumerate или range.

my_list_1 = ['12345', '23456', '34567', '45678', '56789']
new_my_list_1 = []
for index, value in enumerate(my_list_1):
    new_my_list_1.append(value) if index % 2 == 0 else new_my_list_1.append(value[::-1])
print(new_my_list_1)

# 2. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list у которых первый символ - буква "a".

my_list_2 = ['12a345', 'a23456', '345a67', 'a45678', 'A56789']
new_my_list_2 = [value for value in my_list_2 if value.startswith('a')]
print(new_my_list_2)

# 3. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list в которых есть символ - буква "a" на любом месте.

my_list_3 = ['12a345', 'a23456', '345a67', 'a45678', 'A56789']
new_my_list_3 = [value for value in my_list_3 if 'a' in value]
print(new_my_list_3)

# 4) Дан список словарей persons в формате [{"name": "John", "age": 15}, ... ,{"name": "Jack", "age": 45}]

persons_4 = [{"name": "John", "age": 15},
             {"name": "Jack", "age": 23},
             {"name": "Alex", "age": 18},
             {"name": "Jacob", "age": 43},
             {"name": "Micheal", "age": 34},
             {"name": "Jenny", "age": 55},
             {"name": "Alan", "age": 15},
             {"name": "Charlie", "age": 34},
             ]

# а) Создать список и поместить туда имя самого молодого человека.
# Если возраст совпадает - поместить все имена самых молодых.

min_age = min([person["age"] for person in persons_4])
young_person_list = ([person["name"] for person in persons_4 if person["age"] == min_age])
print(young_person_list)

# б) Создать список и поместить туда самое длинное имя. Если длина имени совпадает - поместить все такие имена.

max_name_len = len(max([person["name"] for person in persons_4]))
max_name_list = ([person["name"] for person in persons_4 if len(person["name"]) == max_name_len])
print(max_name_list)

# в) Посчитать среднее количество лет всех людей из начального списка.

age_list = ([person["age"] for person in persons_4])
average_age = sum(age_list) / len(age_list)
print(average_age)

# 5) Даны два словаря my_dict_1 и my_dict_2.

my_dict_1 = {"name": "John",
             "age": 17,
             "job": "student",
             "university": "harvard"
             }

my_dict_2 = {"name": "Jack",
             "age": 23,
             "job": "artist",
             "company": "bond",
             }

# а) Создать список из ключей, которые есть в обоих словарях.

equals_keys_list = list(set(my_dict_1.keys()) & set(my_dict_2.keys()))
print(equals_keys_list)

# б) Создать список из ключей, которые есть в первом, но нет во втором словаре.

diff_keys_list = list(set(my_dict_1.keys()) - set(my_dict_2.keys()))
print(diff_keys_list)

# в) Создать новый словарь из пар {ключ:значение}, для ключей, которые есть в первом, но нет во втором словаре.

my_dict_3 = {key: my_dict_1[key] for key in diff_keys_list}
print(my_dict_3)

# г) Объединить эти два словаря в новый словарь по правилу:
# если ключ есть только в одном из двух словарей - поместить пару ключ:значение,
# если ключ есть в двух словарях - поместить пару {ключ: [значение_из_первого_словаря, значение_из_второго_словаря]},
#
# {1:1, 2:2}, {11:11, 2:22} ---> {1:1, 11:11, 2:[2, 22]}

new_my_dict = my_dict_1.copy()
for key, value in my_dict_2.items():
    new_my_dict[key] = [new_my_dict[key], value] if key in new_my_dict else value
print(new_my_dict)
