"""
Задача 16: Требуется вычислить, сколько раз встречается некоторое
число X в массиве A[1..N]. Пользователь в первой строке вводит
натуральное число N – количество элементов в массиве. В последующих
строках записаны N целых чисел Ai. Последняя строка содержит число X

5
1 2 3 4 5
3
-> 1

"""


def create_list(length):
    result = []
    for i in range(length):
        result.append(i+1)
    return result


def list_digit_counter(list1, digit):
    list1 = ''.join(map(str, list1))
    digit = str(digit)
    counter = 0
    for i in list1:
        if i == digit:
            counter += 1
    print(f"Digit >{digit}< comes >> {counter} times in the given list")


list1 = create_list(30)
print(list1)

list_digit_counter(list1, 2)
