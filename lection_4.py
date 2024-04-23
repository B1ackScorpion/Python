#  Lambda функции
# def f(x):
#     return x*x
# print(type(f))


# def calk1(a, b):
#     return a+b

# def calk2(a, b):
#     return a*b

# def math(op, x, y):
#     print(op(x, y))


# calk1 = lambda a,b: a + b #Lambda функция

# math(calk1, 5, 45)

# math(lambda a,b: a + b, 5, 45)


#Задача 1
# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = list()
# for i in data:
#     if i % 2 == 0:
#         res.append((i, i**2))

# print(res)

# def select(f, col):
#     return [f(x) for x in col]

# def where(f, col):
#     return [x for x in col if f(x)]

# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = select(int, data)
# print(res)
# res = where(lambda x: x % 2 == 0, res)
# print(res)
# res = list(select(lambda x: (x, x**2), res))
# print(res)



# Фунция map(f(x), x)
# list_1 = [x for x in range(1, 20)]
# print(list_1)
# list_1 = list(map(lambda x: x + 10, list_1))
# print(list_1)



# Фунция filter(f(x), x)
# data = [15, 65, 9, 36, 175]
# res = list(filter(lambda x: x % 10 == 5, data))
# print(res)



# Функция zip()
# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 14, 7]
# data = list(zip(users, ids))
# print(data)



# Функция enumerate() - позволяет пронумеровать набор данных
# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# data = list(enumerate(users))
# print(data)



# Работа с файлами
# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a', encoding='utf-8')
# data.writelines(colors)
# data.close()


# with open('file.txt', 'w') as data:
#     data.write('line 1\n')
#     data.write('line 2\n')


# data = open('file.txt', 'r')
# for line in data:
#     print(line)
# data.close()


# with open('file.txt', 'r') as data:
#     for line in data:
#         print(line)



# Модуль OS
# import os
# os.chdir('C:/Users/danii/Desktop/GeekBrains') #Смена текущей директории


# import os
# print(os.getcwd()) #Текущая директория


# import os
# print(os.path.basename('C:/Users/danii/Desktop/GeekBrains/Python/lection_4.py')) #Базовое имя пути


# import os
# print(os.path.abspath('lection_4.py')) #Возвращает нормализованный абсолютный путь



# Модуль shutil
# import shutil
# shutil.copyfile(src, dst) #Копирут содержимое (но не метаданные) файла src в файл dst
# shutil.copy(src, dst) #Копирует содержимое файла src в файл или папку dst
# shutil.rmtree(path) #Удаляет текущую директорию (path) и все поддиректроии