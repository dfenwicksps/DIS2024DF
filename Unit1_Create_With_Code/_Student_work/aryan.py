print("=== Capital Indexes ===\n")

def capitalIndexes(string):
    indexes = []
    for i, v in enumerate(string):
        #if v.upper() == v:
        if v.isupper():
            indexes.append(i)

    return indexes


while True:
    string = input("Enter string or 'q' to quit: ")

    if string.lower() == "q":
        break

    indexes = capitalIndexes(string)
    print(indexes)
