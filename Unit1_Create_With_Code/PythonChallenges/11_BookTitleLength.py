# Write a program that asks the user for the title of a book
# Return the length of the title
# Extension - can you count the number of words in a title
# Extension: respond to the user if you think the title is too short or too long
booktitle = input("Enter the title of a book: ")
words = booktitle.title().split()
print(f"There is {len(words)} words in {booktitle.title()}.")
print(words)
