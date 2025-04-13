from setup import *
board = [
    [7,8,9],
    [4,5,6],
    [1,2,3],
]
def main():
    starting_board(board)
    starting_rules()
    print('\n')
    user_input = type_of_play()
    name1,name2 = players_name(user_input)
    print(f'{name1} vs. {name2}')
    #this is where we need to figure out how to 
    #make player vs player ai vs ai and ai vs player

main()    