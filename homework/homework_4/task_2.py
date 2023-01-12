# 2 Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def func(number:int):
    list_x = []
    for i in range(2, 10):
        if not number % i:
            list_x.append(i)
            number /= i 
    return list_x


if __name__ == '__main__':
    m = int(input('Enter integer number: '))
    print(f'List of multiples of {m}: {func(m)}')