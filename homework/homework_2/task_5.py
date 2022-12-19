# 5 Реализуйте алгоритм перемешивания списка.
from random import randint


def blender(list_x):
    len_x = len(list_x)
    for i in range(len_x):
        x = randint(0, len_x-1)
        list_x[i], list_x[x] = list_x[x], list_x[i]


if __name__ == '__main__':
    list_x = [randint(1, 101) for i in range(10)]
    print(list_x)
    blender(list_x)
    print(list_x)