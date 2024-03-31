# Задача 17:
# list_1 = [1, 1, 2, 3, 5, 5]
# print(len(set(list_1)))

# Задача 19:
# list_1 = [5, 4, 6, 7 ,-10]
# k = int(input())
# k = k % len(list_1)
# list_res = []
# for i in range(k):
#     list_res.append(list_1[len(list_1) - 1 - i])
# print(list_res)
# for i in range(len(list_1) - k):
#     list_res.append(list_1[i])
# print(list_res)

# Задача 21:
# list_1 = [{'V': 'S001'}, {'V': 'S002'}, {'VI': 'S001'}, {'VI': 'S005'}, {'VII': 'S005'}, {'V': 'S009'}, {'VIII': 'S007'}]
# set_1 = set()
# for i in list_1:
#     for j in i:
#         set_1.add(i[j])
# print(set_1)

# Задача 23:
# list_1 = [0, -1, 5, 2, 3]
# count = 0
# for i in range(1, len(list_1)):
#     if list_1[i] > list_1[i-1]:
#         count += 1
# print(count)
