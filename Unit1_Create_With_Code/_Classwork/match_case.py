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