"""
Напишите программу, которая принимает на вход две строки и определяет,
являются ли они анаграммами. Знаки препинания, пробелы и регистр при этом игнорируются.


"""


str1 = 'урок'
str2 = 'УК ОР'


def anagram_detector(str1, str2):
    str1 = {i for i in str1.lower().replace(' ', '')}
    str2 = {i for i in str2.lower().replace(' ', '')}

    if str1 == str1.intersection(str2):
        print(f"Слова являются анаграммами")
    else:
        print("Слова не являются анаграммами")


anagram_detector(str1, str2)
