# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# *Пример:*

# - [2, 3, 4, 5, 6] => [12, 15, 16]; Судя из примера если число элементов не четное то 
# - [2, 3, 5, 6] => [12, 15]

from random import randint

def multi_list(list_x:list):
    len_x = len(list_x)
    x = len_x + 1 if len_x % 2 else len_x
    return [list_x[i]*list_x[len_x - (i + 1)] for i in range(x//2)]


if __name__ == '__main__':
    list_x = [randint(1, 11) for i in range(randint(1, 11))]

    print(f'{list_x} => {multi_list(list_x)}')
    print(multi_list([2, 3, 4, 5, 6]))
    print(multi_list([2, 3, 5, 6]))
