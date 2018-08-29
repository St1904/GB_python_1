# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.


class Person:
    def __init__(self, health, damage, armor):
        self.health = health
        self.damage = damage
        self.armor = armor

    def _calc_damage(self, enemy):
        return enemy.damage * self.armor

    def attack(self, enemy):
        damage = self._calc_damage(enemy)
        print('Здоровья:', self.health, 'Получено урона:', damage)
        self.health -= self._calc_damage(enemy)

    def get_name(self):
        return self.__class__.__name__


class Player(Person):
    def attack(self, enemy):
        print('Игрок атакует!')
        super().attack(enemy)


class Enemy(Person):
    def attack(self, enemy):
        print('Соперник атакует!')
        super().attack(enemy)


class Game:
    def __init__(self, first_player, second_player):
        self.current = first_player
        self.enemy = second_player

    def start(self):
        print('Бой начался!')
        while self.current.health >= 0 and self.enemy.health >= 0:
            self.step()
            input('Для завершения хода нажмите Enter!')
            print()
        else:
            print(self.enemy.get_name(), 'победил!')

    def step(self):
        self.current.attack(self.enemy)

        tmp = self.current
        self.current = self.enemy
        self.enemy = tmp

        # _ = input('Для завершения хода нажмите Enter!')



player = Player(15, 5, 1.0)
enemy = Enemy(10, 4, 0.9)
game = Game(player, enemy)
game.start()