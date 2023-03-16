"""
Задача №19. Решение в группах

Дана последовательность из N целых чисел и число
K. Необходимо сдвинуть всю последовательность
(сдвиг - циклический) на K элементов вправо,  K –
положительное число.

Input:   [1, 2, 3, 4, 5] k = 3

Output:  [4, 5, 1, 2, 3]

Примечание: Пользователь может вводить значения
списка или список задан изначально.


"""

l = [1, 2, 3, 4, 5]
k = 3


def list_shift(list, shift_step):
    result = []
    ln = len(list)
    for i in range(ln):
        if i + 3 < len(list):
            result.append(list[i+3])
        else:
            result.append(list[i + 3 - ln])
    print(result)


list_shift(l, k)
