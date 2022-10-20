import string

my_string = input('Введите текст: ')
my_new_str = my_string.translate(my_string.maketrans('', '', string.punctuation))
print(my_new_str)
my_tuple = tuple(word for word in my_new_str.split(' '))
print(my_tuple)