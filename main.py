from setup import *

def player_vs_player(user_input):
    starting_rules()
    print('\n')
    name1,name2 = players_name(user_input)
    first,second = player_sides(name1,user_input)
    print(f'{name1} vs. {name2}')
    on = True
    while on:
        position_x = player_position(name1)
        change_board(position_x,first)
        if win_condition(board,name1,first):
            break
        position_o = player_position(name2)
        change_board(position_o,second)
        if win_condition(board,name2,second):
            break

def player_vs_computer(user_input):
    starting_rules()
    print('\n')
    name1,name2 = players_name(user_input)
    first,second = player_sides(name1,user_input)
    print(f'{name1} vs. {name2}')
    on = True
    while on:
        position_x = player_position(name1)
        change_board(position_x,first)
        if win_condition(board,name1,first):
            break
        position_o = computer_inputs(second)
        if win_condition(board,name2,second):
            break

def main():
    user_input = type_of_play()
    if user_input == 0:
        player_vs_computer(user_input)
    elif user_input == 1:
        player_vs_player(user_input)    
main()    