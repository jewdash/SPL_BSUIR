from unicodedata import name


my_dict = {
    'Торт': [
        ['Сахар', 'Молоко', 'Шоколад', 'Ваниль'],
        200,
        15],
    'Пирожное': [
        ['Сахар', 'Глазурь', 'Шоколад'],
        50,
        40],
    'Эклер': [
        ['Шоколад', 'Хлеб', 'Яйца'],
        100,
        24],
    'Ватрушка': [
        ['Сахар', 'Хлеб'],
        90,
        36],
    'Бублик': [
        ['Соль', 'Хлеб'],
        70,
        52]
    }
print(my_dict)

while True:
    print("\nМеню кондитерской:\n1 - Просмотр описания: название – описание\n2 - Просмотр цены: название – цена\n3 - Просмотр количества: название – количество\n"
          "4 - Всю информацию\n5 - Покупка\n6 - До свидания")
    req = input(">>>>> ")
    if req == '1':
        print('\nСостав кондитерских изделий ')
        for key, value in my_dict.items(): print(key,' - ',value[0])
    elif req == '2':
        print('\nСтоимость кондитерских изделий ')
        for key, value in my_dict.items(): print(key,' - ',value[1])
    elif req == '3':
        print('\nКоличество всех кондитерских изделий ')
        for key, value in my_dict.items(): print(key,' - ',value[2])
    elif req == '4':
        print('\nВся информация о кондитерских изделиях ')
        for key, value in my_dict.items():
            print(key, '- Cостав: ', value[0],', цена - ', value[1], ', количество - ', value[2])
    elif req == '5':
        check = 0
        while True:
             exit = 0
             available_meal = 0
             print("\nПрайс ")
             for key, value in my_dict.items():
                 print(key, '- Cостав: ', value[0], ', цена - ', value[1], ', количество - ', value[2])
             name_buy = input("Введите название изделия, которое нужно купить (0 - выход из раздела покупок): ")
             print(name_buy)
             if name_buy == '0':
                 print("Общая цена покупок: ", check)
                 print("Количество оставшихся товаров: ")
                 for key, value in my_dict.items():
                     print(key, ' - ', value[2])
                 break
             for key, values in my_dict.items():
                 if key == name_buy:
                     k = key
                     available_meal += 1
                     c = value[2]
             if  available_meal == 1 and c == 0 :
                 print('Товара больше нет в наличии...')
             elif  available_meal == 1 and c > 0 :
                 while True:
                     if exit > 0 : break
                     number_meal = int(input("Введите количество, которое вам нужно приобрести (0 - отказаться от покупки данного изделия): "))
                     if number_meal == 0 : break
                     print(name_buy)
                     for key, value in my_dict.items():
                         if name_buy == key and value[2] >= number_meal and number_meal > 0 :
                             check = check + (value[1] * number_meal)
                             value[2] -= number_meal
                             #my_dict.update({key: values})
                             print("Куплено! Цена - ", check)
                             exit += 1
                             check = 0
                             break
                         elif name_buy == key and value[2] < number_meal:
                             print('Такого количества нет, введите верное количество')
                         elif name_buy == key and number_meal < 0:
                             print('Введено некорректное значение, повторите ввод')
             else : print("Неправильный ввод, повторите попытку")
    elif req == '6':
        print('\nДо Свидания!')
        break
    else : print("Неверный выбор")