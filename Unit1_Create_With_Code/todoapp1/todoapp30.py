# Todo app
name = input("What is your name? ")
print(f"{name}'s To Do List")
myTodos = []
while True:
    user_action = input("Type add or show or exit: ")
    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            myTodos.append(todo)
            #print(myTodos)
        case 'show':
            print(20 * '*')
            print(f"{name}'s To Do List:")
            for item, elem in enumerate(myTodos):
                print(f"{item + 1}: {elem}")
            print(20 * '*')
        case 'exit':
            break
print("Thanks for using this app.")