from logger import input_data, print_data, change_data, delete_data

def interface():
    print("Добрый день! Вы попали на специальный бот справочник от GeekBrains! \n   Доступные команды: \n   1 - запись данных \n   2 - вывод данных \n   3 - изменение данных \n   4 - удаление данных")
    command = input('Введите номер команды: ')
    while command != '1' and command != '2' and command != '3' and command != '4':
        print('Неправильный ввод!')
        command = input('Введите номер команды: ')
    if command == '1':
            input_data()
    elif command == '2':
            print_data()
    elif command == '3':
            change_data('изменить')
    elif command == '4':
            delete_data('удалить')