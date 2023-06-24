import os
import math
import random
import math

def task16():
    print("Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X")
    amount_of_alements = int(input())
    my_list = list()
    
    for i in range(amount_of_alements):
       my_list.append(random.randint(1, amount_of_alements))
    print(*my_list)

    x = int(input())
    count = 0
    for item in my_list:
        if item == x:
            count += 1
    print(count)

# task16()
# input("Введите любую клавишу что бы продолжить ")
# os.system("cls")

def task18():
    print("Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X    ")
    amount_of_alements = int(input())
    my_list = list()
    
    for i in range(amount_of_alements):
       my_list.append(random.randint(1, amount_of_alements))
    print(*my_list)

    x = int(input())
    difference = 10**10
    for item in my_list:
        if item != x:
            if difference > (abs(x-item)):
                number = item
                difference = abs(x-item)
    print(number)

# task18()
# input("Введите любую клавишу что бы продолжить ")
# os.system("cls")

def task20():
    print("*Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. В случае с английским алфавитом очки распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко; D, G – 2 очка; B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; Q, Z – 10 очков. А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; Д, К, Л, М, П, У – 2 очка; Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков. Напишите программу, которая вычисляет стоимость введенного пользователем слова. Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.")
    
    scrabble_data_eng = { 1: 'AEIOULNSTR',
                        2: 'DG',
                        3: 'BCMP',
                        4: 'FHVWY',
                        5: 'K',
                        8: 'JX',
                        10: 'QZ'}
    scrabble_data_ru = {1: 'АВЕИНОРСТ',
                        2: 'ДКЛМПУ',
                        3: 'БГЁЬЯ',
                        4: 'ЙЫ',
                        5: 'ЖЗХЦЧ',
                        8: 'ШЭЮ',
                        10: 'ФЩЪ'}
    index_language = int (input('Введите 1, если вы будете ввдить слово на английском языке, введите 0, если на русском! '))
    word = input('Введите слово: ').upper()
    if index_language == 1:
        print('За это слово вы получаете', sum([key for one_char in word for key, values in scrabble_data_eng.items() if one_char in values ]), 'очков')
    elif index_language == 0:
        print('За это слово вы получаете', sum([key for one_char in word for key, values in scrabble_data_ru.items() if one_char in values ]), 'очков')
    else:
        print("Попробуйте еще раз!")
# task20()
# input("Введите любую клавишу что бы продолжить ")
# os.system("cls")