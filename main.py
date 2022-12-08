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

# 20. Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.
# ввести кол-во строк, потом строки. Строки должны записаться в текстовый файл.
# После вводим число, если есть число в файле, то написать ДА

# a = int(input('Ввод числа '))
#
# with open('file.txt', 'w', encoding='utf-8') as file:
#     for _ in range(a):
#         file.write(input() + '\n')
#
# c = input('Введите искомое ')
#
# with open('file.txt', 'r', encoding='utf-8') as file:
#     strings = file.read().splitlines()
#
#     count = 0
#     b = False
#     for line in strings:
#         count += 1
#         if c in line:
#             b = True
#             print(f'DA ->  {count}')
#
#     if not b:
#         print('NET')

# 21. Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что ее нет
# Пример:
# список: ['qwe', 'asd', 'zxc', 'qwe', 'ertqwe'], ищем 'qwe', ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1

# some_list = ["123", "234", 123, "567"]
# print(some_list)
#
# a = input('Введите искомое ')
#
# count = 0
# count2 = 0
# b = False
# for line in some_list:
#     count += 1
#     if a == line:
#         count2 += 1
#         if count2 == 2:
#             b = True
#             print(f'{count - 1}  ')
#             break
# if not b:
#     print('-1')

# Напишите функцию, которая принимает номер месяца и язык (русский или английский), а возвращает его название.
# Ввод:
# print(month_name(3, "en"))
# March
# Ввод
# print(month_name(3, "ru"))
# март

# def month(x, y):
#     listEn = ('January', 'February', 'March', 'April', 'May', 'June',
#               'July', 'August', 'September', 'October', 'November', 'December')
#     listRu = ('январь', 'февраль', 'март', 'апрель', 'май', 'июнь',
#               'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь')
#     if x > 0 and x < 13:
#         if y == 'en':
#             return listEn[x - 1]
#
#         if y == 'ru':
#             return listRu[x - 1]
#
#
# print(month(5, 'ru'))

# 27. Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число.
# В качестве символа-разделителя используйте пробел.

# var 1
# some_str = input()
# int_list = list(map(int, some_str.split()))
# print(max(int_list))
# print(min(int_list))

# var 2
# text = str(input("Enter a number: "))
# arr = [int(n) for n in text.split()]
# print(arr)

# 28. Найдите корни квадратного уравнения Ax2 + Bx + C = 0 двумя способами:
#   1) c помощью математических формул нахождения корней квадратного уравнения
#   2) с помощью дополнительных библиотек Python

# var1 algorithm
# import math
# a = float(input('a = '))
# b = float(input('b = '))
# c = float(input('c = '))
# discr = pow(b, 2) - 4 * a * c
# print(f'Дискриминант = {discr}')
# if discr > 0:
# x1 = (-b + math.sqrt(discr)) / (2 * a)
# x2 = (-b - math.sqrt(discr)) / (2 * a)
# print(f'x1 = {x1} \nx2 = {x2}')
# elif discr == 0:
# x = -b / (2 * a)
# print(f'x = {x}')
# else:
# print('Корней нет')

# var2 Python
# import sympy
# a = float(input())
# b = float(input())
# c = float(input())
# x = sympy.Symbol('x')
# print(sympy.solve(a * x ** 2 + b * x + c))

# 29. Задайте два числа. Напишите программу, которая найдет НОК (наименьшее общее кратное) этих двух чисел.

# import sympy
# a = int(input())
# b = int(input())
# print(sympy.lcm(a, b))
