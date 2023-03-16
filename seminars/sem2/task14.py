"""
Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

10 -> 1 2 4 8
"""


def two_degree_counter(number):
    result = [1]

    for i in range(2, number):
        flag = True
        temp = i

        while flag:
            if i <= 0:
                flag = False
            elif i == 2:
                flag = False
            elif i % 2 == 0:
                i //= 2
                continue
            else:
                flag = False

        if i == 0 or i == 2:
            result.append(temp)

    print(f"{number} >>> {result}")


two_degree_counter(500)


# def two_degree_counter(number):
#     i = 0
#     while 2 ** i < number:
#         print(2 ** i)
#         i += 1