import os
import math
import random
import math

def task22():
    print("Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах. Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.")

    amount_of_alements_first_list = int(input("Введите количество элементов в первом массиве: "))
    amount_of_alements_second_list = int(input("Введите количество элементов во втором массиве: "))

    list_first = list()
    for i in range(amount_of_alements_first_list):
       list_first.append(input("Введите элементы первого множества: "))
    print(*list_first)

    list_second = list()
    for i in range(amount_of_alements_second_list):
       list_second.append(input("Введите элементы второго множества: "))
    print(*list_second)

    unique_set = sorted(set(list_first).intersection(set(list_second)))
    print(unique_set)

# task22()
# input("Введите любую клавишу что бы продолжить ")
# os.system("cls")

def task24():
    print("Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, причём кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.")

    number_of_bushes = int(input("Введите количество кустов >= 3 штук: "))
    yield_list = list()
    for i in range(number_of_bushes):
       yield_list.append(int(input("Введите урожайность {} куста: ".format(i+1))))
    max_summ_yield = 0
    for i in range(number_of_bushes):
        summ_yield = sum([yield_list[i] + yield_list[i - 1] + yield_list[(i + 1) % number_of_bushes]])
        if summ_yield > max_summ_yield:
            max_summ_yield = summ_yield
            first = i
            second = i+1
            three = (i + 2) % (number_of_bushes + 1)
    print("Максимальное количество ягод за один проход будет собрано с кустов № {}, № {} и № {} в количестве {} ягод ".format(first, second, three, max_summ_yield))

task24()
input("Введите любую клавишу что бы продолжить ")
os.system("cls")