# Задача 39:
# n = int(input())
# list_1 = list()
# for i in range(n):
#     x = int(input())
#     list_1.append(x)
# m = int(input())
# list_2 = list()
# for i in range(m):
#     x = int(input())
#     list_2.append(x)
# count = 0
# for i in range(n):
#     for j in range(m):
#         if list_1[i] == list_2[j]:
#             count += 1
#     if count == 0:
#         print(list_1[i])
#     count = 0


# Задача 41:
# n = int(input())
# list_1 = list()
# for i in range(n):
#     x = int(input())
#     list_1.append(x)
# count = 0
# for i in range(1,n-1):
#     if list_1[i-1] < list_1[i] > list_1[i+1]:
#         count += 1
# print(count)


# Задача 43:
# list_1 = [1, 2, 3, 2, 3]
# count = 0
# for i in range(len(list_1)):
#     for j in range(i+1, len(list_1)):
#         if i != j and list_1[i] == list_1[j]:
#             count += 1
# print(count)


# Задача 45:
# k = int(input())
# list_1 = list()
# for i in range(k):
#     summa = 0
#     for j in range(1, i//2 + 1):
#         if i % j == 0:
#             summa += j
#     list_1.append(tuple([i, summa]))
# for i in range(len(list_1)):
#     for j in range(i, len(list_1)):
#         if i != j and list_1[i][0] == list_1[j][1] and list_1[i][1] == list_1[j][0]:
#             print(*list_1[i])



# list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# min_number = 0
# max_number = 10
# for i in range(len(list_1)):
#     if max_number >= list_1[i] >= min_number:
#         print(i)



a1 = 2
d = 3
n = 4
for i in range(1,n+1):
    a = a1 + (i-1) * d
    print(a)