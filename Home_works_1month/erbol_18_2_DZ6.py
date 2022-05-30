ten = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

evens = list(filter(lambda x: x % 2 == 0, ten))
print(evens)

evens = list(map(lambda x: x ** 2, evens))

print(evens)

def def_index(lst=ten):
    while 1:
        try:
            idx = input('Введите индекс: ')
            if idx == 'exit':
                print('exit...')
                break
            else:
                print(lst[int(idx)])
        except IndexError:
            print(f'Введите индекс до {len(lst)-1} ')

def_index()


