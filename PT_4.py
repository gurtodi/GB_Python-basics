"""
Задание 1
"""
# Скрипт расчета заработной платы сотрудника по формуле: (выработка в часах * ставка в час) + премия.
from sys import argv #импорт аргументов стоки, переданных скрипту (sys.argv)
script_name, h_worked, pay_per_h, bonus = argv
print("Зар.плата составляет ", int(h_worked) * int(pay_per_h) + int(bonus))
#проверонька запуска посредством ввода в командной строке: "PT_4.py 50 10 3, вывод 503"
"""
Задание 2
"""
print('-'*100)
#cur_list = input("Список чисел: ").split() # при ручном вводе списка чисел
cur_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print('Исходный список: ', cur_list)
"""
# формирование списка через цикл
new_list = []
i = int(1)
while i < len(cur_list):
    if cur_list[i] > cur_list [i-1]:
        new_list.append(cur_list[i])
    i += 1
print(new_list)"""
# генератор списка, в который добавляются элементы исходного, значения которых больше предыдущего элемента
new_list = [cur_list[i+1] for i in range(len(cur_list)-1) if cur_list[i] < cur_list [i+1]]
print('Список по условию:', new_list)
"""
Задание 3
"""
print('-'*100)
# Нахождение чисел в диапазоне [20;240], кратных 20 или 21. Однострочное решение
print('Числа из диапазона [20;240], кратные 20 или 21:', [numb for numb in range (20, 241) if not(numb % 20) or not(numb % 21)])
"""
Задание 4
"""
print('-'*100)
# Посредством генератора сформировать массив чисел из исходного без повторений
#original_list = input("Введите список чисел: ").split() # при ручном вводе списка чисел
original_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11] # для теста, рез: 23, 1, 3, 10, 4, 11
new_list = [int(original_list[i]) for i in range(len(original_list)) if original_list.count(original_list[i]) == 1]
print('Список без повторений: ', new_list)

"""
Задание 5
"""
print('-'*100)
# создание списка четных чисел из диапазона [100; 1000]
cur_list = [numb for numb in range (100, 1001) if not(numb % 2)]
#cur_list = [numb for numb in range (1, 10) if not(numb % 2)] # проверка 2*4*6*8 = 384
from functools import reduce
def mult(prev_el, el):
    return prev_el * el
print('Исходный список: ', cur_list, '\nПроизведение всех элементов списка = ', reduce(mult, cur_list))

"""
Задание 6
"""
print('-'*100)
# посредством count() реализовать итератор, генерирующий целые числа, начиная с указанного
from itertools import count
st_numb = int(3)
fin_numb = int(8)
print(f"Целые числа, начиная от {st_numb} до {fin_numb}")
for numb in count(st_numb):
    if numb > fin_numb:
        break
    else:
        print(numb)
print('-'*100)
# посредством cycle() реализовать итератор, повторяющий элементы некоторого списка, определенного заранее
from itertools import cycle
#end = int(input('Сколько повторяем? '))
end = int (7)
с = 1
list = ['раз', 'два', 'три']
print(f"{end} элементов, повтором полученных из списка {list}:")
for numb in cycle(['раз', 'два', 'три']):
    if с > end:
        break
    print(numb)
    с += 1
"""
Задание 7
"""
print('-'*100)
# Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
from math import factorial
#Функция, что отвечает за получение факториала числа, с созданием объекта-генератора
def fact(numb):
    for i in numb:
        yield(factorial(i))
n_max = int(6) #первые n-чисел
n = [i for i in range (1, n_max+1)]
#вывод в цикле первых n чисел, начиная с 1! и до n!, вызов функции д.б. for el in fact(n)
print(f"Первые {n_max} факториалов:")
for el in fact(n):
    print(el)
