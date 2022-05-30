# 1 Написать функцию, которая возвращает первое слово из полученного предложения.
# word = input('Ваше предложение: ')
# def first_word(word='Hello world'):
#     return word.split()[0]
#
# if word == '':
#     print(first_word())
# else:
#     print(first_word(word))




# 2 Написать функцию, которая принимает неограниченное количество чисел и возвращает их среднее арифметическое.
# nums = []
# while True:
#     numbers = int(input('Введите число: '))
#     def average(*args):
#         nums.append(numbers)
#         print(nums, 'nums')
#         args = sum(nums) // len(nums)
#         return args
#     print(average(nums))





# 3 Написать функцию, проверяющую надежность пароля.

while True:
    password = input('your password: ')
    def validity(obj):
        if len(password) >= 6:
            if password.isalpha():
                print('Используйте цифры тоже !')
            elif password.isdigit():
                print('Используйте буквы тоже !')
            else:
                return obj, 'Надёжный пароль !'
        else:
            # return 'note found'
            return False
    print(validity(password))






# Экстра Задача

names = ['jack', 'sam', 'kate', 'steve', 'sam', 'sam', 'kate']
names1 = ['ali', 'said', 'umar', 'bakr', 'bakr']

def frequently(obj):
    most_f = []
    for i in obj:
        c = 0
        if obj.count(i) > 1:
            c += 1
            most_f.append(i)
    return set(most_f)
print(frequently(names))
print(frequently(names1))
