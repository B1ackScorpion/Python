# Задача 9:
# n = int(input())
# i = 1
# result = 1
# while i <= n:
#     result *= i
#     i += 1
# print(result)


# Задача 11:
# n = int(input())
# n0 = 0
# n1 = 0
# n2 = 1
# i = 2
# while n0 < n:
#     n0 = n1 + n2
#     n1 = n2
#     n2 = n0
#     i += 1
#     if n0 > n:
#         i = -1
# print(i)


# Задача 11:
# n = int(input())
# k = 0
# max = 0
# for i in range(n):
#     x = int(input())
#     if x > 0:
#         k += 1
#     else: 
#         if max < k:
#             max = k
#         k = 0
# print(max)


n = int(input())
max = -1
min = 3001
for i in range(n):
    x = int(input())
    if x > max:
        max = x
    if x < min:
        min = x
print(max, min)