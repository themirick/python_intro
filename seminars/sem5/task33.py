"""
Задача №33. Решение в группах

Хакер Василий получил доступ к классному журналу и
хочет заменить все свои минимальные оценки на
максимальные. Напишите программу, которая
заменяет оценки Василия, но наоборот: все
максимальные – на минимальные.

Input: 5 -> 1 3 3 3 4

Output: 1 3 3 3 1


"""

marks = [1, 3, 3, 1, 3, 4]


def marks_remaker(marks_list: list):



    # marks_list = [min(marks_list) if marks_list[i] is max(marks_list) else marks_list[i] for i in range(len(marks_list))]

    # for i in marks_list:
    #     if i == max(marks_list):
    #         marks_list[i] = min(marks_list)


    # index = marks_list.index(max(marks_list))
    # marks_list[index] = min(marks_list)

    print(marks_list)


marks_remaker(marks)
