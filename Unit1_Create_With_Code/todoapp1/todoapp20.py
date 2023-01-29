# Todo app
myTodos = []  # create an empty list to store the todo items (why a list?)
while True:
    todo = input("Enter a todo: ")
    myTodos = todo  # this will overwrite the list each time
    #myTodos.append(todo)  # append adds to list, rather than overwrite
    print(myTodos)
    '''
    print(20 * '*')
    print(f"{name}'s To Do List:")
    for item, elem in enumerate(myTodos):
        print(f"{item}, {elem}")
    print(20 * '*')
    '''