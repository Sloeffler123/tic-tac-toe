from setup import *

def main():
    starting_rules()
    print('\n')
    user_input = type_of_play()
    name1,name2 = players_name(user_input)
    first,second = sides(name1,name2,user_input)
    print(f'{name1} vs. {name2}')
    on = True
    while on:
        position_x = player_position(name1,board)
        change_board(position_x,first)
        if win_condition(board,name1,first):
            break
        position_o = player_position(name2,board)
        change_board(position_o,second)
        if win_condition(board,name2,second):
            break
    #this is where we need to figure out how to 
    #make player vs player ai vs ai and ai vs player

main()    

