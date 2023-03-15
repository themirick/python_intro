"""
Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя,
а другой для тещи. Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче.
Но вот незадача: арбузов слишком много и он не знает как же выбрать самый легкий и самый
тяжелый арбуз? Помогите ему!

Пользователь вводит одно число N – количество арбузов. Вторая строка содержит N чисел,
записанных на новой строчке каждое. Здесь каждое число – это масса соответствующего арбуза

Input:	5 -> 5 1 6 5 9
Output:	1 9


"""

from random import randint


def fruit_weighter(fruits):
    the_biggest = fruits[0]
    the_smallest = fruits[0]

    for melon in fruits:
        if melon > the_biggest:
            the_biggest = melon
        elif melon < the_smallest:
            the_smallest = melon

    print(f"The biggest melon is >> {the_biggest}\n"
          f"The smallest is >> {the_smallest}")


fruits = [randint(1, 20) for melon in range(10)]

print(fruits, "\n")

fruit_weighter(fruits)
