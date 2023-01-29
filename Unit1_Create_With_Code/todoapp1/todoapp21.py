# Todo app - basic app, adding exit to finish
# issue - overwriting todo list

name = input("What is your name? ")
print(f"{name}'s To Do List")
user_prompt = "Enter a todo: "
myTodos = []
while True:
    print("Type exit to finish")
    todo = input(user_prompt)
    if todo == "exit":
        break
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
print(myTodos)
print("Thanks for using this app.")
