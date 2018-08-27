# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)

# class TownCar:
#     def __init__(self, speed, color, name):
#         self.speed = speed
#         self.color = color
#         self.name = name
#         self.is_police = False
#
#     def go(self):
#         print('TownCar go')
#
#     def stop(self):
#         print('TownCar stop')
#
#     def turn(self, direction):
#         print('TownCar turn', direction)
#
#
# class SportCar:
#     def __init__(self, speed, color, name):
#         self.speed = speed
#         self.color = color
#         self.name = name
#         self.is_police = False
#
#     def go(self):
#         print('SportCar go')
#
#     def stop(self):
#         print('SportCar stop')
#
#     def turn(self, direction):
#         print('SportCar turn', direction)
#
#
# class WorkCar:
#     def __init__(self, speed, color, name):
#         self.speed = speed
#         self.color = color
#         self.name = name
#         self.is_police = False
#
#     def go(self):
#         print('WorkCar go')
#
#     def stop(self):
#         print('WorkCar stop')
#
#     def turn(self, direction):
#         print('WorkCar turn', direction)
#
#
# class PoliceCar:
#     def __init__(self, speed, color, name):
#         self.speed = speed
#         self.color = color
#         self.name = name
#         self.is_police = True
#
#     def go(self):
#         print('PoliceCar go')
#
#     def stop(self):
#         print('PoliceCar stop')
#
#     def turn(self, direction):
#         print('PoliceCar turn', direction)


# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.

class Car:
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self._model = 'Car'

    def go(self):
        print('{} go'.format(self._model))

    def stop(self):
        print('{} stop'.format(self._model))

    def turn(self, direction):
        print('{} turn'.format(self._model), direction)

class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.is_police = False
        self._model = 'TownCar'

class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.is_police = False
        self._model = 'SportCar'

class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.is_police = False
        self._model = 'WorkCar'

class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.is_police = True
        self._model = 'PoliceCar'

car1 = TownCar(24, 'blue', 'Some town car')
car1.go()
car1.stop()
car1.turn('left')

car2 = PoliceCar(120, 'red', 'Super police car')
print(car2.name, car2.color, car2.speed, car2.is_police)
car2.go()
car2.stop()
car2.turn('right')