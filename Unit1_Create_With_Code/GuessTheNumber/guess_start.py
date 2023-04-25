# Lesson 1 - Write algorithm first as comments
# Generate random number between 1 and 100
import random

num = random.randint(0, 100)  # Generate random number
# Start guesses count
guesses = 0
# Ask user to enter guess
guess = input("Enter a number between 0 and 100: ")
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