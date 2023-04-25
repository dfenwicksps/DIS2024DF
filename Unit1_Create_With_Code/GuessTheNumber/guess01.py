import random
# Lesson 1 - Write algorithm first as comments
# Generate random number between 1 and 100
num = random.randint(0, 100)  # Generate random number
# Start guesses count
guesses = 0
# Ask user to enter guess
guess = input("Enter a number between 0 and 100: ")
while not type(guess) == int:  # if user_guess is not an integer
    guess = input("Enter a number between 0 and 100: ")  # ask user to enter a number
# game ends when guesses == 6 or user is correct
while guesses != 6:
# Tell user if guess is correct
    if guess == num:
        print(f"Well done! You got it in {guesses} guesses.")
# If guess is not correct, tell user to guess higher or lower
    elif guess > num:
        print("Too high")
    else:
        print("Too low")
# add 1 to guess count
# ask user to guess again

import random

print(num)  # use print to check if random number is being generated


'''Lesson 1 - Write algorithm first as comments

guesses = 0  # Start guesses count
user_guess = int(input("Enter a number between 0 and 100: "))  # User enters guess
if not type(user_guess) == int:  # if user_guess is not an integer
    user_guess = int(input("Enter a number between 0 and 100: "))  # ask user to enter a number
while guesses < 6:  # game ends when guesses == 6
    if user_guess == num:
        print("You win!")  # tell user if guess is correct
        break  # breaks out of the loop and finishes the game
    elif user_guess > num:
        print("Too high")  # tell user if guess is too high
        guesses = guesses + 1  # add 1 to guess count
        user_guess = int(input("Enter a number between 0 and 100: "))
    else:
        print("Too low")  # tell user if guess is too low
        guesses = guesses + 1  # add 1 to guess count
        user_guess = int(input("Enter a number between 0 and 100: "))
'''
