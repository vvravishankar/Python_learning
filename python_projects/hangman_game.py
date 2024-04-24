'''

Here's a problem statement based on the provided solution:

Problem Statement: Word Guessing Game

You are tasked with creating a word guessing game in Python. The game randomly selects a word from a predefined list, and the player has to guess the word by providing letters as input.

Requirements:

The game should start by randomly selecting a word from a predefined list of words.
Display the length of the selected word to the player and prompt them to guess the word.
Allow the player to input a letter in each turn.
After each turn, display the progress of the word, showing correctly guessed letters and placeholders for unknown letters.
The player has a limited number of chances to guess the word, equal to the length of the word plus 2.
If the player guesses all the letters correctly within the given number of chances, declare them as the winner.
'''

import random

def random_word():
    word_list = ['PROCESS','ROBLOX', 'JACKBOT', 'JAYAVARDHAN','NEHA','JAMILA', 'NANU','PALAK','HELLO','SPIDERMAN']
    word = random.choice(word_list)
    print(f"Guess the {len(word)} letter word")
    return(word)

def game_line():
    print(word[0],end="")
    for i in range(len(word)-2):
        print(" _ ",end="")
    print(word[-1])

def logic(user_input,word, indexing):
        words = word[1:-1]
        for i in range(len(words)):
          if words[i] == user_input:
            indexing.append(i+1)
        return(indexing)

#main
print("########################################## START ############################################################")
print("LETS BEGIN THE GAME")
print("############################################## THE WORD ###############################################################")

word = random_word()
word_len = len(word)
game_line()
print("############################################### no of Chance ##############################################################")
print(f"You will get {word_len} no of chance")
counter = 0
indexing = [0,(len(word)-1)]

while counter < word_len+2:
    print(f"\n############################################### CHOOSE YOUR CHANCE NO.{counter} ##############################################################")
    user_input = input(f"\nEnter your choice {counter}:- ").upper()
    indexing = logic(user_input, word, indexing)
    counter = counter + 1

    for i in range(word_len):
        if i in indexing:
            print(f" {word[i]}", end="")
        else:
            print(" _ ",end="")
    if len(word) == len(indexing):
        print(f"\n############################################### RESULT #############################################################")
        print("YOU WIN!!!")
        break
if len(word) != len(indexing):
    print(f"\n############################################### RESULT #############################################################")
    print(f"THE WORD was : {word}")
    print("\nBETTER LUCK NEXT TIME")
