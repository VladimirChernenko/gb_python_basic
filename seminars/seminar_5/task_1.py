# 35. В файле находится N натуральных чисел, записанных через пробел. Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.

import os
from random import randint


def create_file(name_file: str):
    with open(name_file, 'w', encoding='utf-8') as f:
        list_x = [i for i in range(100)]
        x = list_x.pop(randint(0, 100))
        f.write(' '.join(map(str, list_x)))
        return x

def write_file_list(name_file: str):
    if os.path.isfile(name_file):
        with open(name_file, encoding='utf-8') as file: 
            list_x = list(map(int, (file.read()).split()))
            return list_x
    return 'file does not exists'  

def func(list_x:list):
    list_x.sort()
    for i in range(1, len(list_x)):
        if list_x[i] - 1 != list_x[i - 1]:    return list_x[i] - 1

if __name__ == '__main__':
    x = create_file('seminars\\seminar_5\\task_1.txt')
    list_x = write_file_list('seminars\\seminar_5\\task_1.txt')
    y = func(list_x)
    print(x == y)
    

