"""
Задача 18: Требуется найти в массиве A[1..N] самый близкий по
величине элемент к заданному числу X. Пользователь в первой строке
вводит натуральное число N – количество элементов в массиве. В
последующих  строках записаны N целых чисел Ai. Последняя строка
содержит число X

5
1 2 3 4 5
6
-> 5

"""


def create_list(length):
    result = [i + 1 for i in range(length)]
    return result


def closest_finder(list1, number):
    bcounter = 0
    scounter = 0

    flag = True
    i = 0

    while flag:
        if list1[i] == number:
            break

        elif list1[i] < number and number - list1[i] < scounter:
            scounter = number - list1[i]

        elif list1[i] > number and list1[i] - number < bcounter:
            bcounter = list1[i] - number

        i += 1

    if bcounter < scounter:
        print(f'The nearest number is >> {number+ bcounter}')
    else:
        print(f'The nearest number is >> {number - scounter}')


list1 = create_list(30)
print(list1)

closest_finder(list1, 15)