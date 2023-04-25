import random
import math
play = input("Would you like to play? Y/N: ").upper()
guesses = 0
while play == "Y":
    num = random.randint(0, 100)
    print(num)
    # selecting difficulty with difi as variable
    difi = int(input("what difficulty would you like? 1, 2 or 3.  (3 being the hardest): "))
    match difi:
        case 1:  # if difi == 1:
            guess_limit = 7
            guesses = 0
        case 2:  # elif difi == 2:
            guess_limit = 6
            guesses = 0
        case '3':  # elif difi == 3:
            guess_limit = 5
            guesses = 0
    # a way to help with human error
        case '':  # else:
            guess_limit = 0
    print(f"Your guess limit is {guess_limit}")
    while guesses <= guess_limit:
        print(f"You have {guess_limit - guesses} tries left")
        # printing the amount of tries left every time the user is about to guess
        guess = int(input("Guess your number, (0-100): "))
# content copied from above.
        if guess == num:
            guesses = guesses + 1
            print(f"You Guessed it in {guesses} tries")
            break
        elif guess < num:
            guesses = guesses + 1
            print("Go Higher")
        elif guess > num:
            guesses = guesses + 1
            print("Go lower")
    if guesses > guess_limit:
        print(f"Oh no, you hit the guess limit! you lost :(  The number was {num}. You were only {abs(num - guess)} off!")
    play = input("Would you like to play again? Y/N: ").upper()
print("Thankyou for playing my game.")