# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

def quarter(x, y):
    if x == 0 or y == 0:   
        return 0    
    if x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    return 4


if __name__ == '__main__':
    x = int(input('enter coordinates x: '))
    y = int(input('enter coordinates y: '))
    answer_quarter = quarter(x, y)
    if answer_quarter:
        print(answer_quarter)
    else:
        print(f'Error!!!\nx ≠ 0 and y ≠ 0\nx = {x}; y = {y}')