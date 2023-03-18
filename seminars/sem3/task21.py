"""
Задача №21. Решение в группах

Напишите программу для печати всех уникальных
значений в словаре.

Input:  [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}
{"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
":" S007 "}]

Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

Примечание: Список словарей задан изначально
Пользователь его не вводит

"""

d = {"1": "S001", "2": "S002", "3": "S001", "4": "S005", "5": "S005", "6": "S009", "7": "S007"}


def unic_printer(dictionary):
    result = set()
    for item in dictionary:
        result.add(dictionary[item])

    print(result)


unic_printer(d)







# .strip()

# source = [
#     {"V": "S001"},
#     {"V": "S002"},
#     {"VI": "S001"},
#     {"VI": "S005"},
#     {"VII": "S005 "},
#     {"V": "S009"},
#     {"VIII": "S007"}
# ]
#
#
# def unic_printer(list_data):
#     result = set()
#     for item in list_data:
#         result.add(*item.values())
#     print(result)
#
#
# unic_printer(source)
