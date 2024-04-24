#Задача 47:
# values = [1, 23, 42, 'asdfg']
# transformated_values = list(map(lambda x: x, values))
# if values == transformated_values:
#     print('ok')
# else:
#     print('fail')
# print(transformated_values)


#Задача 49:
# from math import pi

# def find_farthest_orbit(list_of_orbits):
#     list_1 = [i for i in list_of_orbits if i[0] != i[1]]
#     list_s = [(pi * i[0] * i[1]) for i in list_1]
#     max_s = list_s.index(max(list_s))
#     return list_1[max_s]

# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4,3)]
# print(*find_farthest_orbit(orbits))


#Задача 51:
# def same_by(characteristic, object):
#     result = True
#     list_1 = [characteristic(x) for x in object]
#     for i in range(len(list_1) - 1):
#         if list_1[i] != list_1[i+1]:
#             result = False
#     return result

# values = [0, 2, 10, 6]
# if same_by(lambda x: x % 2, values):
#     print('same')
# else:
#     print('different')


# Дз 1:
# def print_operation_table(operation, num_rows, num_columns):
#     if num_rows < 2:
#         print('ОШИБКА! Размерности таблицы должны быть больше 2!')
#         return
#     else:
#         list_1 = [[operation(i,j) for j in range(1, num_rows + 1)] for i in range(1, num_columns + 1)]     
#         for row in list_1:
#             print(' '.join([str(elem) for elem in row]))


# print_operation_table(lambda x, y: x * y, 9, 9)


# Дз 2:
def syllables(list_1):
    vowels = ['а', 'я', 'у', 'ю', 'у', 'ю', 'о', 'е', 'ё', 'ы']
    list_2 = []
    for i in range(len(list_1)):
        count = 0
        for let in list_1[i]:
            for elem in vowels:
                if let == elem:
                    count += 1
        list_2.append(count)
    return list_2

stroka = 'пара-ра-рам'
list_1 = stroka.split(' ')
if len(list_1) < 2:
    print('Количество фраз должно быть больше одной!')
else:
    print(syllables(list_1))
    if len(set(syllables(list_1))) == 1:
        print('Парам пам-пам')
    else:
        print('Пам парам')