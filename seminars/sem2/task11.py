"""
Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является,
то есть выведите такое число n, что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.

Input:     5

Output:  6


"""


def find_in_fibonacci(number):
    first = 0
    second = 1
    fibonacci_number = 1
    counter = 2
    flag = True

    while flag:
        if fibonacci_number == number and fibonacci_number <= number:
            flag = False
            print(f"Your nuber is {counter}th in Fibonacci")
        elif fibonacci_number > number:
            flag = False
            print("There is no such a number in Fibonacci")

        fibonacci_number = first + second
        first = second
        second = fibonacci_number
        counter += 1

find_in_fibonacci(27)
