"""
Задача №29. Решение в группах

Ваня и Петя поспорили, кто быстрее решит
следующую задачу: “Задана последовательность
неотрицательных целых чисел. Требуется определить
значение наибольшего элемента
последовательности, которая завершается первым
встретившимся нулем (число 0 не входит в
последовательность)”. Однако 2  друга оказались не
такими смышлеными. Никто из ребят не смог до
конца сделать это задание. Они решили так: у кого
будет меньше ошибок в коде, тот и выиграл спор. За
помощью товарищи обратились к Вам, студентам.

Примечание: Программные коды на следующих
слайдах


"""

list1 = [1, 2, 3, 4, 5, 6, 7, 10, 10, 15, 0, 20, 30, 15, 31, 0]


def big_finder(list1: list):
    temp_list = [list1[i] for i in range(list1.index(0))]
    print(temp_list)
    return f'The biggest number is>> {max(temp_list)}'


print(big_finder(list1))
