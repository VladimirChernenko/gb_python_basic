# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# *Пример:*

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

from random import randint

def fib_minus(number:int):
    list_result = [1, 0]
    for i in range(number-1):
        list_result.insert(0, list_result[1] - list_result[0])
    return list_result


    
def fib(number:int):
    list_result = [0, 1]
    for i in range(2, number+1):
        list_result.append(list_result[i - 1] + list_result[i - 2])
    return list_result


if __name__ == '__main__':
    number = int(input('Entered integer number > 0: '))
    if number > 0:
        print(f'{number} => {fib_minus(number) + fib(number)[1:]}')
    else:
        print(f'You entered a wrong number: {number}')
    print(f'{8} => {fib_minus(8) + fib(8)[1:]}')