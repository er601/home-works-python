from random import randint
from datetime import datetime as dt
bot = randint(1, 100)
attempt = 0
startTime = dt.now()
while True:
    try:
        user = int(input('Угадайте число от 1 до 100: '))
        if user == 0:
            print('exit...')
            break
        elif user > 100:
            print('Загаданное число только от 1 до 100')
            continue
        elif user < 1:
            print('Загаданное число положительное (от 1 до 100)')
            continue
        if user < bot:
            print('больше')
            attempt += 1
        elif user > bot:
            print('меньше')
            attempt += 1
        else:
            print('Угадал !')
            res = dt.now() - startTime
            print(f'Общее колличество попыток: {attempt}, Время игры: {res}')
            break
    except:
        print('Введите только числа!')
