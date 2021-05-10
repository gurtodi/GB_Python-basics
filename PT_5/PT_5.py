"""
Задание 1.
"""
import os
with open('par1.txt', 'w') as str_f: # создание файла, использование оного на запись
    print("Введите несколько строк. Для завершения введите пустую строку")
    words = '1'
    while words:
        words = input()
        str_f.write(words + '\n')
    print("Всё записано в файл", str_f.name)
"""
Задание 2.
"""
result = dict() # результирующий словарь
str_n = int(0) # счетчик количества строк
word_n = int(0) # счетчик количества слов
with open('one_art.txt', 'r') as par2: # работа ведется с файлом one_art.txt
    for line in par2:
        str_n += 1
        word_n = int(0)
        for word in line.split(' '):
            word_n += 1
        result.update({str_n: word_n})
print(result.items())
"""
Задание 3.
"""
all_val = list() # будет список из всех значений
with open('workers.txt', 'r') as par3: # работа ведется с файлом workers.txt
    for line in par3:
        for phrase in line.split(' '):
            all_val.append(phrase.rstrip())
ind = int(0)
sum = int(0)
print("Сотрудники, оклад коих менее 20 тыс:")
while ind < len(all_val): # проход по общему списку, где на нечётных позициях имена, на четных - оклады
    if int(all_val[ind+1]) < 20000:
        print(all_val[ind]) # вывод фамилий тех, чей оклад менее 20тыс
    sum += int (all_val[ind+1]) #подсчет суммы всех окладов для среднего
    ind += 2
print('Средний оклад = ', round((sum / len(all_val) * 2), 2))
"""
Задание 4.
"""
# словарь для замены англ. числительных русскимим
numb_dict = {'One' : 'Один',
             'Two' : 'Два',
             'Three' : 'Три',
             'Four' : 'Четыре'}
par4_2 = open("numbers_out.txt", "w")
with open('numbers_in.txt', 'r') as par4_1: # непрограммно заполненый файл numbers_in.txt
    for line in par4_1:
        key = line[:line.index(' ')] # в качестве ключа используем первое слово строки
        print(line.replace(key, numb_dict[key]).rstrip(), file = par4_2) # запись преобразованной строки в файл
par4_2.close()
"""
Задание 5.
"""
sum = int(0)
par5 = open('numbers_list.txt', 'w+') #созданный текстовый файл numbers_list.txt
par5.write("1 2 3 4 5 6")
par5.seek(0)
line = par5.readline()
for nomb in line.split(' '):
    sum += int(nomb) # подсчет суммы чисел
par5.close()
print(f'Сумма чисел ({line}) равна {sum}')
"""
Задание 6.
"""
values_list = list()
subj_h = dict() # итоговый словарь
# накрученный способ получения списка всех значений из исходного файла с вычетом возможных разделителей ':', ' '
with open('subjects.txt', 'r', encoding='utf-8') as par6: # исходные данные в файле subjects.txt
        for line in par6:
            for phrase in line.split(':'):
                for name in phrase.split():
                    if name:
                        values_list.append(name)
def cut_str(str): # функция для возврата часов
    if str != '-':
        return(int(str[:str.index('(')]))
    else:
        return 0
ind = int(0)
while ind < len(values_list):
    subj_h.update({values_list[ind]:(cut_str(values_list[ind+1]) + cut_str(values_list[ind+2]) + cut_str(values_list[ind+3]))})
    ind += 4
print(subj_h)
"""
Задание 7.
"""
#функция, что топорно возвращает название фирмы и прибыль, как часть словаря
def profit(str):
    str = str.split()
    return({str[0] : int(str[2]) - int(str[3])})
firms = dict() # словарь фирм и их прибылями
firms_count = int(0) # количество фирм (строк)
with open('firms.txt', encoding='utf-8') as par7_in: # работа ведется с файлом firms.txt
    for line in par7_in:
        firms.update(profit(line.rstrip())) # словаря заполнение с фирмами и их прибылями
        firms_count += 1
average_profit = int(0)
for key in firms:
    if firms[key] > 0: # суммарная прибыль неубыточных фирм
        average_profit += firms[key]
average = {'average_profit': average_profit / firms_count} # средняя прибыль, словарь
result_list = (firms, average)
import json
with open("firms_result.json", "w", encoding="utf-8") as par7_out: # сохранение в виде json-объекта в соответствующий файл
    json.dump(result_list, par7_out)
