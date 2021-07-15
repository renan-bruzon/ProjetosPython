from time import sleep

nome = str(input('What is your name adventurer: '))
welcome_msg = str(f'Welcome to the best story of your life {nome}')
for letra in welcome_msg:
    print(letra, end='')
print()
sleep(2)
print('-'*30)
message = str('You find yourself in front of a cave....\n'
              'what do you do ?\n'
              '1 - Be a scaredy cat and go back the way you came.\n'
              '2 - Remeber how good you were at runescape and enter the cave\n')
for letra in message:
    print(letra, end='')
    sleep(0.05)
intro_opc = 0
cont = 0
intro_opc = str(input('Your decision: '))[0]
while intro_opc not in '12':
    print('Cmon dont be an ass you have only two options... why would try to break the game?')
    intro_opc = str(input('Your decision: '))[0]
    cont += 1
print('-'*30)
if intro_opc == '1':
    text_01 = str('You chose the wrong answer my friend\n'
                  'as you walk away and the cave vanishes behind you...\n'
                  'you go back to your boring normal life...\n'
                  '....\n'
                  'I tried to give you an adventure\n'
                  'GF\n')

    for letra in text_01:
        print(letra, end='')
        sleep(0.1)
    print('-' * 30)
    input('Press ENTER to exit')
    quit()
if intro_opc == '2':
    text_02 = str('As you enter the cave you notice some movement...\n'
                  'there is some lizard-like monsters,\n'
                  'they are green with some spikes on their backs...\n'
                  'next to them you find a grave....\n'
                  'they dont seem to be bothered by your presence\n'
                  'what do you want to do ?\n '
                  '1 - Check the grave.\n'
                  '2 - Fight the monsters barehanded.\n')

    for letra in text_02:
        print(letra, end='')
        sleep(0.1)

opc = 0
cont = 0
opc = str(input('Your decision: '))[0]
while opc not in '12':
    print('Cmon dont be an ass you have only two options... why would try to break the game?')
    opc = str(input('Your decision: '))[0]
print('-' * 30)
if opc == '1':
    text_03 = str('you approach the grave and there is some equipment on the ground...\n'
                  'Hey lucky you, it is a full rune set and a rune scimitar\n'
                  'you take them and put on yourself\n'
                  'when you look up to see if there is a name on the grave...\n'
                  'it does...\n'
                  'it says: \n'
                  '"An Adventurer was killed by the poison of the cave crawlers"\n'
                  'Now you know what these things are called and that they can poison you\n'
                  'be careful....\n')
    for letra in text_03:
        print(letra, end='')
        # sleep(0.1)
    print('-' * 30)
if opc == '2':
    text_04 = str('Dude ! Barehanded ? Really? Are you out of you mind?\n'
                  'they are almost as big as you...\n'
                  'go check that grave will you...\n')

    for letra in text_04:
        print(letra, end='')
        sleep(0.1)
    text_03 = str('you approach the grave and there is some equipment on the ground...\n'
                  'Hey lucky you, it is a full rune set and a rune scimitar\n'
                  'you take them and put on yourself\n'
                  'when you look up to see if there is a name on the grave...\n'
                  'No name, but...\n'
                  'it says: \n'
                  '"An Adventurer was killed by the poison of the cave crawlers"\n'
                  'Now you know what these things are called and that they can poison you\n'
                  'be careful....\n')
    for letra in text_03:
        print(letra, end='')
        sleep(0.1)
    print('-' * 30)
text_05 = str('Now  gather all your strenght and choose the smallest of the lizards to fight\n'
              'It is an intense battle, you avoid the spikes and the tongue, with agility you didnt know you had \n'
              '(dont worry I always believed in you ! )\n'
              'after hitting a few zeros, some tens and taking some damage, you manage to beat the creature \n'
              'As you collect your loot from the ground, you sense someone aproaching you.... \n'
              'it is another adventure, but he is only in his underwear...\n'
              'you try not to laugh\n'
              'and finally asked what happened...\n'
              'the adventurer says:\n'
              '"Man those stupid monsters killed me, i didnt know they could poison me (*sadface*)"\n'
              'you reply: \n'
              '"Hey you live, you learn"\n'
              f'"BTW my name is {nome} and Whats your name? "\n'
              'Then the adventurer replies:\n'
              '"Im Cannibal_BR ...."\n')
for letra in text_05:
    print(letra, end='')
    sleep(0.1)
print('-' * 30)

print('BASED ON TRUE EVENTS')
print('Dedicated to my friends')
print('Wagzilla, Pipinha999, FubecaBR')
print('Short story made by Roshirov')

input('Press ENTER to exit')