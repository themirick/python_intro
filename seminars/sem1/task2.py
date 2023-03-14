"""
Задача 2: Найдите сумму цифр трехзначного числа.
123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0)


"""


def sum_number_digits(number):
    result = 0
    while number > 0:
        result += number % 10
        number //= 10
    return result


number = int(input("Input nuber to sum it's digits>> "))
summ = sum_number_digits(number)
print(f"The sum of digits of {number} is {summ}")
