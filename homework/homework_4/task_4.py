# 4 Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# *Пример:* 

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
from random import randint
import os

def func(k:int):
    list_i = [randint(0, 100) for i in range(k+1)]
    if not list_i[0]:   list_i[0] = 1
    list_x = ['', 'x'] + [f'x**{i}' for i in range(2, k+1)]
    list_x.reverse()
    list_result = []
    for x, i in zip(list_x, list_i):
        if i == 1:
            list_result.append(f'{x}')
        elif i:
            list_result.append(f'{i}{x}')
    return list_result

def create_or_add_file(list_x:list, name_file:str):
    x = 'a' if os.path.isfile(os.getcwd() + '\\' + name_file) else 'w'
    with open(name_file, x, encoding='utf-8') as file:
        file.write(' + '.join(list_x) + '\n')


if __name__ == '__main__':
    create_or_add_file(func(randint(1, 10)), 'homework\\homework_4\\file_task_4_4.txt')
