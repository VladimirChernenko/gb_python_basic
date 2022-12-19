# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11

def sum_digit_number(string_number:str):
    result = 0
    for i in string_number:
        if i.isdigit():
            result += int(i)
    return result


if __name__ == '__main__':
    print(sum_digit_number(input('Enter number: ')))