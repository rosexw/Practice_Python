# https://www.practicepython.org/solution/2014/04/02/08-rock-paper-scissors-solutions.html#comment-3826456333
# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

# Remember the rules:

# Rock beats scissors
# Scissors beats paper
# Paper beats rock

# user1 = raw_input("First player, what's your name? ")
# user2 = raw_input("Second player, what's your name? ")
# user1_answer = raw_input("%s, do you choose rock, paper or scissors? " % user1)
# user2_answer = raw_input("%s, do you choose rock, paper or scissors? " % user2)

# def compare(u1, u2):
#     if u1 == u2:
#         return("It's a tie!")
#     elif u1 == 'rock':
#         if u2 == 'scissors':
#             return("Rock wins!")
#         else:
#             return("Paper wins!")
#     elif u1 == 'scissors':
#         if u2 == 'paper':
#             return("Scissors win!")
#         else:
#             return("Rock wins!")
#     elif u1 == 'paper':
#         if u2 == 'rock':
#             return("Paper wins!")
#         else:
#             return("Scissors win!")
#     else:
#         return("Invalid input! You have not entered rock, paper or scissors, try again.")
#         sys.exit()

# print(compare(user1_answer, user2_answer))

# playAgain = raw_input("Do you want to play again? Type yes or no: ")

# def playAgain(answer):
#     if answer == "yes":
#        return("yes, play again")
#     elif answer == 'no':
#         return("Have a good day, goodbye!")
#     else:
#         return("Invalid input!")
#         sys.exit()

print('Play a game of Rock Paper Scissors')

choices = ['rock', 'scissors', 'paper']
# Game loop
continueGame = True
def playGame(player1, player2):
    if player1 not in choices or player2 not in choices:
        print("Invalid entry. Try again")
    elif choices.index(player1) == choices.index(player2):
        print("Its a tie! Try again")
    elif choices.index(player1) == (choices.index(player2) + 1) % 3:
        print('Player 2 with ' + str(player2) + ' wins!')
    elif choices.index(player2) == (choices.index(player1) + 1) % 3:
        print('Player 1 with ' + str(player1) + ' wins!')
    else:
        print('Not found')


while continueGame == True:
    player1 = raw_input("Player 1 - Rock, Paper, Scissors? ").lower()
    player2 = raw_input("Player 2 - Rock, Paper, Scissors? ").lower()
    playGame(player1, player2)
    continue_text = raw_input("Would you like to continue? Type q to exit:")
    if(continue_text.lower() == "q"):
        continueGame = False
        print("Thank you for playing. Goodbye!")

# while True: 
#     usr_command = raw_input("Enter your command: ")
#     if usr_command == "quit":
#       break
#     else: 
#       print("You typed " + usr_command)