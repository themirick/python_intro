"""
По данному целому неотрицательному n вычислите значение n!.
N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N) 0! = 1
Решить задачу используя цикл while


Input:       5

Output:    120


"""


def factorial(limiter):
    if limiter == 0:
        return 1
    else:
        counter = 1
        result = 1
        while counter <= limiter:
            result *= counter
            counter += 1
        return result


number = 3
n = factorial(number)
print(f"Факториал от числа {number} >> {n}")
