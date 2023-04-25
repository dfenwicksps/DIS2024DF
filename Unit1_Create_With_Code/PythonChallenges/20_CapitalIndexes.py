'''
Challenge
Capital indexes
Write a function named capital_indexes.
The function takes a single parameter, which is a string.
Your function should return a list of all the indexes in the string that have capital letters.

For example, calling capital_indexes("HeLlO") should return the list [0, 2, 4].
'''


# Solution starts here
def capital_indexes(myString):
    myList = []
    for char in myString:
        if char.isupper():
            myList.append(myString.index(char))
    return myList

def capital_indexes2(myString):
    myList = []
    for index, char in enumerate(myString):
        if char.isupper():
                myList.append(index)
    #print(myList)
    return myList

answer = capital_indexes("qUesTiOn")
print(answer)
answer = capital_indexes2("qUesTiOn")
print(answer)

