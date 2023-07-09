import os
import math
import random
import math

def task30():
    print("Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d. Каждое число вводится с новой строки.")

    amount_of_elements = int(input("Введите количество элементов прогрессии: "))
    first_element = int(input("Введите первый элемент прогрессии: "))
    difference = int(input("Введите разницу элементов прогресии: "))

    last_element = first_element + (amount_of_elements) * difference
    list_progression = [i for i in range(first_element, last_element, difference )]

    return list_progression

# print(*task30(), sep='\n')

# input("Введите любую клавишу что бы продолжить ")
# os.system("cls")

def task32():
    print("Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума). ")
    
    amount_of_alements = int(input("Введите количество элементов массива: "))

    list_my = [random.randint(0, 20) for i in range(amount_of_alements)]

    max_value = int(input("Введите максимальное значение: "))
    min_value = int(input("Введите минимальное значение: "))
    
    list_index = [i for i in range(len(list_my)) if max_value >= list_my[i] >= min_value]
    
    print(list_my)
    print(list_index)

task32()

input("Введите любую клавишу что бы продолжить ")
os.system("cls")