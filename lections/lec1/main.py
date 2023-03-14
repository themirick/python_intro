# n = None

# print(n)


# n = 'string'
# n1 = "string1"

# print (n)
# print(n1)


# n = 5
# n1 = 'fdjhf'
# n2 = 'dfj\'dkjf'
# n3 = 'dfj "dfjdk" dkjf'

# print (n3)
# print (type(n))
# print (type(n1))
# print (type(n2))


# print(1)
# print(2)
# print(3)

# print(4)
"""
print(5)
print(5)
print(5)
"""

# print(5)
# print(5)
# print(5)


# a = 5
# b = 5.56
# c = 'themirick'

# print(a, b, c)

# print(a, " - ", b, " - ", c)

# print(f"{a} - {b} - {c}")

# print("{} - {} - {}".format(a, b, c))


# print("input the first number")
# a = input()

# b - input("Input the second number>> ")


# print(a + b)

# c = 5.5
# print(type(c))

# n = int(c)
# print(n)
# print(type(n))

# c = int(c)
# print(type(c))

# c = str(c)
# print(c)
# print(type(c))

# c = 1
# print(c)
# print(type(c))

# n = c
# n = bool(c)
# print(n)
# print(type(n))

# v = "string"
# v = int(v) нельзя


# a = int(input("Input the first number>> "))
# b = int(input("Input the second number>> "))

# print("{} + {} = {}".format(a, b, a + b))


# a = 5.65465
# b = 10.546465

# print(a * b)

# print(round(a * b, 3))

# a = 1 > 4
# print(a)

# a = 1 < 4 and 5 > 2
# print(a)

# a = 1 == 2
# print(a)

# a = 1 != 2
# print(a)

# a = "str"
# b = "str"
# print(a == b)

# a = 1 < 3 < 5 < 10
# print(a)

# username = input("Input your username>> ")

# if username == "themirick":
#     print("themirick is top")
# elif username == "Max":
#     print("hi Max")
# else:
#     print("Hello {}".format(username))

# n = 423
# sum = 0

# while n > 0:
#     sum += n % 10
#     n //= 10

# print(sum)

# i = 0

# while i < 5:
#     if i == 3:
#         break     # лучше обходиться без него, это не приветсвуется, в ООП нет такого понятия
#     i += 1
# else:             #срабатывает только если while завершился самопроизвольно то есть без break
#     print("It's enough)")

# print(i)

# n = int(input("input numbeer>> "))

# flag = True

# i = 2

# while flag:
#     if n % i == 0:
#         flag = False
#         print(i) # наименьший делитель числа (n)

#     elif i > n // 2:
#         flag = False
#     i += 1

# a = 'qwerty'

# print(a[0])

# for i in a:
#     print(i)

# line = ""

# for i in range(5):
#     line = ""
#     for j in range(5):
#         line += "*"
#     print(line)


# a = "fkjfkj KJFKJ kdjflksjf JFLj jkdjfKFJKJ jfkdjKJF"

# print(len(a))
# print("fk" in a)
# print(a.lower())
# print(a.upper())
# print(a.replace("fk", "AAAAAA"))


# text = 'съешь ещё этих мягких французских булок'
# print(text[0])                                       # c
# print(text[1])                                       # ъ
# print(text[len(text)-1])                             # к
# print(text[-5])                                      # б
# print(text[:])                                       # съешь ещё этих мягких французских булок
# print(text[:2])                                      # съ
# print(text[len(text)-2:])                            # ок
# print(text[2:9])                                     # ешь ещё
# print(text[6:-18])                                   # ещё этих мягких
# print(text[0:len(text):6])                           # сеикакл
# print(text[::6])                                     # сеикакл
# text = text[2:9] + text[-5] + text[:2]               # ...
