"""
Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд
и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером,
где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый,
т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

385916 -> yes
123456 -> no

"""


ticket_number = int(input("Input the ticket number>> "))


def lucky_number_detector(ticket_number):
    limiter = 0
    sum1 = 0
    sum2 = 0

    while limiter <= 6:

        if limiter <= 6 / 2 - 1:
            sum2 += ticket_number % 10
        else:
            sum1 += ticket_number % 10

        limiter += 1
        ticket_number //= 10

    if sum1 == sum2:
        print(f"{ticket_number} >> yes")
    else:
        print(f"{ticket_number} >> no")


lucky_number_detector(ticket_number)
