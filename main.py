from setup import *

def player_vs_player(user_input):
    
    print('\n')
    name1,name2 = players_name(user_input)
    first,second = player_sides(name1,user_input)
    print(f'{name1} vs. {name2}')
    on = True
    while on:
        position_x = player_position(name1)
        change_board(position_x,first,name1)
        if win_condition(first):
            print(f'{name1} wins!!!')
            break
        if check_draw():
            print('Thats a draw!!!')
            break
        position_o = player_position(name2)
        change_board(position_o,second,name2)
        if win_condition(second):
            print(f'{name2} wins!!!')
            break
        if check_draw():
            print('Thats a draw!!!')
            break

def player_vs_computer(user_input):
    print('\n')

    name1,name2 = players_name(user_input)
    first,second = player_sides(name1,user_input)
    comp_difficulty = input('What difficulty would you like to play? (E)asy, (M)edium, (I)mpossible: ').upper()
    print(f'{name1} vs. {name2}')
    if comp_difficulty == 'E':
        on = True
        while on:
            position_x = player_position(name1)
            change_board(position_x,first,name1)
            if win_condition(first):
                print(f'{name1} wins!!!')
                break
            if check_draw():
                print('Thats a draw!!!')
                break
            computer_inputs(second,name2)
            if win_condition(second):
                print(f'{name2} wins!!!')
                break
            if check_draw():
                print('Thats a draw')
                break
    elif comp_difficulty == 'M':
        on = True
        while on:
            position_x = player_position(name1)
            change_board(position_x,first,name1)
            if win_condition(first):
                print(f'{name1} wins!!!')
                break
            if check_draw():
                print(f'Thats a draw!!!')
                break
            computer_medium(second,first,name2)
            if win_condition(second):
                print(f'{name2} wins!!!')
                break
            if check_draw():
                print(f'Thats a draw')
                break
    else:
        on = True
        while on:
            position_x = player_position(name1)
            change_board(position_x,first,name1)
            starting_board(board)
            if win_condition(first):
                print(f'{name1} wins!!!')
                break
            if check_draw():
                print(f'Thats a draw!!!')
                break
            computer_hard(name1,second,first,name2,True)
            starting_board(board)
            if win_condition(second):
                print(f'{name2} wins!!!')
                break
            if check_draw():
                print(f'Thats a draw!!!')
                break
def computer_vs_computer(user_input):
    
    print('\n')
    name1,name2 = players_name(user_input)
    first,second = player_sides(name1,user_input)
    print(f'{name1} vs. {name2}')
    on = True
    while on:
        position_x = computer_inputs(first,name1)
        if win_condition(first):
            print(f'{name1} wins!!!')
            break
        if check_draw():
            print('Thats a draw!!!')
            break
        position_o = computer_inputs(second,name2)
        if win_condition(second):
            print(f'{name2} wins!!!')
            break
        if check_draw():
            print('Thats a draw!!!')
            break

def main():
    starting_rules()
    user_input = type_of_play() 
    if user_input == 0:
        player_vs_computer(user_input)
    elif user_input == 1:
        player_vs_player(user_input) 
    elif user_input == 2:
        computer_vs_computer(user_input) 
    play_again = input('Would you like to play again? (Y)es or (N)o ').upper()
    if play_again == 'Y' or play_again == 'YES':
        reset()
        main()              
main()    