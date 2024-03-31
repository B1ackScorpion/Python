# list_1 = []
# list_1 = list()
# list_1 = [1, 2, 3, 8]
# print(list_1)
# print(*list_1) #Вывод списка без скобочек

# for i in list_1:
#     print(i)

# print(len(list_1)) #Длина списка
# print(list_1[0])

# list_1 = [1, 5]
# print(list_1)
# list_1.append(8) #Добавление элемента в конец списка
# print(list_1)

# list_1 = []
# for i in range(5):
#     list_1.append(i)
#     print(list_1)

# list_1 = [12, 7 ,-1, 21, 0]
# print(list_1.pop()) #Удаляет последний элемент списка и возвращает его
# print(list_1)
# print(list_1.pop(0)) #Удаление конкретного элемента

# list_1 = [12, 7 ,-1, 21, 0]
# list_1.insert(2, 11) #Добавление элемента на нужную позицию .insert(x, y) x - позиция,y - элемент
# print(list_1)

# print(list_1[x:y:z]) #x - начало, y - конец, z -шаг

# --------------------------------------------------------------------------------

# Кортеж - неизменяемый список
# t = ()
# print(type(t))

# t = (1, 5, 3,)
# print(type(t))

# v = [1, 8 ,9]
# print(v)
# print(type(v))

# v = tuple(v)
# print(v)
# print(type(v))


# # a, b = 1, 2 - Множественное присвоение

# a, b , c = v
# print(a, b, c)

# --------------------------------------------------------------------------------

# d = {} #Словарь
# d = dict()

# d['q'] = 'qwerty'
# print(d)

# d['w'] = 'werty'
# print(d)

# print(d['q'])

# del d['q'] #Удаление элемента по ключу
# print(d)


# dictionary = {}
# dictionary = {'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
# del dictionary['left']
# for item in dictionary:
#     print('{}: {}'.format(item, dictionary[item]))
# for (k,v) in dictionary.items():
#     print(k, v)
# print(dictionary.items()) #Список из кортежей(ключ, значение)

# --------------------------------------------------------------------------------

# # В множестве хранятся только уникальные значения
# colors = {'red', 'green', 'blue'}
# print(colors)
# colors.add('gray')
# print(colors)
# colors.remove('red') #Удалает элемент. Если такого нет, то выдает ошибку
# print(colors)
# colors.discard('red') #Проверяет на наличие элемента и удаляет его
# print(colors)
# colors.clear() #Очистка множества
# print(colors)

# q = set

# Операции со множествами в Python
# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy()                # c = {1, 2, 3, 5, 8}
# u = a.union(b)              # u = {1, 2, 3, 5, 8, 13, 21}
# i = a.intersection(b)       # i = {8, 2, 5}
# dl = a.difference(b)        # dl = {1, 3}
# dr = b.difference(a)        # dr = {13, 21}
# q = a.union(b).difference(a.intersection(b))    # q = {1, 21, 3, 13}

# a = {1, 8, 6}
# b = frozenset(a) #Замороженное мно-во(нельзя изменять)
# print(b)

# --------------------------------------------------------------------------------

# List comprehension
# list_1 = [exp for item in itereble]
# list_1 = [i for i in range(1, 101)]
# print(list_1)

# list_1 = [exp for item in itereble (if condition)]
# list_1 = [i for i in range(1, 101) if i % 2 == 0]
# print(list_1)

list_1 = [(i, i*i) for i in range(1, 10) if i % 2 == 0]
print(list_1)