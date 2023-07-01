import os
import math
import random
import math

def rec_exponentiation(a, b):
    if b == 1:
        return a
    return a * rec_exponentiation(a, b-1)

def task26():
    print("Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.")
    number_a = int(input("Введите число А: "))
    number_b = int(input("Введите число B - степень числа А: "))
    print(rec_exponentiation(number_a, number_b))

# task26()
# input("Введите любую клавишу что бы продолжить ")
# os.system("cls")

def rec_sum(a, b):
    return rec_sum(a+1, b-1) if b > 0 else rec_sum(a-1, b+1) if b < 0 else a

def task28():
    print("Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.")
    number_a = int(input("Введите число А: "))
    number_b = int(input("Введите число B: "))
    print(rec_sum(number_a, number_b))

task28()
input("Введите любую клавишу что бы продолжить ")
os.system("cls")

