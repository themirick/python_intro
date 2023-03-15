"""
Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих
чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

4 4 -> 2 2
5 6 -> 2 3

"""
from math import sqrt, pow

"""
    a + b = numbers_sum => b = numbers_sum - a
    a * b = numbers_product => 
    -a*a + numbers_sum * a - numbers_product = 0
    получили квадратное уравнение

"""


def number_guesser(numbers_sum, numbers_product):

    dicriminant = pow(numbers_sum, 2) - 4 * 1 * numbers_product  # считаем дискриминант

    if dicriminant >= 0:    # если дискриминанат > 0 - два корня
        sq = sqrt(dicriminant) / 2
        p = numbers_sum / 2
        a = p + sq
        b = p - sq

    print(f"The first number is >> {a} and the second is >> {b}")


number_guesser(7, 12)
