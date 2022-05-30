from datetime import datetime as dt
from random import randint
startTime = dt.now()

name = input('name: ')
attempts = int(input('Введите колличество попыток: '))
count = 0
while count != attempts:
    a = randint(1, 9)
    b = randint(1, 9)
    answer = input(f'{a} * {b} = ? ')
    result = a * b
    with open('result.txt', 'a') as file:
        if int(answer) == result:
            file.write(f'{a} * {b} = {answer} ({result}) правильно\n')
            print('верно ', result)
            count += 1
        else:
            file.write(f'{a} * {b} = {answer} ({result}) неправильно\n')
            print('неверно ', result)
            count += 1
    print(f'Колличество оставшихся попыток {attempts - count}')

res = dt.now() - startTime
with open('result.txt', 'a') as file:
    file.write(f'было {attempts} попыток, потраченное время: {res}, имя: {name.title()}')

