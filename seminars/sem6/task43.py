"""
Задача №43. Решение в группах

Дан список чисел. Посчитайте, сколько в нем пар
элементов, равных друг другу. Считается, что любые
два элемента, равные друг другу образуют одну пару
которую необходимо посчитать. Вводится список
чисел. Все числа списка находятся на разных
строках.

Ввод: Вывод:

1 2 3 2 3 2
"""
from random import randint


def array_creater(length):
    result = [randint(1, 10) for i in range(length)]
    print(result)
    return result


def pair_finder(array:list):
    counter = 0
    temp_list = []
    for i in range(len(array)):
        if array.count(i) == 2 and not i in temp_list:
            counter += 1

    return counter


array = array_creater(15)
print(pair_finder(array))
