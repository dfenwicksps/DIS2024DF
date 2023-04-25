# Todo app - storing items in text files
name = input("What is your name? ").title()
print(f"{name}'s To Do List")
#user_prompt = "Enter a todo: (x to exit) "
myTodos = []
run = "y"
#while True:
while run.lower() == "y":
    #todo = input(user_prompt)
    user_action = input("Type add, show, edit or exit: ").strip()

    match user_action:
        case 'exit':
            run = 'n'
        case 'add':
            todo = input("Enter a todo (or press return when done): ").strip().title() + "\n"
            file = open('todos.txt')
            myTodos = file.readlines()
            file.close()
            myTodos.append(todo)
            file = open('todos.txt', 'w')
            file.writelines(myTodos)

            #while todo != "\n":
            #    myTodos.append(todo)
            #    todo = input("Enter a todo (or press return when done): ").strip().title() + "\n"
            #print(myTodos)
        case 'show' | 'display':  # the pipe is used as an OR
            print(20 * '*')
            print(f"{name}'s To Do List:")
            if len(myTodos) == 0:
                print("-- You haven't added any To Do's yet!")
            for item, elem in enumerate(myTodos):
                print(f"{item + 1}: {elem}")
            print(20 * '*')
        case 'edit':
            number = int(input("Enter number of todo to edit: "))  # convert input from str to int
            number -= 1  # take away 1 to match item to index
            new_todo = input("Enter new todo: ")
            myTodos[number] = new_todo  # overwrite/replace an item in a list
        case _:  # the underscore is recognised as the default capture for unknown commands
            print("You've entered an unknown command.")
print()
print("Thanks for using this app.")