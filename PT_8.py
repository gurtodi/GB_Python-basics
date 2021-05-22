import time
from datetime import datetime

"""
Задание 1
"""


class Date:
    # функция-конструктор должна принимать дату в виде строки формата «день-месяц-год».
    def __init__(self, string_date):
        self.string_date = string_date

    # извлечение числа, месяца, года, преобразуя их к типу «Число».
    @classmethod
    def get_dmy(cls, self):
        date_list = list()
        # print(date_1.__dict__)
        for d in self.__getattribute__('string_date').split('-'):
            date_list.append(int(d))
        return date_list

    # должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
    @staticmethod
    def valid_dmy_1(date):
        print(f'Date {date} validation for option 1.')
        # проверка путем приведения к объекту класса datetime
        try:
            datetime.strptime(date, '%d-%m-%Y')
        except ValueError:
            return 'Validation failed. Date error'
        return 'Validation completed successfully!'

    @staticmethod
    def valid_dmy_2(date):
        # крайне 
        print(f'Date {date} validation for option 2.')
        if date[1] < 1 or date[1] > 12:
            return 'Validation failed. Month number error: ' \
                   'the value must be in the range from 1 to 12'
        if date[1] in (1, 3, 5, 7, 8, 10, 12) and (date[0] < 1 or date[0] > 31):
            return 'Validation failed. Day number error:' \
                   'the value must be in the range from 1 to 31'
        if date[1] in (4, 6, 9, 11) and (date[0] < 1 or date[0] > 30):
            return 'Validation failed. Day number error:' \
                   'the value must be in the range from 1 to 30'
        if date[1] == 2 and not(date[2] % 4):
            if date[0] < 1 or date[0] > 29:
                return 'Validation failed. Day number error' \
                       'the value must be in the range from 1 to 29'
        else:
            if date[0] < 1 or date[0] > 28:
                return 'Validation failed. Day number error:' \
                       'the value must be in the range from 1 to 28'
        return 'Validation completed successfully!'


# Проверить работу полученной структуры на реальных данных.
date_1 = Date('26-09-1995')
date_list_1 = Date.get_dmy(date_1)
print(f'Day - {date_list_1[0]}, Month - {date_list_1[1]}, Year - {date_list_1[2]}')
print(date_list_1)
print(Date.valid_dmy_1(date_1.string_date))

# Проверки валидации даты
# date_2 = Date('30-02-2000')
# print(Date.valid_dmy_1(date_2.string_date))
# print(Date.valid_dmy_2(Date.get_dmy(date_2)))
#
# date_3 = Date('29-02-2001')
# print(Date.valid_dmy_1(date_3.string_date))
# print(Date.valid_dmy_2(Date.get_dmy(date_3)))
#
# date_4 = Date('40-30-2000')
# print(Date.valid_dmy_1(date_4.string_date))
# print(Date.valid_dmy_2(Date.get_dmy(date_4)))

"""
Задание 2
"""


# класс-исключение, обрабатывающий деление на ноль
class DivisionByZero(Exception):

    def __init__(self, txt):
        self.txt = txt


dividend = int(input('Делимое = '))
divider = int(input('Делитель = '))

try:
    if divider == 0:
        raise DivisionByZero('Нет, нет, нет, на ноль не делим!')
except DivisionByZero as error:
    print(error)
else:
    print(f'Можем посчитать частное: {dividend}/{divider} = {dividend/divider}')

"""
Задание 3
"""


# Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
class OnlyNumbers(Exception):
    res_list = list()

    def __init__(self, txt):
        self.txt = txt

    @staticmethod
    def is_number(input_data):
        try:
            if not(input_data.isdigit()):
                raise OnlyNumbers('Нет, нет, нет, должно быть число. Продолжаем:')
        except OnlyNumbers as error:
            print(error)
        else:
            OnlyNumbers.res_list.append(int(input_data))


user_input = ''
print('Правила простые: вводите данные, мы проверим их и добавим в список только числа. '
      '\nЗавершаем при вводе слова "stop". Начнем!')
while user_input != 'stop':
    user_input = input()
    OnlyNumbers.is_number(user_input)
print('Вот список итоговый:', OnlyNumbers.res_list)

"""
Задание 4
Задание 5
Задание 6
"""


class Depot:
    def __init__(self):
        self.storage = {}

    def supply(self, equip):
        self.storage.setdefault(equip.group_name(), []).append(equip)


class OfficeEquipment:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.group = self.__class__.__name__

    def group_name(self):
        return f'{self.group}'


class Printer(OfficeEquipment):
    def __init__(self, name, price, print_type, print_speed):
        super().__init__(name, price)
        self.print_type = print_type
        self.print_speed = print_speed

    def __repr__(self):
        return f'{self.name} {self.price} {self.print_type} {self.print_speed}'


class Scanner(OfficeEquipment):
    def __init__(self, name, price, scan_type, scan_speed, scan_area):
        super().__init__(name, price)
        self.scan_type = scan_type
        self.scan_speed = scan_speed
        self.scan_area = scan_area

    def group_name(self):
        return f'{self.group}'

    def __repr__(self):
        return f'{self.name} {self.price} {self.scan_type} {self.scan_type} {self.scan_area}'


class Copier(OfficeEquipment):
    def __init__(self, name, price, copy_speed, copy_resolution):
        super().__init__(name, price)
        self.copy_speed = copy_speed
        self.copy_resolution = copy_resolution


depot = Depot()
printer_1 = Printer('Printer 1', 100500, 'laser', 100)
depot.supply(printer_1)
printer_2 = Printer('Printer 2', 200, 'laser', 20)
depot.supply(printer_2)
print(depot.storage)


"""
Задание 7
"""

class ComplexNumber:

    def __init__(self, real, imaginary):
        # a + b*i
        self.a = real
        self.b = imaginary

    def __str__(self):
        return f"{self.a}{'+' if self.b > 0 else ''}{self.b}·i"

    def __add__(self, other):
        # (a + bi) + (c + di) = (a + c) + (b + d)i
        return ComplexNumber(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        # (a + bi) · (c + di) = (ac – bd) + (ad + bc)i
        return ComplexNumber(self.a * other.a - self.b * other.b, self.a * other.b + self.b * other.a)


number_1 = ComplexNumber(1, -3)
number_2 = ComplexNumber(-5, 4)
print('First number = ', number_1)
print('Second number = ', number_2)
# (1 + -3i) + (-5 + 4i) = -4 + 1·i
print('Sum number = ', number_1 + number_2)
# (1 + -3i) · (-5 + 4i) = (-5 + 12) + (4 + 15)·i
print('Product number = ', number_1 * number_2)
