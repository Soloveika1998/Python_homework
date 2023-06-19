import os
import math

def task10():
    print("Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть")
    
    number_of_coins = int(input("Введите количество монет: "))
    print("Укажите изначальное положение монет цифрами 0 (орел) или 1 (решка)")
    count_actions = 0

    for i in range(number_of_coins):
      coin_position = int (input())
      if coin_position == 1:
        count_actions += 1
    if count_actions >= number_of_coins/2:
      print(f"Наименьшее количество монет для поворота {number_of_coins - count_actions} ")
    else:
       print("Наименьшее количество монет - {}!".format(count_actions))
    

# task10()
# input("Введите любую клавишу что бы продолжить ")
# os.system("cls")

def task12():
  print("Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.")

  summ_numbers = int(input("Введите сумму чисел: "))
  product_numbers = int(input("Введите произведение чисел: "))
  discr = summ_numbers**2 - 4*product_numbers
  if discr < 0:
    print("Решений нет!")
  
  elif discr == 0:
    first_number = int(summ_numbers//2)
    print("Есть решение: первое и второе числа равны {}".format(first_number))
  
  elif discr >= 0:
    first_number = int((summ_numbers + math.sqrt(discr))//2)
    second_number = int((summ_numbers - math.sqrt(discr))//2)
    print("Есть решения: первое число {}, второе число {}.".format(first_number, second_number))

# task12()
# input("Введите любую клавишу что бы продолжить ")
# os.system("cls")

def task14():
  print("Задача 14: Требуется вывести все целые степени двойки")
  number = int(input("Укажите натуральное число: "))
  temp_number = 0
  
  while number >= 2**temp_number:
    print("{} - {}".format(temp_number, 2**temp_number))
    temp_number += 1

# task14()
# input("Введите любую клавишу что бы продолжить ")
# os.system("cls")


