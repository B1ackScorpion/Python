# Задача 31:
# 0 1 1 2 3 5 8 13 21
# def f(n):
#     if n == 0 or n == 1:
#         return 1
#     return f(n-1) + f(n-2)

# n = int(input())
# print(f(n-2))


# Задача 33:
# n = int(input())
# list_1 = list()
# for i in range(n):
#     x = int(input())
#     list_1.append(x)
# max_n = max(list_1)
# min_n = min(list_1)
# for i in range(len(list_1)):
#     if list_1[i] == max_n:
#         list_1[i] = min_n
# print(list_1)


# Задача 35:
# def prime(n):
#     flag = True
#     i = 2
#     while i < n and flag:
#         if n % i == 0:
#             flag = False
#         i += 1
#     if flag:
#         return 'yes'
#     else:
#         return 'no'
    
# n = int(input())
# print(prime(n))


# Задача 37:
# def f(n):
#     if n == 0:
#         return ''
#     k = int(input())
#     return f(n-1) + f'{k}'

# n = int(input())
# print(f(n))


# def f(a, b):
#     b -= 1
#     if b == 0:
#         return a
#     return f(a, b) * a

# a = 5
# b = 3
# print(f(a, b))


def sum(a, b):  
    if b == 0:
        return a
    b -= 1
    return sum(a, b) + 1

a = 3
b = 5
print(sum(a, b))