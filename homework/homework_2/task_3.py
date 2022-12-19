# 3 Задайте список из n чисел последовательности (1 + (1 / n)) ** n и выведите на экран их сумму.
# Решил задачу выше так как не понял данную формулу == $(1+\frac 1 n)^n$.
# на семинаре нам сказали что правильная задача ==  Задайте список из n чисел последовательности (1 + (1 / n)) ** n и выведите на экран их сумму.


def func_list(number:int):
    return [round((1 + (1 / i)) ** i, 2) for i in range(1, number + 1)]

def func_dict(number:int):
    return {i: round((1 + (1 / i)) ** i, 2) for i in range(1, number + 1)}


if __name__ == '__main__':
    number = int(input('Enter number: '))
    list_result = func_list(number)
    print(list_result)
    print(round(sum(list_result)))
    # dict_result = func_dict(number)
    # print(dict_result)
    