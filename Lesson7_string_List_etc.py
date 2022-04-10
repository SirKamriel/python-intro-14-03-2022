#1. Дано целое число (int). Определить сколько нулей в этом числе.

# int = 60050
# rezult = str(int).count("0")
# print(rezult)

#2. Дано целое число (int). Определить сколько нулей в конце этого числа. Например для числа 1002000 - три нуля

# int = 2000300
# my_str = ""
# value = -1
# while str(int)[value] in str(int) and str(int)[value] == "0":
#     my_str += (str(int)[value])
#     value -= 1
# print(len(my_str))

# 3. Даны списки my_list_1 и my_list_2.
# Создать список my_result в который вначале поместить
# элементы на четных местах из my_list_1, а потом все элементы на нечетных местах из my_list_2.

# my_list_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# my_list_2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# my_result = my_list_1[::2] + my_list_2[1::2]
# print(my_result)

# забыл что с 0 начинаеться и долго дебажил =)

# 4. Дан список my_list. СОЗДАТЬ НОВЫЙ список new_list у которого первый элемент из my_list
# стоит на последнем месте. Если my_list [1,2,3,4], то new_list [2,3,4,1]

# my_list = [1, 2, 3, 4]
# symbol = my_list[0]
# new_list = my_list.copy()[1:]
# new_list.append(symbol)
# print(new_list)

# 5.Дан список my_list. В ЭТОМ списке первый элемент переставить на последнее место.
# [1,2,3,4] -> [2,3,4,1]. Пересоздавать список нельзя! (используйте метод pop)

# my_list = [1, 2, 3, 4]
# del_value = my_list[::-1].pop()
# my_list[:] = my_list[1:]
# my_list.append(del_value)
# print(my_list)

# 6. Дана строка в которой есть числа (разделяются пробелами).
# Например "43 больше чем 34 но меньше чем 56". Найти сумму ВСЕХ ЧИСЕЛ (А НЕ ЦИФР) в этой строке.
# Для данного примера ответ - 133. (используйте split и проверку isdigit)

# my_str = "43 больше чем 34 но меньше чем 56"
# my_list = []
# for symbol in my_str.split(" "):
#     if symbol.isdigit():
#         my_list.append(int(symbol))
# print(sum(my_list))

# 7. Дана строка my_str в которой символы МОГУТ повторяться и два символа l_limit, r_limit,
# которые точно находятся в этой строке. Причем l_limit левее чем r_limit.
# В переменную sub_str поместить НАИБОЛЬШУЮ часть строки между этими символами.
# my_str = "My long string", l_limit = "o", r_limit = "g" -> sub_str = "ng strin".

# my_str = "My long string"
# l_limit = "o"
# r_limit = "g"
# l_index = my_str.find(l_limit) + 1
# r_index = my_str.rfind(r_limit)
# sub_str = my_str[l_index:r_index]
# print(sub_str)

# не сразу понял задачу

# 8. Дана строка my_str. Разделите эту строку на пары из двух символов и поместите эти пары в список.
# Если строка содержит нечетное количество символов, пропущенный второй символ последней пары должен
# быть заменен подчеркиванием ('_'). Примеры: 'abcd' -> ['ab', 'cd'], 'abcde' -> ['ab', 'cd', e_']
# (используйте срезы длинны 2)

# my_str = "abcdefghjkl"
# my_list = []
# index_1 = 0
# index_2 = 2
# if len(my_str) %2 != 0:
#     my_str += "_"
# for index in enumerate(my_str):
#     if index_2 <= len(my_str):
#         value = my_str[index_1:index_2]
#         my_list.append(value)
#         index_1 +=2
#         index_2 +=2
# print(my_list)

# 9. Дан список чисел. Определите, сколько в этом списке элементов,
# которые больше суммы двух своих соседей (слева и справа), и НАПЕЧАТАЙТЕ КОЛИЧЕСТВО таких элементов.
# Крайние элементы списка никогда не учитываются, поскольку у них недостаточно соседей.
# Для списка [2,4,1,5,3,9,0,7] ответом будет 3 потому что 4 > 2+1, 5 > 1+3, 9>3+0.

# my_list = [2, 4, 1, 5, 3, 9, 0, 7]
# index = 1
# result = 0
# for x,symbol in enumerate(my_list):
#     if index + 1 < len(my_list):
#         summ = my_list[index - 1] + my_list[index + 1]
#         if my_list[index] > summ:
#             result +=1
#         index += 1
# print(result)

# 10. Дан список my_list в котором могут быть как строки (type str) так и целые числа (type int).
# Например [1, 2, 3, "11", "22", 33]
# Создать новый список в который поместить только строки из my_list.

# my_list = [1, 2, 3, "11", "22", "33"]
# new_list = []
# for symbol in my_list:
#     if type(symbol) == str:
#         new_list.append(symbol)
# print(new_list)


# 11. Дана строка my_str. Создать список в который поместить те символы из my_str,
# которые встречаются в строке ТОЛЬКО ОДИН раз.

# my_str = "Goodbye world"
# my_list = []
# for symbol in set(my_str):
#     if my_str.count(symbol) == 1:
#         my_list.append(symbol)
# print(my_list)

# 12. Даны две строки. Создать список в который поместить те символы,
# которые есть в обеих строках хотя бы раз.

# my_str_1 = "Hello world"
# my_str_2 = "Goodbye world"
# my_list = []
# my_list = set(my_str_1).intersection(set(my_str_2))
# print(my_list)

# 13. Даны две строки. Создать список в который поместить те символы, которые есть в обеих строках,
# но в каждой ТОЛЬКО ПО ОДНОМУ разу.
# Пример: для строк "aaaasdf1" и "asdfff2" ответ ["s", "d"], т.к. эти символы есть в каждой строке по одному разу

my_str_1 = "aaaasdf1"
my_str_2 = "asdfff2"
my_list = []
for symbol in set(my_str_1).intersection(my_str_2):
    if (my_str_1 + my_str_2).count(symbol) == 2:
        my_list.append(symbol)
print(my_list)