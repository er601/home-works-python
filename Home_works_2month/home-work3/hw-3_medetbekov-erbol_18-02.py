# #ДЗУрок3 Дэдлайн 12.05.2022 23 59
    # 1. Создать класс Computer (компьютер) с приватными атрибутами cpu и memory.
    # 2. Добавить сеттеры и геттеры к существующим атрибутам.
    # 3. Добавить в класс Computer метод make_computations, в котором бы выполнялись арифметические вычисления с атрибутами объекта cpu и memory.
    # 4. Создать класс Phone (телефон) с приватным полем sim_cards_list (список симкард)
    # 3. Добавить сеттеры и геттеры к существующему атрибуту.
    # 4. Добавить в класс Phone метод call с входящим параметром sim_card_number и call_to_number, в котором бы распечатывалась симуляция звонка в зависимости от переданного номера сим-карты (например: если при вызове метода передать число 1 и номер телефона, распечатывается текст “Идет звонок на номер +996 777 99 88 11” с сим-карты-1 - Beeline).
    # 5. Создать класс SmartPhone и наследовать его от 2-х классов Computer и Phone.
    # 6. Добавить метод в класс SmartPhone use_gps с входящим параметром location, который бы распечатывал симуляцию проложения маршрута до локации.
    # 7. В каждом классе переопределить магический метод str которые бы возвращали полную информацию об объекте.
    # 8. Перезаписать все магические методы сравнения в классе Computer, для того чтоб можно было сравнивать между собой объекты, по атрибуту memory.
    # 9. Создать 1 объект компьютера, 1 объект телефона и 2 объекта смартфона
    # 10. Распечатать информацию о созданных объектах
    # 11. Опробовать все возможные методы каждого объекта (например: use_gps и тд.)



class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, value):
        self.__cpu = value

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        self.__memory = value

    def make_computations(self):
        return f'CPU - Memory = {self.__cpu - self.__memory}'

    def __str__(self):
        return f'cpu: {self.__cpu}, memory: {self.__memory}'

    def __gt__(self, other):
        return self.memory > other.memory

class Phone:
    def __init__(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    @property
    def sim_cards_list(self):
        return self.__sim_cards_list

    @sim_cards_list.setter
    def sim_cards_list(self, value):
        self.__sim_cards_list = value

    def call(self, sim_card_number, call_to_number):
        print(f'Идет звонок на номер {sim_card_number} с сим-карты-{call_to_number}')

    def __str__(self):
        return f"sim cards list: {self.__sim_cards_list}"



class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory, sim_cards_list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_cards_list)

    def use_gps(self, location):
        print(f'маршрут построен до {location}')

    def __str__(self):
        return f'CPU: {self.cpu}, Memory: {self.memory}, Sim-cards: {self.sim_cards_list}'



sim_cards = ['1-O!', '2-Beeline', '3-MegaCom']

computer = Computer(3500, 256)
print('computer:', computer)

phone = Phone(3)
print('phone:', phone)
phone.call('0708-997-100', sim_cards[2])

smart_phone1 = SmartPhone(1000, 64, 2)
print('smart_phone1:', smart_phone1)

smart_phone2 = SmartPhone(900, 32, 3)
print('smart_phone2:', smart_phone2)

smart_phone2.call('0999-100-200', sim_cards[1])
smart_phone2.use_gps('Восток-5')

