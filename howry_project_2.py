"""
The program is a remake of the game "Wordle".
It generates a random 5-letter word and gives the user 6 attempts to guess the word with the given hints.

File Name: howry_project_2.py
Author: Ken Howry
Date: 17.1.23
Course: COMP 1352
Assignment: Project II
Collaborators: N/A
Internet Source: N/A
"""

def guess_result(guess: str, answer: str) -> str:
    """
    Description of Function: This function compares the user input to the actual answer and returns "Y/G/B" hint
    Parameters: guess: str -- the user input, answer: str -- the randomly selected word
    Return: str
    """
    #return if the user-input is the correct answer
    if guess == answer:
        return "GGGGG"

    #creating a list
    hint = ["B"] * len(answer)

    #altering the list based off the user-input and replacing the value of answer to deal with duplicates
    for i in range(len(answer)):
        if guess[i] == answer[i]:
            hint[i] = "G"
            answer = answer.replace(guess[i], "-", 1)

    for i in range(len(answer)):
        if guess[i] in answer and hint[i] == "B":
            hint[i] = "Y"
            answer = answer.replace(guess[i], "-", 1)

    return ''.join(hint)

import random
possible_words = []

#extracting the five-letter words the program can pick
with open("projects/usaWords.txt", 'r') as a_file:
    for line in a_file:
        if len(line) == 6:
            data = line.strip()
            possible_words.append(data)

#explaining the program to the user
print("Welcome to Wordle! You have six chances to guess the five-letter word.")
print("A letter G means you got that letter correct and in the right position.")
print("A letter Y means you matched that letter, but it is in the wrong position.")
print("A letter B means that letter does not appear in the correct word.")

quit = False

#variables
#tracks the number of guesses the user makes
user_guesses = 0
#variable for the random word selected
solution = possible_words[random.randint(0, len(possible_words))]
#stores each guess the user makes
guess_storage = []

while not quit:
    #prompting the user for their guess
    user_input = input("What is your guess? ")
    #appending to the list guess_storage
    guess_storage.append(user_input)

    #increasing the number of user guesses
    user_guesses += 1

    #producing the hints for each guess and printing whether the user guessed the answer or failed to guess in 6 guesses
    for i in range(len(guess_storage)):
        #if the user guess is not correct but they still have more guesses
        if user_guesses < 6 and guess_result(guess_storage[i], solution) != "GGGGG":
            print(f"Guess {i+1}: {guess_storage[i]} {guess_result(guess_storage[i], solution)} ")
        #if the user guessed the answer
        elif user_guesses <= 6 and guess_result(guess_storage[i], solution) == "GGGGG":
            print(f"Guess {i+1}: {guess_storage[i]} {guess_result(guess_storage[i], solution)} ")
            print(f"You win. You got it in {user_guesses} guesses.")
            quit = True
    #if the user runs out of guesses
    if user_guesses == 6 and guess_result(guess_storage[i], solution) != "GGGGG":
        print("You lose, you did not guess the word in 6 guesses.")
        quit = True