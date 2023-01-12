# 1. Дан список чисел. Создайте список, в который попадают числа, описываемые возрастающую последовательность. Порядок элементов менять нельзя.
    
#     *Пример:* 
    
#     [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.
    
from random import randint

def func(list_x: list):
    x = list_x[0]
    list_y = [x]
    for i in range(1, len(list_x)):    
        if list_x[i] > x:
            x = list_x[i]
            list_y.append(x)
    return list_y

if __name__ == '__main__':
    list_x = [randint(0, 100) for i in range(10)]
    print(list_x, func(list_x))

