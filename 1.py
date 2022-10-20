checking = False

while not checking:
    print('Введите диапазон значений: ')
    left_border = int(input('Левая граница: '))
    right_border = int(input('Правая граница: '))

    if (left_border < 0 and right_border <= 0) or right_border < left_border:
        print('Неверные значения, повторите попытку')
    else: checking = True

if left_border >= 0:
    for i in range(left_border, right_border):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(i, ' ')
elif left_border < 0:
    for i in range(2, right_border):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(i, ' ')