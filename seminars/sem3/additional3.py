"""
Напишите функцию, которая принимает словарь с параметрами и возвращает строку запроса,
сформированную из отсортированных в лексикографическом порядке параметров.

Пример:

Код print(query({'course': 'python', 'lesson': 2, 'challenge': 17})) должен возвращать строку:

challenge=17&course=python&lesson=2


"""

query = {'course': 'python', 'lesson': 2, 'challenge': 17}


def dict_converter(dictionary: dict):
    str1 = str()

    for item in dictionary:
        str1 += f'{item} - {dictionary[item]}, '

    print(str1)


dict_converter(query)
