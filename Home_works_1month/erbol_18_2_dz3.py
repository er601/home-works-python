data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')

letters = []
numbers = []

for i in data_tuple:
    if type(i) == str:
        letters.append(i)
    else:
        numbers.append(i)

del numbers[0]
letters.append(numbers.pop(0))
numbers.insert(1, 2)
numbers.sort()
letters.reverse()
letters[1], letters[-2] = 'G', 'c'
numbers = 1 ** 2, 2 ** 2, 3 ** 2

print(tuple(letters))
print(tuple(numbers))


# ---------Доп---Задание---------

rus_letters = {"а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"}


print(type(rus_letters))
students = []

while True:
    student = input('Введите имя: ')

    if student == 'exit':
        print('exit...')
        break

    elif len(student) > 10 or len(student) < 3:
        print('слишком длинное имя или короткое')
        continue

    elif not student.isalpha():
        print('Только буквы в имени!')
        continue

    elif rus_letters.intersection(set(student.title())):  #Метод intersection()возвращает набор, содержащий сходство между двумя или более наборами.
        print('only english letters please !')
        continue

    students.append(student.title())
    print(students)
