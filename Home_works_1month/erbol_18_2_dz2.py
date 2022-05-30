vowelsLetter = 'аеёийоуыэюяaeiouy'
Vowels_letter = vowelsLetter.upper()
while True:
    vowels = 0
    consonants = 0
    user_word = input('Слово: ')
    if user_word == 'exit':
        print('exit...')
        break
    for i in user_word:
        if i in vowelsLetter or i in Vowels_letter:
            vowels += 1
        else:
            consonants += 1
    print("Колличество букв:", len(user_word))
    print('Согласных букв:', consonants)
    print('Гласных букв:', vowels)
    print(f'Гласные/Согласные: {round(vowels / len(user_word) * 100, 2)}% / {round(consonants / len(user_word) * 100, 2)}%')
