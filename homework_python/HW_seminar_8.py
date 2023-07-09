import os
import math

def read_file(filename):
    with open(filename, 'r', encoding = 'UTF-8') as data:
        data_str = data.read()
        if len(data_str) == 0:
            print("Список контактов пуст!")
            print()
        else:
            print("В списке содержится: ")
            print(data_str)

def write_file(filename):
    input_fio = input("Введите Фамилию Имя и Отчество: ")
    input_tel = input("Введите телефон: ")
    find_word = f"{input_fio} | {input_tel}\n"
    with open(filename, 'r+', encoding = 'UTF-8') as file:
        find_list = [line for line in file if find_word in line]
        if len(find_list) != 0:
            print("Такой контакт уже существует!")
            return 0
        else:
            file.write(f"{input_fio} | {input_tel}\n")
            print(f"Добавлен контакт {input_fio} | {input_tel}\n")

def find_file(filename):
    find_word = input("Введите телефон или ФИО для поиска: ")
    print()
    with open(filename, encoding='utf-8') as file:
        find_list = [line for line in file if find_word in line]
    return find_list

def search_processing(find_list):
    if len(find_list) == 0:
        print("Контакты с такими данными не найдены")
        print()
    else:
        print("Найдены следующие контакты: ")
        for i in range(len(find_list)):
            print(f"{i + 1}. {find_list[i]}", end = '')
        print('')

def replace_list(filename, change_find_list, selection_change = 0):
    with open (filename, 'r', encoding = 'UTF-8') as file:
        old_data = file.read()
        new_input_fio = input("Введите новое Фамилию Имя и Отчество: ")
        new_input_tel = input("Введите новый телефон: ")
        new_data = old_data.replace(change_find_list[selection_change],  new_input_fio + ' | ' + new_input_tel + '\n')

    with open ('tell_list.txt', 'w', encoding = 'UTF-8') as file:
        file.write(new_data)

def change_file(filename):
    change_find_list = find_file(filename)
    search_processing(change_find_list)
    if len(change_find_list) == 0:
        return 0
    elif len(change_find_list) > 1:
        selection_change = int(input("Введите порядковый номер контакта, который нужно изменить: "))
        replace_list(filename, change_find_list, selection_change - 1)
        print()
    else:
        replace_list(filename, change_find_list)
        print()

def delete_data(filename):
    with open(filename, 'r', encoding = 'UTF-8') as file:
        list_tel = [line for line in file]
        if len(list_tel) == 0:
            print("Список контактов пуст!")
            print()
            return 0
        else:
            for i in range(len(list_tel)):
                print(f"{i + 1}. {list_tel[i]}", end = '')
            print('')

        index_delete_data = int(input('Введите номер строки для удаления: ')) - 1
        if len(list_tel) > index_delete_data >= 0:
            delet_elem = list_tel.pop(index_delete_data)
            print(f"Удален контакт: {delet_elem}")
            with open(filename, 'w', encoding = 'UTF-8') as data:
                for item in list_tel:
                    data.write("%s" % item)
        else:
            print("Вы ввели номер несуществующей строки, попробуйте еще раз!")
            print()
            return 0

def menu():
    file_tel = "tell_list.txt"
    with open(file_tel, 'a', encoding = 'UTF-8') as file:
        file.write('')
        
    while True:
        print("Выберите действие: ")
        print("1 - вывести информацию на экран")
        print("2 - добавить данные в справочник")
        print("3 - для поиска файлов по фамилии или телефону")
        print("4 - для изменения контакта")
        print("5 - для удаления контакта")
        print("0 - выход из программы")
        number_options = int(input("Ваш выбор: "))
        if number_options == 0:
            os.system("cls")
            break

        elif number_options == 1:
            read_file('tell_list.txt')


        elif number_options == 2:
            os.system("cls")
            write_file('tell_list.txt')

        elif number_options == 3:
            os.system("cls")
            find_list = find_file('tell_list.txt')
            search_processing(find_list)

        elif number_options == 4:
            os.system("cls")
            change_file('tell_list.txt')

        elif number_options == 5:
            os.system("cls")
            delete_data('tell_list.txt')

        else:
            print("Введите корректное число: ")
            menu()


if __name__ == '__main__':
    menu()