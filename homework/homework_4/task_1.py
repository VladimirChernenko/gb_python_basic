# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
from math import pi

def func_count(d:float):
    count = 0
    while d < 1:
        d *= 10
        count += 1
    return count if count <= 10 else 10
    

if __name__ == '__main__':
    print(pi)
    print(round(pi, func_count(0.000000000000000001)))
    print(round(pi, func_count(0.001)))