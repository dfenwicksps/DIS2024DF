# 4 Lessons per week
# single, single, double, single
# 5 lessons
# Lesson 1 - Write algorithm first as comments
# Generate random number between 1 and 100
import random

global num = random.randint(0, 100)


def myguess(num):
    if user_guess == num:
        return print("You win!")
    elif user_guess > num:
        return print("Too high")
    else:
        return print("Too low")
def game(diff, num):
    guesses = diff
    while guesses < 6:
        user_guess = int(input("Enter a number between 0 and 100: "))
        myguess(user_guess)
        guesses += 1

    print("Sorry you ran out of guesses!")

game(0, 1)