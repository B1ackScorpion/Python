from data_create import name_data, surname_data, phone_data, address_data



def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    var = int(input(f"В каком формате записать данные?\n\n"
                    f"1 Вариант: \n"
                    f"{name}\n{surname}\n{phone}\n{address}\n\n" 
                    f"2 Вариант: \n"
                    f"{name};{surname};{phone};{address}\n"
                    f"Выберете вариант: "))
    
    while var != 1 and var != 2:
        print('Неправильный ввод')
        var = int(input('Выберете вариант: '))

    if var == 1:
        with open('data_first_variant.csv', 'a', encoding='utf-8') as f:
            f.write(f"{name}\n{surname}\n{phone}\n{address}\n\n")
    elif var == 2:
        with open('data_second_variant.csv', 'a', encoding='utf-8') as f:
            f.write(f"{name};{surname};{phone};{address}\n\n")


def print_data():
    print('Вывожу данные из 1 файла: \n')
    with open('data_first_variant.csv', 'r', encoding='utf-8') as f:
        data_first = f.readlines()
        data_first_list = []
        j = 0
        for i in range(len(data_first)):
            if data_first[i] == '\n' or i == len(data_first) - 1:
                data_first_list.append(''.join(data_first[j:i+1]))
                j = i
        print(''.join(data_first_list))


    print('Вывожу данные из 2 файла: \n')
    with open('data_second_variant.csv', 'r', encoding='utf-8') as f:
        data_second = f.readline()
        print(*data_second)


def select_file(command_word):
    command_word = command_word
    var = int(input('С каким файлом вы хотите работать? '))
    while var != 1 and var != 2:
        print('Такого файла не существует! Выберете один из двух файлов.')
        var = int(input('С каким файлом вы хотите работать? '))
    if var == 1:
        file_name = "data_first_variant.csv"
        x = 5
        symbol = '\n'
    elif var == 2:
        file_name = "data_second_variant.csv"
        x = 2
        symbol = ';'
    with open(file_name, 'r', encoding='utf-8') as f:
        var_data = f.readlines()
    count = 0
    for i in range(len(var_data)):
        if var_data[i] == '\n':
            count += 1
    num = int(input(f'Какую запись вы хотите {command_word}? '))
    while num > count or num < 1:
        print('Запись под этим номером не найдена! Выберете существующую запись.')
        num = int(input(f'Какую запись вы хотите {command_word}? '))
    return file_name, x, symbol, count, num, var_data


def change_data(command_word):
    command_word = command_word
    file_name, x, symbol, count, num, var_data = select_file(command_word)
    print('Введите новые данные:')
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    new_var = []
    for i in range(len(var_data) - (count + 1 - num) * x):
        new_var.append(var_data[i])
    new_var.append(''.join(f"{name}{symbol}{surname}{symbol}{phone}{symbol}{address}\n\n"))
    for i in range(len(var_data) - (count - num) * x, len(var_data)):
        new_var.append(var_data[i])
    with open(file_name, 'w', encoding='utf-8') as f:
        for i in range(len(new_var)):
            f.write(new_var[i])


def delete_data(command_word):
    command_word = command_word
    file_name, x, symbol, count, num, var_data = select_file(command_word)
    new_var = []
    for i in range(len(var_data) - (count + 1 - num) * x):
        new_var.append(var_data[i])
    for i in range(len(var_data) - (count - num) * x, len(var_data)):
        new_var.append(var_data[i])
    with open(file_name, 'w', encoding='utf-8') as f:
        for i in range(len(new_var)):
            f.write(new_var[i])