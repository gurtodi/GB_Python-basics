from abc import ABC, abstractmethod
"""
Задание 1
"""


# Реализация класса Matrix (матрица)
class Matrix:

    # перегрузка метода __init__() со списком списков для формирования матрицы
    def __init__(self, list_list):
        self.matrix = list_list

    # перегрузка метода __str__() для вывода матриц в привычном виде
    def __str__(self):
        try:
            result = ''
            for row in self.matrix:
                for elem in row:
                    result += str(elem) + '\t'
                result += '\n'
            return result
            # Вариант 2. Возврат строки, собранной посредством генератора
            # return '\n'.join('\t'.join(map(str, row)) for row in self.matrix)
        except TypeError:
            return 'There is one trouble: object is not exist. Sorry'

    # перегрузка метода __add__() для сложения двух объектов класса Matrix
    def __add__(self, other):
        # складывать и вычитать можно матрицы одного размера, проверяем это
        if len(self.matrix) == len(other.matrix) and len(self.matrix[0]) == len(other.matrix[0]):
            # результатом сложения д.б. матрица
            new_matrix = []
            for row in range(len(self.matrix)):
                column = []
                for col in range(len(self.matrix[0])):
                    column.append(self.matrix[row][col] + other.matrix[row][col])
                new_matrix.append(column)
            return new_matrix
        else:
            print("add can't be done. Matrices must be the same size")
            pass


# задание объектов класса
matrix_1 = Matrix([[1, 2], [3, 4], [5, 6]])
matrix_2 = Matrix([[-2, -4], [-6, -8], [-10, -12]])
matrix_3 = Matrix([[0, 1], [2, 3]])
# проверка перегуженного метода __str__()
print(matrix_1)
print(matrix_2)
print(matrix_3)
# проверка перегуженного метода __add__()
matrix_sum = Matrix(matrix_1 + matrix_2)
print(matrix_sum)
# ошибка сложения
matrix_sum_error = Matrix(matrix_1 + matrix_3)
# ошибка вывода
print(matrix_sum_error)

"""
Задание 2
"""


class Clothes(ABC):
    full_cons = 0

    def __init__(self, name, val):
        self.name = name
        self.val = val

    @abstractmethod
    def fabric_consumption(self):
        pass

    def __add__(self, other):
        return self.fabric_consumption() + other.fabric_consumption()

    @property
    def context_name(self):
        return f'Fabric consumption for "{self.name}" is ~'


# к типам одежды в этом проекте относятся пальто и костюм.
class Coat(Clothes):

    def fabric_consumption(self):
        # определения расхода ткани для пальто (V/6.5 + 0.5)
        drain = self.val / 6.5 + 0.5
        Clothes.full_cons += drain
        return drain


class Suit(Clothes):

    def fabric_consumption(self):
        # определения расхода ткани для костюма (2 * H + 0.3)
        drain = 2 * self.val + 0.3
        Clothes.full_cons += drain
        return drain


# дочерний класс для проверки @property
# class Skirt(Clothes):
#     pass

coat_1 = Coat('New great coat', 50)
print(coat_1.context_name, round((coat_1.fabric_consumption()), 2))

suit_1 = Suit('First precious suit', 178)
print(suit_1.context_name, round((suit_1.fabric_consumption()), 2))

suit_2 = Suit('Second precious suit', 143)
print(suit_1.context_name, round((suit_1.fabric_consumption()), 2))

print('Overall fabric consumption is ~', round(Clothes.full_cons, 2))

# объект для проверки @property
# skirt_1 = Skirt('New glam skirt', 100)

"""
Задание 3
"""


class Cell:

    # инициализировать параметр, соответствующий количеству клеток (целое число)
    def __init__(self, amount):
        self.amount = int(amount)

    def __add__(self, other):
        return Cell(self.amount + other.amount)

    def __sub__(self, other):
        # выполняется если разность количества ячеек двух клеток больше нуля, иначе - сообщение
        if self.amount > other.amount:
            return Cell(self.amount - other.amount)
        else:
            print("Error! Subtraction can't be done")
            pass

    def __mul__(self, other):
        return Cell(self.amount * other.amount)

    def __truediv__(self, other):
        # + округление значения до целого числа
        return Cell(round(self.amount / other.amount))

    # метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
    def make_order(self, row):
        # возвращает строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
        count = self.amount
        cell_string = ''
        while count > 0:
            cell_string += ('*' * row if count > row else '*' * count) + '\n'
            count -= row
        return cell_string


cell_1 = Cell(18)
print(cell_1.make_order(20))
cell_2 = Cell(10)
print(cell_2.make_order(3))

cell_sum_1 = cell_1 + cell_2
print('Сумма:', cell_sum_1.amount)

cell_sub_1 = cell_1 - cell_2
print('Вычитание:', cell_sub_1.amount)
# ошибка вычитания
cell_sub_2 = cell_2 - cell_1

cell_mul_1 = cell_1 * cell_2
print('Произведение:', cell_mul_1.amount)

cell_div_1 = cell_2 / cell_1
print('Деление (с округлением до целого):', cell_div_1.amount)
