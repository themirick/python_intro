"""
У вас есть массив чисел, составьте из них максимальное число.

Например:[61, 228, 9] -> 961228

"""


def largest_number(numbers):
    array = [[i for i in str(n)] for n in numbers]

    for i in range(len(array)-1):
        for j in range(len(array)-1):

            if array[j][0] > array[j+1][0]:
                continue
            elif array[j][0] == array[j+1][0]:
                continue
            else:
                temp = array[j+1]
                array[j + 1] = array[j]
                array[j] = temp

    # print(array)
    for i in range(len(array)):
        array[i] = "".join(array[i])
    # print(array)

    result = "".join(array)
    print(f"The largest available number from list-{array} is >> {result}")


numbers = [15, 93, 3]
largest_number(numbers)
