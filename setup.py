
board = [
    [7,8,9],
    [4,5,6],
    [1,2,3],
]

#board[0][wherever they want to play]
#input is 1-9 
#for ai just have it randomly select a space that has not been selected this could be easy mode
#for hard mode make the ai smarter
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

def player_position(player,board):
    starting_board(board)
    user_input = int(input(f'{player}, choose your position '))
    return user_input

#if both players are none then assign both to be AI if one is absent assign player 2 as AI
def sides(player1,player2,user_input):
    match user_input:
        case 0:
            side = input(f"{player1}, what side would you like to be on? O's or X's")
            if side.isalpha():
                if side.upper() == 'O':
                    first = 'O'
                    second = 'X'
                    return first,second
            else:
                raise Exception('Please enter a valid input')        
        case 1:
            first = 'X'
            second = 'O'
            return first,second
        case 2:
            first = 'X'
            second = 'O'
            return first,second
        
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
def win_condition(board,):
    if all(board[0]):
        pass
    elif all(board[1]):
        pass
    elif all(board[2]):
        pass
    elif all(board[0][0],board[1][1],board[2][2]):
        pass
    elif all(board[0][2],board[1][1],board[2][0]):
        pass
    elif all(board[0][0],board[1][0],board[2][0]):
        pass
    elif all(board[0][2],board[1][2],board[2][2]):
        pass
    elif all(board[0][1],board[1][1],board[2][1]):
        pass