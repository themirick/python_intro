"""
Напишите программу, которая принимает на вход две строки и определяет,
являются ли они анаграммами. Знаки препинания, пробелы и регистр при этом игнорируются.


"""


str1 = 'урок'
str2 = 'укор'


def anagram_detector(str1, str2):
    str1 = {i for i in str1}
    str2 = {i for i in str2}

    if str1 == str1.intersection(str2):
        print(f"Слова являются анаграммами")
    else:
        print("Слова не являются анаграммами")


anagram_detector(str1, str2)
