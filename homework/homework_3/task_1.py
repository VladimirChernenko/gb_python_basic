# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint

def sum_list_index_not_even(list_x:list):
    sum_x = 0
    for i in range(1, len(list_x), 2):
        sum_x += list_x[i]
    return sum_x


if __name__ == '__main__':
    list_x = [randint(1, 11) for i in range(10)]
    print(list_x)
    print(sum_list_index_not_even(list_x))
    print(sum_list_index_not_even([2, 3, 5, 9, 3]))
    