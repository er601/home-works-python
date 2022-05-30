# #ДЗУрок5 Дэдлайн 19.05.2022 23 59 Сдаем через GitHub
# 1. Установить в свою виртуальную среду проекта внешний модуль envparse
# 2. В файле requirements.txt зафиксировать зависимости проекта с помощью команды pip freeze
# 3. Создать многомодульную игру Казино
# 4. Сам запуск игры в отдельном файле
# 5. Логика выигрыша или проигрыша в отдельном файле
# Правила игры такие :
# A. Есть массив из чисел от 1 до 30, каждый раз вы делаете ставку на определенную слоту из чисел и ставите деньги
# B. Рандомно выбирается выигрышная слота, если вы выигрываете, вам причисляется
# удвоенная сумма, той которую вы поставили, если вы загадали не выигрышную слоту -
# теряете поставленную сумму
# C. В начале игры у вас также есть деньги например 1000$, но в конце мы понимаем вы в
# выигрыше или в проигрыше
# D. значение переменной начального капитала должно считываться с системной
# переменной под названием MY_MONEY из файла settings.env
# E. После каждой ставки вам задается вопрос хотите ли вы сыграть еще, если да - то
# делаете ставку, если нет - то подводится итог игры


import os
import random
from envparse import env


class Casino:
    def __init__(self):
        self.__cash = int(os.environ.get('MY_MONEY'))
        while int(self.__cash) > 0:
            print(f"Ваш денги: {self.__cash}")
            self.__win_slot = random.randint(1, 30)
            print(self.__win_slot)
            self.__slot = int(30)
            self.__bet = int(input('Сделайте ставку: '))
            if self.__bet > self.__cash:
                print("У вас недостаточно денег! ")
            else:
                self.__choice = int(input('Выберите слот: '))
                if self.__choice > self.__slot:
                    print("Выберите слота только от 1-30")
                    userRound = input('Хотите ешё поиграть?("да" или "нет"')
                    if userRound == 'да':
                        continue
                    elif userRound == 'нет':
                        break
                    else:
                        print("да или нет?")

    @property
    def win(self):
        return self.__win_slot

    @win.setter
    def win(self, value):
        self.__win_slot = value

    @property
    def slot(self):
        return self.__slot

    @slot.setter
    def slot(self, value):
        self.__slot = value

env.read_envfile('settings.env')
