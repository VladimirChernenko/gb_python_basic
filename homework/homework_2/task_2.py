# 2 Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# *Пример:*

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
def multi_list(list_x:list):
    result = 1
    for i in list_x:
        result *= i
    return result


def factorial_step(number_factorial:int):
    return [i*multi_list([j for j in range(1, i)]) for i in range(1, number_factorial+1)]


if __name__ == '__main__':
    number = int(input('Enter number'))
    print(factorial_step(number))