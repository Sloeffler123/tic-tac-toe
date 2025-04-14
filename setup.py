import random
board = [
    [7,8,9],
    [4,5,6],
    [1,2,3],
]

def starting_board(board):
    board = f'''\n            {board[0][0]} | {board[0][1]} | {board[0][2]}
            -----------
            {board[1][0]} | {board[1][1]} | {board[1][2]}
            -----------
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
    try:
        user_input = int(input('Select an option (0-2): '))
        if user_input < 0 or user_input > 2:
            raise Exception('Please select a number between (0-2)')
    except ValueError:
        print('Please select a valid number')
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
    user_input = int(input(f'{player}, choose your position '))
    return user_input

def player_sides(player1,user_input):
    match user_input:
        case 1:
            side = input(f"{player1}, what side would you like to be on? O's or X's: ").upper()
            if side != 'X' and side != 'O':
                raise Exception('please enter a valid input')
            
            else:
                if side.upper() == 'O':
                    first = 'O'
                    second = 'X'
                    return first,second
                else:
                    first = 'X'
                    second = 'O'
                    return first,second
        case 0:
            
            side = input(f"{player1}, what side would you like to be on? O's or X's: ").upper()
            if side != 'X' and side != 'O':
                raise Exception('please enter a valid input')
            
            else:
                if side.upper() == 'O':
                    first = 'O'
                    second = 'X'
                    return first,second
                else:
                    first = 'X'
                    second = 'O'
                    return first,second
        case 2:
            first = 'X'
            second = 'O'
            return first,second        
def computer_inputs(computer_side):
    # easy mode
    rand_pos = ''
    while type(rand_pos) != int:
        rand_pos_board = random.choice(board)
        rand_pos = random.choice(rand_pos_board)
    print(rand_pos)
    change_board(rand_pos,computer_side)

def change_board(player_position,player_side):  
    if player_position in board[2]:
        index = board[2].index(player_position)
        board[2][index] = player_side
    elif player_position in board[1]:
        index = board[1].index(player_position)
        board[1][index] = player_side
    elif player_position in board[0]:
        index = board[0].index(player_position)
        board[0][index] = player_side     
    starting_board(board)     

def win_condition(board,player,player_side):
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