

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
        user_input = input('Select an option (0-2): ')
    except ValueError:
        print('Please select a valid number')
    return user_input

def player1_name():
    player_name = input("Please enter player 1's name: ")
    return player_name

def player2_name():
    player_name = input("Please enter player 2's name: ")
    return player_name

def player_position(player):
    user_input = input(f'{player}, choose your position')
    return user_input



#if both players are none then assign both to be AI if one is absent assign player 2 as AI
def player_sides(player_1=None, player_2=None):
    if player_1 is None and player_2 is None:
        pass

def change_board(player_position,player_side):
    position = board[0][player_position]
    board.remove(position)
    new_pos = board.insert(position,player_side)
    starting_board(new_pos)
    
