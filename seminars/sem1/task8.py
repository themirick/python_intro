"""
Задача 8: Требуется определить, можно ли от шоколадки размером n × m
долек отломить k долек, если разрешается сделать один разлом по прямой
между дольками (то есть разломить шоколадку на два прямоугольника).

3 2 4 -> yes
3 2 1 -> no

"""

width = 2
height = 3
bar = 0


def chocolate_slicer(width, height, bar):
    if (bar % width == 0 or bar % height == 0) and bar <= width * height and bar != width * height and bar != 0:
        print(f"{width}x{height} / {bar} >> Yes")

    else:
        print(f"{width}x{height} / {bar} >> No")


chocolate_slicer(width, height, bar)
