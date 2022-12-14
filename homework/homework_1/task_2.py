# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
from random import randint

def check_true(n=1000):
    answer = 1
    for i in range(n):
        array_x = {randint(1, 1000000) for i in range(randint(1, 1000))}
        array_y = {randint(1, 1000000) for i in range(randint(1, 1000))}
        array_z = {randint(1, 1000000) for i in range(randint(1, 1000))}
        answer *= not (array_x | array_y | array_z) == (not array_x) & (not array_y) & (not array_z)
    return bool(answer)

if __name__ == '__main__':
    print(check_true())
