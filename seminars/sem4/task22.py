"""
Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
повторениями). Выдать без повторений в порядке возрастания все те числа, которые
встречаются в обоих наборах.

Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
элементов второго множества. Затем пользователь вводит сами элементы множеств.

11 6
2 4 6 8 10 12 10 8 6 4 2
3 6 9 12 15 18

6 12


"""

# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества.

# Затем пользователь вводит сами элементы множеств.


def sort_set(m_length: int, n_length: int):
    set1 = {int(input(f'Input {i + 1}th element of first list>> ')) for i in range(m_length)}
    set2 = {int(input(f'Input {i + 1}th element of second list>> ')) for i in range(n_length)}

    set1 = list(set1.intersection(set2))
    set1.sort()

    return set1


print(sort_set(5, 4))
