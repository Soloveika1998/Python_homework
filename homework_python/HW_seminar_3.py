import os
import math
import random

def task16():
    print("Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X")
    amount_of_alements = int(input())
    my_list = list()
    
    for i in range(amount_of_alements):
       my_list.append(random.randint(1, amount_of_alements))
    print(*my_list)

    x = int(input())
    count = 0
    for item in my_list:w
        if item == x:
            count+=1
    print(count)

task16()
input("Введите любую клавишу что бы продолжить ")
os.system("cls")