print("Welcome to my little Book Title Counter! ")
runagain = "y"
while runagain == "y":
    answer = input("Do you want me to count the characters in the title of the book? (yes/no) ").lower()
    if answer == "yes":
         book = input("What is the title of the book? ")
         print(f"The are {len(book)} characters in the book title {book} including spaces.")
    else:
        runagain = "n"
print("Ok see you next time")