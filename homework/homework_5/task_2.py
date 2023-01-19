# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом""


from random import randint

def who_in_game(num:int):
    if num == 3:
        return bot_hard
    elif num == 2:
        return bot_easy
    return player

def validate_num_game(num):
    if 0 < num < 4: return True
    print(f'There is no game with this number.\nYour entered: {num}')

def player(count_candy, turn=28):
    return int(input(f'Candy left: {count_candy}. Enter number 1-{turn}: '))

def bot_easy(count_candy, turn=28):
    return randint(1, turn) if count_candy > turn else count_candy

def bot_hard(count_candy, turn=28):
    x = count_candy % (turn + 1) 
    return x if x else 1

def game(player_2, count_candy=2021, turn =28, player_1=player):
    game_list = [(player_1, 'Player_1'), (player_2, 'Player_2')] if randint(0, 1) else [(player_2, 'Player_2'), (player_1, 'Player_1')]
    print(f'{game_list[0][1]} turn first')
    while count_candy > 0:
        for f, n in game_list:
            print(f'Now {n} turn')
            x = f(count_candy, turn)
            x = x if x < 29 else 28
            count_candy -= x 
            print(f'{n} take {x} candies, candy left: {count_candy}')
            if count_candy == 0:  
                print(f'Win {n}')
                break
    print('The end.')



if __name__ == '__main__':
    game_x = int(input('Start game.\n(1 == game with player, 2 == game with easy bot, 3 == game with hard bot).\nEnter number of game: '))
    if validate_num_game(game_x):
        game(who_in_game(game_x))
