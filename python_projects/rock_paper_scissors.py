'''
Problem Statement: Rock, Paper, Scissors Game

You're tasked with creating a simple console-based game of Rock, Paper, Scissors in Python. The game should allow the user to play against the computer for a specified number of rounds.

Requirements:

The game should start by prompting the user to input their choice: 'r' for Rock, 'p' for Paper, or 's' for Scissors.
The computer should randomly select its choice from the same options.
Determine the winner for each round based on the following rules:
Rock beats Scissors
Paper beats Rock
Scissors beats Paper
Keep track of the number of rounds played and the number of rounds won by the user.
After the specified number of rounds, determine the overall winner:
If the user wins more than half of the rounds, declare the user as the winner.
If the user wins exactly half of the rounds, declare a tie.
If the user wins less than half of the rounds, declare the computer as the winner.

'''
import random

def userinput():
    print("##################################### CHOOSE ########################################################################")
    print("Select your choice as under:")
    print("r for ROCK || p for PAPER || s fo SCISSORS")
    user_input = input("your Choice :-")
    return(user_input.lower())

def randominput():
    list = ['r', 'p', 's']
    random_input = random.choice(list)
    return(random_input)

def game(user,ran):
    if user == ran:
        val = 'tie'
    elif (user == 'r' and ran == 's') or (user == 'p' and ran == 'r') or (user == 's' and ran == 'p'):
        val = 'user'
    else:
        val = 'comp'
    return(val,user,ran)

# main
print("########################################## START ############################################################")
print("LETS BEGIN THE GAME")
print("#############################################################################################################")
times = int(input("No. of times you would like to play:-"))
print(f"############################################ LET'S PLAY FOR {times} TIMES #################################################################")
print(f"We will have best of {times}")
counter = 0
user_win = 0
while counter < times:
    counter = counter+1
    result, user, ran = game(userinput(), randominput())
    if result == 'user':
       user_win = user_win + 1
    print(f"############################################### GAME DETAIL {counter} ##############################################################")
    print(f"Game no:- {counter}")
    print(f"User input:- {user}")
    print(f"Comp input:- {ran}")
    if result == 'tie':
        print("The game is Tie")
    else:
        print(f"Game is won by:- {result}")
    print(f"Number of Game won by User is :- {user_win} / {times}")

print("########################################### FINAL RESULT ##################################################################")
if user_win > (times/2):
    print("You have Won the GAME")
elif user_win == (times/2):
    print("Its is Tie")
else:
    print("Better LUCK next time")
print("########################################### END ##################################################################")
