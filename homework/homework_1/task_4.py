# 4 Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

def coordinate_range(quarter, range_x=10):
    return {1: f'x(0, {range_x}] y(0, {range_x}]', 2: f'x[-{range_x}, 0) y(0, {range_x}]', 3: f'x[-{range_x}, 0) y[-{range_x}, 0)', 4: f'x(0, {range_x}] y[-{range_x}, 0)'}[quarter]

if __name__ == '__main__':
    quarter = int(input('enter quarter 1-4: '))
    if 0 < quarter < 5:
        print(coordinate_range(quarter))
    else:
        print(f'Quarter {quarter} does not exist!')       