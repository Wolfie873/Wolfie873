#! python3
#Guess the number Game
import random #imports random library

print("Hello, what is your Name: ") #print writes stuff
name = input() #variables are created without value, no int var necessary

print("Well " + name + ", I'm thinking of a number between 1 and 20")
secretNumber = random.randint(1, 20)#This saves a random integer between 1 and 20

for guessesTaken in range(1, 7): #notice built in variable range
    print("Take a guess: ")
    guess = int(input()) #Converts string into integer

    if guess < secretNumber:
        print("Nope, too low")
    elif guess > secretNumber:
        print("Nope, too high")
    elif guess == secretNumber:
        print("Ding, ding, ding, ding, ding, ding")
        break

print("You took " + str(guessesTaken) + " guesses.")