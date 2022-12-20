# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# *Пример:*

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

from random import uniform

def difference_remainder(list_x:list):
    min = list_x[0] % 1
    max = min
    for i in list_x:
        i %= 1
        if i < min:
            min = i
        else:
            if i > max:
                max = i
    return max - min


if __name__ == '__main__':
    list_x = [uniform(1, 11) for i in range(10)]
    list_check = [i % 1 for i in list_x]
    min = min(list_check)
    max = max(list_check)
    result = difference_remainder(list_x)
    print(f'{list_x} => {result: .2f}')
    print(max - min == result)
    