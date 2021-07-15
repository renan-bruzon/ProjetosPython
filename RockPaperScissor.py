import random
from time import sleep


def computer():
    option = ['rock', 'paper', 'scissor']
    resultado = random.choice(option).upper()
    return resultado


def player(option):
    if option == '1':
        return 'rock'.upper()
    elif option == '2':
        return 'paper'.upper()
    elif option == '3':
        return 'scissor'.upper()
    elif option == '4':
        return 'Thanks See you again.'
        exit()


player_input = '0'

while player_input not in '1234':
    player_input = input('Hello player,\n'
                         '1 - Rock,\n'
                         '2 - Paper,\n'
                         '3 - Scissor,\n'
                         '4 - Exit, \n'
                         'Your choice: ')


if player_input in '123':
    AI_choice = computer()
    Player_choice = player(player_input)
    print('-'*30)
    print(f'You played |--- {Player_choice} --|')
    print(f'The AI played: |-- {AI_choice} --|')
    print('-'*30)
    if Player_choice == 'ROCK' and AI_choice == 'SCISSOR' or Player_choice == 'PAPER' and AI_choice == 'ROCK' or Player_choice == 'SCISSOR' and AI_choice == 'PAPER':
        print('You WON !!!!')
    elif Player_choice == 'SCISSOR' and AI_choice == 'ROCK' or Player_choice == 'ROCK' and AI_choice == 'PAPER' or Player_choice == 'PAPER' and AI_choice == 'SCISSOR' :
        print('You LOST!!!!')
    else:
        print('It is a TIE')
else:
    print(player(player_input))

sleep(5)
