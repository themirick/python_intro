"""

Задача №41. Решение в группах

Дан массив, состоящий из целых чисел. Напишите
программу, которая в данном массиве определит
количество элементов, у которых два соседних и, при
этом, оба соседних элемента меньше данного. Сначала
вводится число N — количество элементов в массиве
Далее записаны N чисел — элементы массива. Массив
состоит из целых чисел.

Ввод: Ввод:
5 5
1 2 3 4 5 1 5 1 5 1

Вывод: Вывод:
0 2

(каждое число вводится с новой строки)
"""

from random import randint


def array_creater(length):
    result = [randint(1, 10) for i in range(length)]
    print(result)
    return result


def middle_finder(array: list):
    counter = 0
    for i in range(1, len(array)-1):
        if array[i] > array[i+1] > array[i-1]:
            counter += 1

    return counter


array = array_creater(5)
print(middle_finder(array))
