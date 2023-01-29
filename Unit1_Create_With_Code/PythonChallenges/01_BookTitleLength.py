# Write a program that asks the user for the title of a book
# Return the length of the title
# Extension - can you count the number of words in a title
# Extension: respond to the user if you think the title is too short or too long
booktitle = input("Enter the title of a book: ")
count = 1
print(f"{booktitle.capitalize()} is {len(booktitle)} characters long.")
for i in booktitle:
    if i == " ":
        count += 1
if count == 1:
    print(f"There is {count} word in {booktitle.capitalize()}.")
else:
    print(f"There are {count} words in {booktitle.capitalize()}.")