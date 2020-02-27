#!/usr/bin/env python3.8
import random

# this simple displays games instruictions
print('Winning rules of game: \n'
       'rock vs paper means paper wins \n'
       'rock vs scissor means rock wins \n'
       'paper vs scissor means scissor wins \n')

while True:
    print('you go first \n 1.Rock \n 2.Paper \n 3.Scissors \n')

    

    #OR is a short-cut element
    #if any one of the condition is true
    #then return True value

    #this will loop until the user enters invalid input
    
    choice = int(input("User's turn: "))
    #computer chooses randomly any number among the 'choice' 
    #using the randint method in the random module
    com_choice = random.randint(1, 3)
    # initialize value of choice_name variable (new variable at this state)
    # this will correspond to the choice value
    if choice == com_choice:
        print('It is a tie')

    elif choice == 1:
        if com_choice ==2:
            print('Computer wins')

    elif com_choice ==3:
        print('You win')

    elif choice == 2:
        if com_choice == 1:
            print('You win')
        elif com_choice == 3:
            print('Computer wins')

    else:
        if com_choice == 1:
            print('Computer wins')
        elif com_choice == 2:
            print('You win')
    

    ans = input('Do you wish to play again? (Y/N)')
    if ans == 'n'or ans == 'N':
        break
    

    #after coming out of the loop
    #it print thanks for play
print('\nThanks for playing')