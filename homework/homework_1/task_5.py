# 5 Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# *Пример:*

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

def create_tuple_coordinate():
    x = int(input('enter coordinate x: '))
    y = int(input('enter coordinate y: '))
    return x, y

def distance_x_y(list_1, list_2):  
    return ((list_1[0] - list_2[0])**2 + (list_1[1] - list_2[1])**2)**0.5


if __name__ == '__main__':
    list_1 = create_tuple_coordinate()
    list_2 = create_tuple_coordinate()
    print(f'Distance between {list_1} and {list_2}: {round(distance_x_y(list_1, list_2), 2)}')
