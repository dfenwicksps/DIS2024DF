#with open("myTextfile2.txt", "r") as file:  # open the file with READ access
#    print(file.read())  # read from the file and output to screen
filename = "myTextfile.txt"
mylist = ["a", "b", "c"]  # create a list and populate with items
name = input("What is your name? ")
mylist.append(name)

for item in mylist:  # iterate over each item in the list
    with open(filename, "a") as file:  # open the file with APPEND access
        file.write(item)  # each item in the list
        file.write("\n")  # write a new line

with open(filename, "r") as file:
    print(file.read())

file = open('myTextfile3.txt', 'w')
file.writelines(['Line 1\n', 'Line 2\n'])
file.close()

file = open('myTextfile3.txt', 'w')
file.write('This is just text here and there. \nThis will be on a new line.')
file.close()
