# REVIEW from last lesson
# STEP 1 - Write an algorithm that solves the problem as a human - test to make sure it works
# STEP 2 - Think about how a computer might read the algorithm -
#       * do you need to save data to variables?
#       * do you know any built in functions that might help you?
# STEP 3 - Write the program by following the algorithm step by step - test to make sure it works
# STEP 4 - Are there any functions you could add to make the program more efficient?
# STEP 5 - Consider useability principles - can you make your program -
#       * ACCESSIBILITY - The ability to be used by many different people, including people with disabilities -> provide clear instructions and feedback
#       * SAFETY - The ability for users to make errors
#       * EFFECTIVENESS & UTILITY - can you add any additional features or functions for the user
#       * LEARNABILITY - is your solution consistent and easy to learn?
print("Welcome to my Book Title counter.")
print("Enter the title of a book and I will count the characters.")
title = ''
books = []
length = []
mydict = {}
while title.lower() != 'q':
    title = input("What is the title of the book? (or q to quit): ")
    if title != 'q':
        books.append(title.title())
        length.append(len(title))
        print(f"'{title.capitalize()}' is {len(title)} characters in length.")
for i in range(len(books)):
    mydict[books[i]] = length[i]
print(mydict)
print(50 * '=')
print("The books you checked were:")
for idx, (books, length) in enumerate(mydict.items()):
    print(f"{idx+1}: '{books}', has {length} characters.")
print(50 * '=')
print("Thanks for trying my program. See you next time.")