"""
Задача №35. Решение в группах

Напишите функцию, которая принимает одно число и
проверяет, является ли оно простым

Напоминание: Простое число - это число, которое
имеет 2 делителя: 1  и n(само число)

Input: 5
Output: yes


"""


def is_prime(number, i=2):
    if number <= 1:
        return 'input more than 1'
    elif i >= number / 2:
        return 'number is prime'
    elif number % i == 0:
        return 'number is not prime'

    return is_prime(number, i + 1)


print(is_prime(50))
