import random

l = ['stone', 'paper', 'scissor']
name = input('enter your name :')
name = name.upper()
print('''
            HI {} THIS IS THE STONE PAPER SCISSORS GAME BY VINAY SINGHANIA
            SOME BASIC INSTRUCTIONS
        +––––––––––––––––––––+
        |    Enter --:                       |
        |   * ST FOR STONE       |
        |   * P FOR PAPER          |
        |    * S FOR SCISSORS  |
        +–––––––––––––––––––––+
         ENJOY
'''.format(name))
computer_points = 0
user_points = 0

rounds = int(input('enter the limits of game :'))
counter = 0
while counter <= (rounds):
    if counter == rounds:
        print('GAME POINT')
    print('STONE...PAPER...SCISSOR....')
    print('-' * 20)

    computerturn = random.choice(l)
    userturn = input('enter your argument :')  # user turn
    userturn = userturn.lower()
    print('Chances remaining-',(rounds-counter))
    print('computer---', computerturn)  # computer turn
    print('-' * 20)
    if userturn == 's' and computerturn == l[0]:
        computer_points += 1
        print('Computer WINS !')
        print('-' * 20)
        print('computer points-', computer_points)
        print(name + 'points-', user_points)
        print('-' * 20)
    elif userturn == 's' and computerturn == l[1]:
        user_points += 1
        print(name + ' WINS !')
        print('-' * 20)
        print('computer points-', computer_points)
        print(name + '  points-', user_points)
        print('-' * 20)
    elif userturn == 's' and computerturn == l[2]:
        print('TIE')
        print('-' * 20)
        print('computer points-', computer_points)
        print(name + 'points-', user_points)
        print('-' * 20)
    elif userturn == 'p' and computerturn == l[0]:
        user_points += 1
        print(name + 'WINS !')
        print('-' * 20)
        print('computer points-', computer_points)
        print(name + 'points-', user_points)
        print('-' * 20)
    elif userturn == 'p' and computerturn == l[1]:
        print('TIE')
        print('-' * 20)
        print('computer points-', computer_points)
        print(name + 'points-', user_points)
        print('-' * 20)
    elif userturn == 'p' and computerturn == l[2]:
        computer_points += 1
        print('Computer WINS !')
        print('-' * 20)
        print('computer points-', computer_points)
        print(name + 'points-', user_points)
        print('-' * 20)
    elif userturn == 'st' and computerturn == l[0]:
        print('TIE')
        print('-' * 20)
        print('computer points-', computer_points)
        print(name + 'points-', user_points)
        print('-' * 20)
    elif userturn == 'st' and computerturn == l[1]:
        computer_points += 1
        print('Computer WINS !')
        print('-' * 20)
        print('computer points-', computer_points)
        print(name + 'points-', user_points)
        print('-' * 20)
    elif userturn == 'st' and computerturn == l[2]:
        user_points += 1
        print(name + 'WINS !')
        print('-' * 20)
        print('computer points-', computer_points)
        print(name + 'points-', user_points)
        print('-' * 20)
    else:
        counter = counter - 1
        print('pls check spelling ')
        print('''
    –––––––––––––––––––––––––––
   |      Enter --:                                |      
   |        * ST FOR STONE             |
   |         * P FOR PAPER               |
   |         * S FOR SCISSORS        |
   ––––––––––––––––––––––––––––
        ''')
    counter += 1
if user_points > computer_points:
    print('''
    CONGRATULATIONS !🎉🎉  {} YOU WON THIS GAME
    '''.format(name))
else:
    print('''
    YOU LOSE
    BETTER LUCK NEXT TIME
    
    
    ''')
