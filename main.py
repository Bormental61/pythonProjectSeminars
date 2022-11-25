# 1. Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.
# *Примеры:*
# - 5, 25 -> да
# - 4, 16 -> да
# - 25, 5 -> да
# - 8,9 -> нет

# var1
# num1 = int(input('Введите первое число: '))
# num2 = int(input('Введите второе число: '))
#
# if num1 ** 2 == num2 or num2 ** 2 == num1:
#     print ('да')
# else:
#     print ('нет')

# var2
# num1, num2 = map(int, input().split(', '))
# if num1 ** 2 == num2 or num2 ** 2 == num1:
#     print ('да')
# else:
#     print ('нет')

# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
# Примеры:
# - 1, 4, 8, 7, 5 -> 8
# - 78, 55, 36, 90, 2 -> 90

# var1
# numbers = []
# for _ in range(5):
#     n = int(input())
#     numbers.append(n)
# maxx = numbers[0]
# for el in numbers:
#     if el > maxx:
#         maxx = el
# print(maxx)

# var2
# maxx = int(input())
# for _ in range(4):
#     n = int(input())
#     if n > maxx:
#         maxx = n
# print(maxx)

# var3
# print(max(map(int, input().split(', '))))

# 3. Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N
# *Примеры:*
# - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5

# var1
# N = int(input())
# numbers = []
# for s in range(-N , N + 1):
#     numbers.append(s)
# print(numbers)

# var2
# n = int(input())
# if n > 0:
# for i in range(-n, n):
# print(i, end=', ')
# print(n)
# else:
# for i in range(-n, n, -1):
# print(i, end=', ')
# print(n)

# var3
# n = int(input())
# print(*list(range(-n, n + 1)), sep=', ')

# var4
# n = int(input())
# some_str = ''
# for i in range(-n, n + 1):
#     some_str += str(i) + ', '
# print(some_str[0: -2])

# 4. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
# *Примеры:*
# - 6,78 -> 7
# - 5 -> нет
# - 0,34 -> 3

# var1
# some_str = input()
# if ',' in some_str:
#     some_list = some_str.split(',')
#     print(some_list[1][0])
# else:
#     print('нет')

# var2
# some_str = input()
# if ',' in some_str:
#     ind = some_str.index(',')
#     print(some_str[ind + 1])
# else:
#     print('нет')

# var3
# print(int(float(input())*10%10))

# var4
# num = float(input("Введите число: "))
# res = int((num*10) % 10)
# print(res)

# var5
# number = float(input())
# if number % 1 != 0:
#     number = number * 10
#     number = int(number)
#     print(number % 10)
# else:
#     print('нет')

# 5. Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.

# n = int(input())
# if (n % 5 == 0 and n % 10 == 0 or n % 15 == 0) and n % 30 != 0:
#     print('да')
# else:
#     print('нет')

# 11. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
# *Пример: *
# - Для N = 5: 1, -3, 9, -27, 81

# n = int(input())
# for i in range(n - 1):
#     print((-3) ** i, end=', ')
# print((-3) ** (i + 1))

# 12. Для натурального n создать словарь индекс - значение, состоящий из элементов последовательности 3n + 1.
# *Пример: *
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# some_dict = {}
# n = int(input())
# for i in range(1, n + 1):
#     some_dict[i] = 3 * i + 1
# print(some_dict)

# 13. Напишите программу, в которой пользователь будет задавать две строки, а программа - определять количество вхождений одной строки в другой.

# var_1 Версия Рината
# s1 = input()
# s2 = input()
# c = 0
# for i in range(len(s1) - len(s2) + 1):
#     print(s1[i:i+len(s2)])
#     if s1[i:i+len(s2)] == s2:
#         c += 1
# print(c)

# var_2 Короткая версия с count
# s1 = input()
# s2 = input()
# print(s1.count(s2) or s2.count(s1))

