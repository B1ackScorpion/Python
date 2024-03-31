# Задача 25:
# stroka = input().split()
# res = {}
# for i in stroka:
#     if i in res:
#         print(f'{i}_{res[i]}', end = ' ')
#     else:
#         print(i, end = ' ')
#     res[i] = res.get(i, 0) + 1
# print(res)


# Задача 27:
# stroka = input().split()
# set_1 = set()
# for i in stroka:
#     set_1.add(i.lower())
# print(len(set_1))


# var1 = '5 4' 
# var2 = '1 3 4 5 7 9' 
# var3 = '2 3 4 5' 

# # Введите ваше решение ниже
# v2 = set(var2.split())
# v3 = set(var3.split())
# new_var = list(v2.intersection(v3))
# for i in range(len(new_var)):
#     new_var[i] = int(new_var[i])
# new_var = sorted(new_var)
# for i in new_var:
#     print(i, end= ' ')


arr = [5, 8, 6, 4, 9, 2, 7, 3]
max = 0
for i in range(1, len(arr) - 1):
    if max < arr[i] + arr[i-1] + arr[i+1]:
        max = arr[i] + arr[i-1] + arr[i+1]
print(max)