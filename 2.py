my_text = input('Введите текст: ')
print('Количество слов в тексте: ', my_text.count(' ') + 1)

my_text_2 = my_text.lower()
count_of_vowels = 0
count_of_consonants = 0

for i in range(0, len(my_text_2)):
    if my_text_2[i] in 'aoeiuyаеёиыуюэяо':
        count_of_vowels += 1
    elif my_text_2[i] in 'qwrtpsdfghjklzxcvbnmбвгджзйклмнпрстфхцчщъь':
        count_of_consonants += 1

print('Количество гласных букв: ', count_of_vowels)
print('Количество согласных букв: ', count_of_consonants)

if count_of_consonants == count_of_vowels:
    print('Гласных столько же, сколько и согласных!\nГласные буквы: ')
    for i in range(0, len(my_text_2)):
        if my_text_2[i] in 'aoeiuyаеёиыуюэяо':
            print(my_text[i])