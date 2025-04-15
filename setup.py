import random
import time
board = [
    [7,8,9],
    [4,5,6],
    [1,2,3],
]

def reset():
    global board
    board = [
    [7,8,9],
    [4,5,6],
    [1,2,3],
]

def starting_board(board):
    board = f'''\n            {board[0][0]} | {board[0][1]} | {board[0][2]}
            ----------
            {board[1][0]} | {board[1][1]} | {board[1][2]}
            ----------
            {board[2][0]} | {board[2][1]} | {board[2][2]}'''
    print(board)

def starting_rules():
    print('This is what the board will look like')
    print('''\n            7 | 8 | 9
            -----------
            4 | 5 | 6
            -----------
            1 | 2 | 3''')
    
    print('\nYou just have to input the position (1-9)')

def type_of_play():
    print('What game mode would you like to play?')
    print('0. Player vs. Computer ')
    print('1. Player vs. Player')
    print('2. Computer vs. Computer')
    flag = True
    while flag:
        try:
            user_input = int(input('Select an option (0-2): '))
            if user_input < 0 or user_input > 2:
                print('Please select a number between (0-2)')
            else:
                flag = False
        except ValueError:
            print('Please enter a valid input')     
        
    return user_input

def players_name(user_input):
    if user_input == 0:
        player_name = input("Please enter the players name who will take on the computer: ")
        computer_name = 'Computer'
        return player_name,computer_name
    elif user_input == 1:
        player1_name = input("Please enter player 1's name: ")  
        player2_name = input("Please enter player 2's name: ")
        return player1_name,player2_name
    else:
        computer_1 = 'Computer 1'
        computer_2 = 'Computer 2'
        return computer_1,computer_2

def player_position(player):
    starting_board(board)
    while True:
        try:
            user_input = int(input(f'{player}, choose your position '))
            if user_input > 9 or user_input < 1:
                print('Please enter a number from (1-9)')
            else:    
                return user_input
        except ValueError:
            print('Please enter a valid input')    
    
def player_sides(player1,user_input):
    while True:
        if user_input == 1 or user_input == 0:
            side = input(f"{player1}, what side would you like to be on? O's or X's: ").upper()
            if side != 'X' and side != 'O':
                print('please enter a valid input')
            else:
                if side.upper() == 'O':
                    first = 'O'
                    second = 'X'
                    return first,second
                else:
                    first = 'X'
                    second = 'O'
                    return first,second 
        else:    
            first = 'X'
            second = 'O'
            return first,second        

def change_board(player_pos,player_side,player): 
    flag = True
    while flag:
        if player_pos in board[2] and isinstance(board[2][board[2].index(player_pos)],int):
            index = board[2].index(player_pos)
            board[2][index] = player_side
            flag = False
        elif player_pos in board[1] and isinstance(board[1][board[1].index(player_pos)],int):
            index = board[1].index(player_pos)
            board[1][index] = player_side
            flag = False
        elif player_pos in board[0] and isinstance(board[0][board[0].index(player_pos)],int):
            index = board[0].index(player_pos)
            board[0][index] = player_side 
            flag = False   
        else:
            print(f'{player_pos} already taken')   
            player_pos = player_position(player)
    starting_board(board)     

def check_draw():
    lst = []
    for b in board:
        for i in b:
            if type(i) == str:
                lst.append(i)
            else:
                break
                
    if len(lst) == 9:
        print('Thats a draw!!!')
        return True
          
def win_condition(player,player_side):
    if len(set(board[0])) == 1:
        print(f'{player} wins!!!!')
        return True
    elif len(set(board[1])) == 1:
        print(f'{player} wins!!!!')
        return True
    elif len(set(board[2])) == 1:
        print(f'{player} wins!!!!')
        return True
    elif (board[0][0], board[1][1], board[2][2]) == (player_side,player_side,player_side):
        print(f'{player} wins!!!!')
        return True
    elif (board[0][2],board[1][1],board[2][0]) == (player_side,player_side,player_side):
        print(f'{player} wins!!!!')
        return True
    elif (board[0][0],board[1][0],board[2][0]) == (player_side,player_side,player_side):
        print(f'{player} wins!!!!')
        return True
    elif (board[0][2],board[1][2],board[2][2]) == (player_side,player_side,player_side):
        print(f'{player} wins!!!!')
        return True
    elif (board[0][1],board[1][1],board[2][1]) == (player_side,player_side,player_side):
        print(f'{player} wins!!!!')
        return True
    if check_draw():
        return True
# Easy Mode
def computer_inputs(computer_side,comp_name):
    # easy mode
    flag = True
    while flag:
        rand_pos_board = random.choice(board)
        rand_pos = random.choice(rand_pos_board)
        if type(rand_pos) == int:
            flag = False 
    change_board(rand_pos,computer_side,comp_name)  
# Medium Mode
def computer_medium(computer_side,player_side,comp_name):
    winning_lines = [
    # Horizontal rows
    [(0, 0), (0, 1), (0, 2)],
    [(1, 0), (1, 1), (1, 2)],
    [(2, 0), (2, 1), (2, 2)],

    # Vertical columns
    [(0, 0), (1, 0), (2, 0)],
    [(0, 1), (1, 1), (2, 1)],
    [(0, 2), (1, 2), (2, 2)],

    # Diagonals
    [(0, 0), (1, 1), (2, 2)],
    [(0, 2), (1, 1), (2, 0)]
]
    found = False
    for row in winning_lines:
        count = 0
        temp = 0
        for f_index,s_index in row:
            if board[f_index][s_index] == player_side:
                count += 1
            else:
                if board[f_index][s_index] == computer_side:
                    count = 0
                if board[f_index][s_index] != 'O':    
                    num = board[f_index][s_index] 
            temp += 1       
            if count == 2 and temp == 3:
                found = True
                change_board(num,computer_side,comp_name)
                break
        if found is True:
            break    
    if  found is False:
        computer_inputs(computer_side,comp_name)   
