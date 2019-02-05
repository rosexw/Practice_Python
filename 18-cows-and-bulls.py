# Create a program that will play the “cows and bulls” game with the user. The game works like this:
# Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every digit that the
# user guessed correctly in the correct place, they have a “cow”. For every digit the user guessed
# correctly in the wrong place is a “bull.” Every time the user makes a guess, tell them how many
# “cows” and “bulls” they have. Once the user guesses the correct number, the game is over. Keep track
# of the number of guesses the user makes throughout teh game and tell the user at the end.
# Say the number generated by the computer is 1038. An example interaction could look like this:
#   Welcome to the Cows and Bulls Game!
#   Enter a number:
#   >>> 1234
#   2 cows, 0 bulls
#   >>> 1256
#   1 cow, 1 bull

import random

def isthisit (guess):
    # numberGenerated = 1038
    numberGenerated = str(random.randint(1000,9999))

    numberAsAList = [int(x) for x in list(str(guess))]
    print(numberAsAList)
    numberAsAListGen = [int(x) for x in list(str(numberGenerated))]
    print(numberAsAListGen)
    cows = 0
    bulls = 0

    if guess == numberGenerated:
        cows = 4
        bulls = 0
        print("You guessed it! " + str(cows) + " cows and " + str(bulls) + " bulls")
    else:
        for i in range(len(numberAsAList)): # assuming the lists are of the same length
            if numberAsAList[i] == numberAsAListGen[i]:
                cows +=1
            for j in range(len(numberAsAListGen)):
                if numberAsAList[i] == numberAsAListGen[j] and numberAsAList[i] != numberAsAListGen[i]:
                    bulls += 1
        
        if cows == 1 and bulls > 1:
            print(str(cows) + " cow, " + str(bulls) + " bulls")
        elif cows == 0 and bulls > 1:
            print(str(bulls) + " bulls")
        elif cows == 1 and bulls == 1:
            print(str(cows) + " cow, " + str(bulls) + " bull")
        elif cows > 1 and bulls == 0:
            print(str(cows) + " cows")
        elif cows == 1 and bulls == 0:
            print(str(cows) + " cow")
        elif cows == 1 and bulls > 1:
            print(str(cows) + " cow", + str(bulls) + " bulls")
        elif cows > 1 and bulls > 1:
            print(str(cows) + " cows, " + str(bulls) + " bulls")
        else:
            print("0 cows, 0 bulls")

if __name__=="__main__":
    print("Welcome to the Cows and Bulls Game!")
    while True:
        guess = input("Enter 4 digits: ")
        try:
            if len(str(guess)) != 4:
                print("Incorrect value, please try again")
            elif guess == "quit":
                print("Goodbye")
                break
            else:
                isthisit(int(guess))
        except ValueError:
            ## ValueError: Raised when a built-in operation or function receives an argument that has the right type but an inappropriate value
            print("Incorrect value, please try again")
  