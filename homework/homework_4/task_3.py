# 3 Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.


if __name__ == '__main__':
    str_number = input('Enter numbers separated by spaces: ')
    set_number = set(str_number.split())
    print(set_number)