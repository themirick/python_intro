"""
Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали
одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем
Петя и Сережа вместе?

6 -> 1  4  1
24 -> 4  16  4
60 -> 10  40  10

"""
from math import ceil

cranes = int(input("Input amount of cranes>> "))

petya = cranes // 6
seryoja = petya
katya = petya * 4

# print(f"Petya done -   {petya} cranes"
#       f"Katya done -   {katya} cranes"
#       f"Seryoja done - {seryoja} cranes")

print(f"Petya done    - {petya} cranes \n"
      f"Katya done    - {katya} cranes \n"
      f"Seryoja done  - {seryoja} cranes")
