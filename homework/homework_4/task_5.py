# 5 Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

import task_4
import os
from re import search
from random import randint


def sum_polynomial(list_1:list, list_2:list):
    pass

def file_in_list(name_file:str):
    if os.path.isfile(os.getcwd() + '\\' + name_file):
        with open(name_file, encoding='utf-8') as file : 
            return [search(r'(-*\d*)(.*)', i).groups() for i in (file.readline()).split()]
    print('file does not exists')
    return




if __name__ == '__main__':
    # task_4.create_or_add_file(task_4.func(randint(1, 10)), 'homework\\homework_4\\file_1.txt')
    # task_4.create_or_add_file(task_4.func(randint(1, 10)), 'homework\\homework_4\\file_2.txt')
    print(file_in_list('homework\\homework_4\\file_1.txt'))