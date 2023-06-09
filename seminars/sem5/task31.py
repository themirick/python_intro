"""
Задача №31. Решение в группах

Последовательностью Фибоначчи называется
последовательность чисел a0, a1, ..., an, ..., где
a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
Требуется найти N-е число Фибоначчи
Input: 7
Output: 21

Задание необходимо решать через рекурсию


"""

# 1 1 2 3 5 8 13


def fibonaci(limit: int):

    if limit in (1, 2):
        return 1
    return fibonaci(limit - 1) + fibonaci(limit - 2)


print(fibonaci(7))
