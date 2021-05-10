"""
Задание 1.
"""
import time


class TrafficLight:
    # атрибут приватный
    __color = ('red', 'yellow', 'green')

    # метод переключения по стотояниям из списка
    def running(self):
        ind = int(0)
        # список продолжительности состояний в сек
        delay = (7, 2, 5)
        while ind < len(TrafficLight.__color):
            print(f'Traffic light is {TrafficLight.__color[ind]} for {delay[ind]} seconds')
            time.sleep(delay[ind])
            ind += 1


tr_light1 = TrafficLight()
tr_light1.running()

"""
Задание 2.
"""


class Road:
    # защищенные атрибуты длина, ширина, задающиеся при создании объекта
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def weight(self, mass, area):
        # расчет массы по заданной формуле, без перевода единиц измерения
        print(self._length * self._width * mass * area)


# Например: 20м * 5000м * 25кг * 5см = 12500 т
work1 = Road(20, 5000)
work1.weight(25, 5)

"""
Задание 3.
"""


# класс Worker с атрибутами: name, surname, position (должность), income (доход)
class Worker:
    # Последний атрибут должен быть защищенным и ссылаться на словарь,
    # содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        # income, защищенный, словарь {оклад: премия}
        self._income = {wage: bonus}


# класс Position, дочерний класса Worker
class Position(Worker):
    # метод получения полного имени сотрудника
    def get_full_name(self):
        print(f'Полное имя сторудника: {self.name} {self.surname}')

    # метод получения дохода с учетом премии
    def get_total_income(self):
        for key in self._income:
            print('Доход с учетом премии', key + self._income[key])


worker1 = Position('Иван', 'Иванов', 'Слесарь', 1000, 200)
print(f'Data checking:\nname: {worker1.name}, surname: {worker1.surname}, '
      f'position: {worker1.position}, income: {worker1._income}.\n')
worker2 = Position('Петр', 'Петров', 'Монтажник', 1200, 400)
worker1.get_full_name()
worker1.get_total_income()
worker2.get_full_name()
worker2.get_total_income()

"""
Задание 4.
"""


# базовый класс Car
class Car:
    # следующие атрибуты: speed, color, name, is_police (булево)
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        # is_police оспеделяется по факту принадлежнасти классу PoliceCar
        if type(self) == PoliceCar:
            self.is_police = True
        else:
            self.is_police = False

    # go машина поехала
    def go(self):
        print(f'Машинка "{self.name}" поехала')

    # stop машина остановилась
    def stop(self):
        print(f'Машинка "{self.name}" остановилась')
        pass

    # turn(direction) машина повернула (куда).
    def turn(self, direction):
        if direction == 'right':
            print(f'Машинка "{self.name}" повернула направо\n(☞ﾟヮﾟ)☞')
        elif direction == 'left':
            print(f'Машинка "{self.name}" повернула налево\n☜(ﾟヮﾟ☜)')
        else:
            print('Оп! Поворот никуда (´。＿。｀)')
        pass

    # метод, отображающий текущую скорость
    def show_speed(self):
        print(f'Текущая скорость машинки "{self.name}" = {self.speed} км/ч')


# дочерний к Car класс TownCar.
class TownCar(Car):
    # Переопределенный метод show_speed, если скорость больше 60 - сообщение о превышении
    def show_speed(self):
        print(f'Текущая скорость машинки "{self.name}" = {self.speed} км/ч')
        if self.speed > 60:
            print('Внимание, скорость превышена!')


# дочерний к Car класс SportCar.
class SportCar(Car):
    pass


# дочерний к Car класс WorkCar.
class WorkCar(Car):
    # Переопределенный метод show_speed, если скорость больше 40 - сообщение о превышении
    def show_speed(self):
        print(f'Текущая скорость машинки "{self.name}" = {self.speed} км/ч')
        if self.speed > 40:
            print('Внимание, скорость превышена!')


# дочерний к Car класс PoliceCar.
class PoliceCar(Car):
    pass


# создание объектов
town_car_1 = TownCar(30, 'black', 'Town car 1')
town_car_2 = TownCar(70, 'white', 'Town car 2')
sport_car_1 = SportCar(100, 'red', 'Sport car 1')
work_car_1 = WorkCar(50, 'yellow', 'Work car 1')
work_car_2 = WorkCar(30, 'yellow and red', 'Work car 2')
police_car_1 = PoliceCar(20, 'white and blue', 'Police car 1')

# проверка данных, доступ к атрибутам
print(f'Data checking for {town_car_1}:\nname: {town_car_1.name}, color: {town_car_1.color}, '
      f'speed: {town_car_1.speed}, police flag: {town_car_1.is_police}')
print(f'Data checking for {police_car_1}:\nname: {police_car_1.name}, color: {police_car_1.color}, '
      f'speed: {police_car_1.speed}, police flag: {police_car_1.is_police}')

# вызов методов
sport_car_1.go()
sport_car_1.stop()
sport_car_1.turn('right')
sport_car_1.turn('left')
sport_car_1.turn('hmm..')

town_car_1.show_speed()
town_car_2.show_speed()

work_car_1.show_speed()
work_car_2.show_speed()

"""
Задание 5.
"""


# Реализовать класс Stationery (канцелярская принадлежность).
class Stationery:
    # Определить в нем атрибут title (название)
    def __init__(self, title):
        self.title = title

    # и метод draw (отрисовка) выводит сообщение “Запуск отрисовки.”
    def draw(self):
        print('Запуск отрисовки')


# дочерний класс Pen.
class Pen(Stationery):
    # переопределнный метод draw с уникальным сообщением
    def draw(self):
        print(f'Запуск отрисовки ручкой, используется "{self.title}"')


# дочерний класс Pencil.
class Pencil(Stationery):
    # переопределнный метод draw с уникальным сообщением
    def draw(self):
        print(f'Запуск отрисовки карандашом, используется "{self.title}"')


# дочерний класс Handle.
class Handle(Stationery):
    # переопределнный метод draw с уникальным сообщением
    def draw(self):
        print(f'Запуск отрисовки маркером, используется "{self.title}"')


# создание экземпляров
brush_1 = Stationery('Кисточка')
pen_1 = Pen('Ручка')
pencil_1 = Pencil('Карандаш')
handle_1 = Handle('Маркер')

# вызов метода для каждого экземпляра
brush_1.draw()
pen_1.draw()
pencil_1.draw()
handle_1.draw()
