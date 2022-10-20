list_of_digits = []
checking = False

while not checking:
    size = int(input('Введите размер списка: '))
    if size <= 0:
        print('Введено неверное значение, повторите попытку')
    else:
        checking = True

print('Введите значения: ')
for i in range(0, size):
    digit = int(input())
    list_of_digits.append(digit)

print('Заданный список чисел: ', list_of_digits)

list_1 = list(set(list_of_digits))
print('Список без повторов: ', list_1)

list_1.reverse()
print('Список по убыванию: ', list_1)