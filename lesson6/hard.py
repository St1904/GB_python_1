# Задача - 1
# Вам необходимо создать завод по производству мягких игрушек для детей.
# Вам надо продумать структуру классов,
# чтобы у вас был класс, который создает игрушки на основании:
#  Названия, Цвета, Типа (животное, персонаж мультфильма)
# Опишите процедуры создания игрушки в трех методах:
# -- Закупка сырья, пошив, окраска
# Не усложняйте пусть методы просто выводят текст о том, что делают.
# В итоге ваш класс по производству игрушек должен вернуть объект нового класса Игрушка.


# class Toy:
#     def __init__(self, name, color, type):
#         self.name = name
#         self.color = color
#         self.type = type
#
#     def _buy_source(self):
#         print('Закупка сырья...')
#
#     def _sew(self):
#         print('Шьем...')
#
#     def _paint(self):
#         print('Красим...')
#
#     def create_toy(self, name, color, type):
#         self._buy_source()
#         self._sew()
#         self._paint()
#         return Toy(name, color, type)


# Задача - 2
# Доработайте нашу фабрику, создайте по одному классу на каждый тип, теперь надо в классе фабрика
# исходя из типа игрушки отдавать конкретный объект класса, который наследуется от базового - Игрушка

class Toy:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def toy_print(self):
        print('Йа игрушко')


class Car(Toy):
    def toy_print(self):
        print('Йа машинко')


class Doll(Toy):
    def toy_print(self):
        print('Йа куколко')


class ToyFactory:
    def _buy_source(self):
        print('Закупка сырья...')

    def _sew(self):
        print('Шьем...')

    def _paint(self):
        print('Красим...')

    def create_toy(self, name, color, type):
        self._buy_source()
        self._sew()
        self._paint()
        if type == 'Toy':
            return Toy(name, color)
        elif type == 'Doll':
            return Doll(name, color)
        elif type == 'Car':
            return Car(name, color)
        else:
            print('Не знаю таких игрушек!')


factory = ToyFactory()
doll = factory.create_toy('Asya', 'black', 'Doll')
car = factory.create_toy('Ferrarrrri', 'red', 'Car')

doll.toy_print()
car.toy_print()