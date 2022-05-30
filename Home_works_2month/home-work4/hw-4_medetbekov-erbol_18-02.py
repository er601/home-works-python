# #ДЗУрок4 Дэдлайн 15.05.2022 23 59
#  Добавить в проект уникальную реализацию суперспособности героев
    # 1. Berserk должен получать от босса урон, затем при ударе наносить ему свой урон, плюс часть накопленного урона полученного от босса
    # 2. Thor, удар по боссу имеет шанс оглушить босса на 1 раунд, вследствие чего босс пропускает 1 раунд и не наносит урон героям
    # 3. Golem, который имеет увеличенную жизнь но слабый удар. Может принимать на себя 1/5 часть урона исходящего от босса по другим игрокам
# 4. Witcher, не наносит урон боссу, но получает урон от босса. Имеет 1 шанс оживить первого погибшего героя, отдав ему свою жизнь, при этом погибает сам.
# 5. Avrora, которая может входить в режим невидимости на 2 раунда (т.е не получает урон от босса), в тоже время полученный урон в режиме невидимости возвращает боссу в последующих раундах. Она может исчезать только один раз за игру
# 6. Druid, который имеет способность рандомно призывать помощника ангела героям или же ворона боссу на 1 раунд за всю игру. "Ангел" увеличивает способность медика лечить героев на  n кол-во. А ворон прибавляет  агрессию (увеличивается урон на 50%), боссу если его жизнь менее 50%.
    # 7. Hacker, который будет через раунд забирать у Босса N-ое количество здоровья и переводить его одному из героев
# 8. TrickyBastard,  способность которого будет состоять в том, чтобы притвориться мертвым в определенном раунде(из случайного выбора), но в следующем раунде он снова вступает в бой. При этом он не получает урон и не бьет босса когда притворился мертвым
# 9. AntMan, в каждом раунде он может увеличиться или же уменьшится на N-ный размер, также увеличиваются/уменьшаются жизнь и урон, после раунда он возвращается в исходный размер
# 10. Deku (сила удара может меняться каждый раунд с шансом 50 на 50,  может усилится на 20%, 50%, 100%, но при усилении теряется хп (чем сильнее усиление, тем больше хп потеряет герой)

from random import randint

class GameEntity:
    def __init__(self, name, health, damage):
        self.__name = name
        self.__health = health
        self.__damage = damage

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if value < 0:
            self.__health = 0
        else:
            self.__health = value

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, value):
        self.__damage = value

    def __str__(self):
        return f'{self.__name} health: {self.__health} [{self.__damage}]'


class Boss(GameEntity):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)

    def hit(self, heroes):
        for h in heroes:
            if h.health > 0:
                h.health = h.health - self.damage


class Hero(GameEntity):
    def __init__(self, name, health, damage, super_ability):
        super().__init__(name, health, damage)
        self.__super_ability = super_ability

    @property
    def super_ability(self):
        return self.__super_ability

    @super_ability.setter
    def super_ability(self, value):
        self.__super_ability = value

    def hit(self, boss):
        if boss.health > 0:
            boss.health = boss.health - self.damage

    def apply_super_ability(self, boss, heroes):
        pass


class Warrior(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, "CRITICAL_DAMAGE")

    def apply_super_ability(self, boss, heroes):
        coeff = randint(2, 5)
        boss.health = boss.health - coeff * self.damage
        print(f'Warrior hits critically: {coeff * self.damage}')


class Magic(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, "BOOST")

    def apply_super_ability(self, boss, heroes):
        boost = randint(2, 4)
        print(f'Boost: {boost}')
        for h in heroes:
            if h.health > 0:
                h.damage += boost


class Medic(Hero):
    def __init__(self, name, health, damage, heal_points):
        super().__init__(name, health, damage, "HEAL")
        self.__heal_points = heal_points

    @property
    def heal_points(self):
        return self.__heal_points

    @heal_points.setter
    def heal_points(self, value):
        self.__heal_points = value

    def apply_super_ability(self, boss, heroes):
        for h in heroes:
            if h.health > 0 and h != self:
                h.health += self.heal_points


class Berserk(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, "SAVE_DAMAGE_AND_REVERT")

    def apply_super_ability(self, boss, heroes):
        for h in heroes:
            if h.health > 0:
                if h.health - boss.damage:
                    h.damage = h.damage + boss.damage // 8
                else:
                    boss.damage = boss.damage


class Hucker(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, "HACKER")

    def apply_super_ability(self, boss, heroes):
        rndnt = randint(2, 5)
        for h in heroes:
            if h.health > 0:
                boss.health = boss.health - rndnt
                h.health = h.health + rndnt


class Golem(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, "GOLEM")

    def apply_super_ability(self, boss, heroes):
        for h in heroes:
            if h.health > 0 and h != self:
                boss.damage = boss.damage // 5
                h.health = h.health - boss.damage


class Thor(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, "JAM")

    def apply_super_ability(self, boss, heroes):
        round_num = randint(1, 5)
        print(boss.damage, 'this boss damadge')
        for h in heroes:
            if h.health > 0 and round_number == round_num:
                boss.damage = 0
                print('boss stunned')
                break
            else:
                boss.damage = 50


round_number = 0


def print_statistics(boss, heroes):
    print(f'ROUND {round_number} ______________')
    print(boss)
    for h in heroes:
        print(h)


def is_game_finished(boss, heroes):
    if boss.health <= 0:
        print("Heroes won!!!")
        return True
    all_heroes_dead = True
    for h in heroes:
        if h.health > 0:
            all_heroes_dead = False
            break
    if all_heroes_dead:
        print("Boss won!!!")
    return all_heroes_dead


def start_game():
    boss = Boss("Dragon", 10000, 50)
    warrior = Warrior("Herold", 270, 10)
    doc = Medic("Aibolit", 250, 5, 15)
    magic = Magic("Gendolf", 260, 20)
    berserk = Berserk("Gats", 280, 20)
    assistant = Medic("Med Brat", 290, 10, 5)
    hucker = Hucker('huckerName', 240, 8)
    golem = Golem('GolemName', 500, 5)
    thor = Thor('Thor', 250, 10)
    heroes_list = [warrior, doc, magic, berserk, assistant, hucker, golem, thor]

    print_statistics(boss, heroes_list)

    while not is_game_finished(boss, heroes_list):
        round(boss, heroes_list)


def round(boss, heroes):
    global round_number
    round_number += 1
    boss.hit(heroes)
    for h in heroes:
        if h.health > 0:
            h.hit(boss)
            h.apply_super_ability(boss, heroes)
    print_statistics(boss, heroes)


start_game()
