import os
import math
import random
import math


def сounting_vowels_in_phrases(poem):
    list_vomel = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
    phrase = poem.replace('-', '').split()
    count_vomel_list = list()

    for i in range(len(phrase)):
        count_vomel_list.append(sum(map(lambda x : 1 if x in list_vomel else 0, phrase[i])))
    
    return count_vomel_list


def task34():
    print("Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке")


    vini_poem = input("Введите стихотворение: ")
    if len(set(сounting_vowels_in_phrases(vini_poem))) < 2:
        print("Парам пам-пам")
    else:
        print("Пам парам")


# task34()
# input("Введите любую клавишу что бы продолжить ")
# os.system("cls")


def print_operation_table(operation, num_rows=6, num_columns=6):
    res_list = [[operation(i, j) for i in range(1, num_rows)] for j in range(1, num_columns)]
    for i in res_list:
        print(*[f"{x:5}" for x in i])

print_operation_table(lambda x, y: x * y)

def task36():
    print("Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.")