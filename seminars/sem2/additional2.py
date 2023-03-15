"""
Составьте программу, которая вычисляет сумму квадратов
чисел от 1 до введенного вами целого числа N.

"""

start = 1
end = 100
summ = 0

while start <= end:
    summ += start * start
    start += 1

print(f"The summ of squred number from {start-end} to {end} is >> {summ}")
