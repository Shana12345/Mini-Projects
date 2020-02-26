#!/usr/bin/env python3.8
import math
import random
# Rather give the locations set locations, you can use the 'Math' operator to set the locations in random places
randomLoc = math.floor
location1 = randomLoc
location2 = location1 + 1
location3 = location2 + 1
guess = []
hits = 0
guesses = 0
isSunk = false


# GET: the user's guess
# Each time you got through the while loop you will need to get input from the user(this case a guess) To do that you use the prompt built-in function. 
# Here you're assigning the result of the prompt function to the guess variable.
# After the prompt function obtains input from the user, it returns that input to your code. In this case the input, in the form of a string, is assigned to the varibale guess.

#Here you are checking the validity by making sure the guess is between zero and six.
guess = input("Ready, aim, fire! (enter a number from 0-6) :")
for x in range(6):
    guess.append(["O"] * 6)
    if (guess < 0 or guess > 6):
        #If the guess isn't valid, we'll tell the user with an alert.
        print("Please enter a valid cell number!")

    else:
        #And if the guess is valid, go ahead and add one to guesses so you can keep track of how many times the user has guessed. 
        #If the guess matches one of the ship's locations you then increment the  the 'guesses' variable by 1. 
        guesses = guesses + 1

        #If the guess matches one of the ship's locations you increment the 'hit' counter.
        #The || in this code means, if guess is equal to location1 OR guess is equal to location2 OR guess isequal to location3, increment hits.
        if (guess == location1 or guess == location2 or guess == location3):
            print("HIT!")
            hits = hits + 1
            #First check to see if there are three hits.
            #And let the user know.
            if (hits == 3):
                isSunk = True
                print("You sank my battleship!")
            else:
                print("MISS")
        #Here you are creating a string that contains a message to the user including the number of guesses they took, along with the accuracy of their shots.
        #Notice that we're splitting up the string into pieces(to insert the variable guesses, and also to fit the string into multiple lines) using the concatenation operator, +.
            stats = "You took " + guesses + " guesses to sunk the battleship, " + "which means your shooting accuracy was " + (3 / guesses)
            print(stats)