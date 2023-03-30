# list1 = []
# list1 = list()
# list1 = [1, 2, 3]
#
# print(list1)
# print(*list1)
# print(list1[2])
#
# list1 = [1, 5]
# print(list1)
# list1.append(8)
# print(list1)
#
#
# list1 = []
# for i in range(5):
#     list1.append(i)
#     print(list1)
#
# list1.pop()
# print(list1.pop())
# a = list1.pop()
# print(a)
#
# list1.pop(0) # удаляет элемент с укаазанным индексом
#
# list1.insert(1, 11) # первый аргумент индекс, второй - добавляемый элемент
# print(list1)
# print(len(list1))
#
# # срезы со списками тоже уместны
#
#
#
# # Кортежи
#
# t = ()
# print(type(t))
#
# t = (1)
# print(type(t))
#
# t = (1, )
# print(type(t))
#
# v = [1, 5, 8]
# print(v)
# print(type(v))
#
# v = tuple(v)
# print(v)
# print(type(v))
#
# a, b = 1, 2
# a = b = 1
#
# a, b, c = v # распоковка кортежа
#
# print(a, b, c)
#
# t = (1, 2, 3, 4, 5)
# print(t[1])
#
# for i in t:
#     print(i)
#
# for i in range(len(t)):
#     print(t[i])
#
# # t[0] = 2 can't change!
#
#
# # Словари
#
# d = {}
# d = dict()
#
# d['q'] = 'qwerty'
# d['w'] = 'jec'
# print(d)
# print(d["q"])
#
# dictionary = {}
# dictionary = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# print(dictionary)
# print(dictionary['c'])
# dictionary['a'] = 10
# print(dictionary['a'])
#
# del dictionary['b']
# print(dictionary)
#
# # for item in dictionary:
# #     # print(item)
# #     # print(f"{item}: {dictionary[item]}")
#
# print(dictionary.items())
# for (k, v) in dictionary.items():
#     print(k, v)
#
# # Множества
# colors = set()
# colors = {'red', 'green', 'blue'}
# print(colors)
#
# colors.add('green')
# print(colors)
#
# colors.add('grey')
# print(colors)
#
# # colors.remove('red') KeyError
# # print(colors)
#
# colors.remove('red')
# print(colors)
#
# colors.discard('red')
# print(colors)
#
# colors.clear()
# print(colors)
#
# # Операции со множествами
#
# a = {1, 2, 3, 4, 5, 6}
# b = {1, 4, 6, 9, 5}
#
# c = a.copy()
# print(c)
#
# u = a.union(b)
# print(u)
#
# i = a.intersection(b)
# print(i)
#
# d1 = a.difference(b)
# print(d1)
#
# d2 = b.difference(a)
# print(d2)
#
# q = a.union(b).difference(a.intersection(b))
# print(q)
#
# a = {1, 3, 8}
#
# b = frozenset(a) # Замороженное множество
#
#
# # **● SyntaxError(Синтаксическая ошибка)**
# #
# # number_first = 5
# # number_second = 7
# # if number_first > number_second  # !!!!!
# # print(number_first)
# #
# # Отсутствие :
# #
# # **● IndentationError(Ошибка отступов)**
# # number_first = 5
# # number_second = 7
# # if number_first > number_second:
# # print(number_first) # !!!!!
# #
# # Отсутствие отступов
# #
# # **● TypeError(Типовая ошибка)**
# # text = 'Python'
# # number = 5
# # print(text + number)
# #
# # Нельзя складывать строки и числа
# #
# # **● ZeroDivisionError(Деление на 0)**
# # number_first = 5
# # number_second = 0
# # print(number_first // number_second)
# #
# # Делить на 0 нельзя
# #
# # **● KeyError(Ошибка ключа)**
# # dictionary = {1: 'Monday', 2: 'Tuesday'}
# # print(dictionary[3])
# #
# # Такого ключа не существует
# #
# # **● NameError(Ошибка имени переменной)**
# # name = 'Ivan'
# # print(names)
# #
# # Переменной names не существует
# #
# # **● ValueError(Ошибка значения)**
# # text = 'Python'
# # print(int(text))
# #
# # Нельзя символы перевести в целые значения




