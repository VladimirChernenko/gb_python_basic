# 4 Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

from random import randint

def create_list(len_list):
    return [randint(-len_list, len_list + 1) for i in range(len_list)]

def create_file(file_name:str, list_x:list):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in list_x:
            file.write(str(i) + '\n')

def multi_number(name_file:str, list_x:list):
    with open(name_file, encoding='utf-8') as file:
        list_i = [int(i) for i in file]
    result = 0
    if list_i:
        result = 1 
        for i in list_i:
            result *= list_x[i]
    return result

if __name__ == '__main__':
    number = int(input('Enter number: '))
    list_result = create_list(number)
    create_file('task_4.txt', [randint(0,number) for i in range(number//10)])
    print(multi_number('task_4.txt', list_result))    