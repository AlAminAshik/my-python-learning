# this is a number guessing game that prompt user input untill the user guesses the correct number

#import random module
import random

n = random.randint(1, 99)       #generate a number between 1 and 99
guess = int(input("Enter an integer from 1 to 99: "))   #input the first number

while True:             #loop until break
    if guess < n:
        print("guess is low")
        guess = int(input("Enter an integer from 1 to 99: "))
    elif guess > n:
        print("guess is high")
        guess = int(input("Enter an integer from 1 to 99: "))
    else:
        print("you guessed it!")
        break