#  Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# *Пример:*

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

from random import randint

def binary_number(number:int):
    str_binary_number = ''
    while number > 0:
        str_binary_number += str(number % 2)
        number //= 2
    return (str_binary_number)[::-1]


if __name__ == '__main__':
    number = randint(1, 101)
    print(f'{number} => {binary_number(number)} => {bin(number)}')
    