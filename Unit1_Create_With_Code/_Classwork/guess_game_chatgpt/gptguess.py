import random


def main():
    print("Welcome to the number guessing game!")
    print("I am thinking of a number between 0 and 1000. You have 6 attempts to guess it.")

    number_to_guess = random.randint(0, 1000)
    attempts_left = 6

    while attempts_left > 0:
        try:
            user_guess = int(input("Enter your guess: "))
        except ValueError:
            print("Invalid input. Please enter an integer between 0 and 1000.")
            continue

        if user_guess < 0 or user_guess > 1000:
            print("Please enter a number between 0 and 1000.")
            continue

        if user_guess == number_to_guess:
            print(f"Congratulations! You guessed the correct number {number_to_guess}!")
            break
        elif user_guess < number_to_guess:
            print("Your guess is too low.")
        else:
            print("Your guess is too high.")

        attempts_left -= 1
        print(f"Attempts left: {attempts_left}")

    if attempts_left == 0:
        print(f"Sorry, you ran out of attempts. The correct number was {number_to_guess}.")


if __name__ == "__main__":
    main()
