#!/usr/bin/env python3.8
import random

# Rather give the locations set locations, you can use the 'Math' operator to set the locations in random places
location1 = 1
location2 = 2
location3 = 5
guess = []
guesses = 0
limit = 3
notSunk = True

name = input('please enter your name: \n')
while notSunk:

    if guesses == limit:
        notSunk = False
        break
        # here 'False' means you don't want the application to run and 'True' means you want them to continue (which means the 'notSunk' variable is 'True')
    
    guess = int(input('Hello ' + name + ' enter a number from 0-6: '))
    
    if guess < 0 and guess > 6:
        print('Invalid entry')

    elif guess == location1 or guess == location2 or guess == location3:
        print('HIT')
        guesses += 1

    elif guess != location1 or guess != location2 or guess != location3:
        print('MISS')
        guesses = guesses + 1
   