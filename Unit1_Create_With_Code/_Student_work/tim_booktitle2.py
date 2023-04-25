# create a program that counts the number of words in a book title
# advise user if title is 3 words or greater it won't sell as well on Amazon
# praise user if title is 1 or 2 words - these titles sell best on Amazon


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