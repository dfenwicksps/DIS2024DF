# REVIEW from last lesson
# STEP 1 - Write an algorithm that solves the problem as a human - test to make sure it works
# STEP 2 - Think about how a computer might read the algorithm -
#       * do you need to save data to variables?
#       * do you know any built in functions that might help you?
# STEP 3 - Write the program by following the algorithm step by step - test to make sure it works
# STEP 4 - Are there any functions you could add to make the program more efficient?
# STEP 5 - Consider useability principles - can you make your program -
#       * ACCESSIBILITY - The ability to be used by many different people, including people with
#           disabilities -> provide clear instructions and feedback
#       * SAFETY - The ability for users to make errors
#       * EFFECTIVENESS & UTILITY - can you add any additional features or functions for the user
#       * LEARNABILITY - is your solution consistent and easy to learn?

question = "What is the title of the book? "
print("Welcome to my Book Title counter.")
print("Enter the title of a book and I will count the characters.")
title = input(question)
count = 0
runagain = "y"
while runagain == "y":
#for char in title:
#    count = count + 1
#print(count)
    print(f"'{title}' is {len(title)} characters in length.")
    runagain = input("Do you want to try another book? ")

print("Thanks for trying my program. See you next time.")