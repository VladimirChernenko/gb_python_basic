# Создайте программу для игры в ""Крестики-нолики"".

def matrix(x:int):
    return [[i_x + x*i_y for i_x in range(1, x+1)] for i_y in range(x)]

def print_matrix(matrix_x:list):
        for i in matrix_x:
            for el in i:
                print(el, end=' ')
            print()

def game_x(matrix_x):
    tuple_char = 'x', '0'
    for count in range(1, 6):
        for char in tuple_char:
            print_matrix(matrix_x)
            x = int(input(f'Now {char} turn.\nEnter cell number : '))
            len_matrix = len(matrix_x)
            for num_str in range(len_matrix):
                for num_column in range(len_matrix):
                    position = matrix_x[num_str][num_column]
                    if matrix_x[num_str][num_column] == x: 
                        matrix_x[num_str][num_column] = char
                        if count > 2:
                            if (matrix_x[num_str][0] == matrix_x[num_str][1] == matrix_x[num_str][1]) or (matrix_x[0][num_column] == matrix_x[1][num_column] == matrix_x[2][num_column]) or (not position%2 and ((matrix_x[0][0] == matrix_x[1][1] == matrix_x[2][2]) or (matrix_x[0][2] == matrix_x[1][1] == matrix_x[2][0]))):
                                print(f'Win {char}!')
                                return
            
    print_matrix(matrix_x)
    


            

if __name__ =='__main__':
    matrix_x = matrix(3)
    game_x(matrix_x)