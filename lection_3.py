# Функции
# def sumNumbers(n): # Создание функции
#     summa = 0
#     for i in range(1, n +1):
#         summa += i
#     return summa

# a = sumNumbers(5)
# print(a)


# def sum_str(*args): # * - неограниченное кол-во аргументов
#     res = ''
#     for i in args:
#         res += i
#     return res

# print(sum_str('q', 'e', 'l'))
# print(sum_str('q', 'e', 'l', 's', 'w'))


# Модули
# import modul_1 # Импорт модуля
# print(modul_1.max1(5, 9))

# from modul_1 import max1 # Импорт определенной функции из модуля
# print(max1(10, 9))

# from modul_1 import * # Импорт всех функций из модуля
# print(max1(8, 4))

# import modul_1 as m1
# print(m1.max1(10, 9))


# Рекурсия
# def fib(n):
#     if n in [1, 2]:
#         return 1
#     return fib(n-1) + fib(n-2)

# list_1 = []
# for i in range(1, 10):
#     list_1.append(fib(i))
# print(list_1)



# Быстрая сортировка
# def quick_sort(array):
#     if len(array) <= 1:
#         return array
#     else:
#         pivot = array[0]
#     less = [i for i in array[1:] if i <= pivot]
#     greater = [i for i in array[1:] if i > pivot]
#     return quick_sort(less) + [pivot] + quick_sort(greater)

# print(quick_sort([14, 5, 9, 6, 3, 58, 7, 5, 2, 7]))



# Сортировка слиянием
def merge_sort(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1
        while i < len(left):
            nums[k] = right[j]
            j += 1
            k += 1

list_1 = [1, 5, 6, 9, 8, 7, 2, 1, 55, 2, 4]
merge_sort(list_1)
print(list_1)