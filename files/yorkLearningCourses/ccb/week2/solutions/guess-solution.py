"""
Generate a random number between 1-100 and ask the user to guess what it is.

"""

import random

def checkGuess(tries, guess):
    if guess == value:
        print( "Correct! The answer is " + str(guess)+ "!")
        print( "You guessed it in " + str(guesses) + " tries!")
        exit(0) #Tells the program to exit 'normally'.
                #Or you could return 0 to terminate the loop
    else:
        if guess < value:
            print( "Sorry, try guessing HIGHER next time")
        elif guess > value:
            print( "Sorry, try guessing LOWER next time")
            
        print( "You have " + str(guessesLeft-1) + " tries left.")

    return tries -1


value = random.randrange(1,101)
guessesLeft = 10
guesses = 0

print( "Guess Me Guess-Zo")
print( "Can you guess my number in 10 tries or less?")

while guessesLeft > 0:
    guess = (input("What is your guess? "))
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        guessesLeft = checkGuess(guessesLeft, guess)
    else:
        print("Please input a digit")

