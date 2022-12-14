# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# Пример:

#     - 6 -> да
#     - 7 -> да
#     - 1 -> нет

if __name__ == '__main__':
    day_number = int(input('Enter the number of the day of the week(1 - 7): '))

    if 0 < day_number < 6:
        print('No!')
    elif day_number == 6 or day_number == 7:
        print('Yes!')
    else:
        print('There is no such day of the week!')
