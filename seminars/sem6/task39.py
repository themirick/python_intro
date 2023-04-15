"""
Задача №39. Решение в группах

Даны два массива чисел. Требуется вывести те элементы
первого массива (в том порядке, в каком они идут в первом
массиве), которых нет во втором массиве. Пользователь вводит
число N - количество элементов в первом массиве, затем N
чисел - элементы массива. Затем число M - количество
элементов во втором массиве. Затем элементы второго массива
Ввод: Вывод:
7 3 3 2 12

3 1 3 4 2 4 12

6

4 15 43 1 15 1 (каждое число вводится с новой строки)

"""
from random import randint


def array_creater(length):
    result = [randint(1, 10) for i in range(length-1)]
    print(result)
    return result


def lists_compare(list1, list2):
    for i in list1:
        if i in list2:
            continue
        print(i, end=" ")


lists_compare(array_creater(5), array_creater(7))
