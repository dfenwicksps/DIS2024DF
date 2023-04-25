# Todo app - add complete option
name = input("What is your name? ").title()
print(f"{name}'s To Do List")
#user_prompt = "Enter a todo: (x to exit) "
myTodos = []
run = "y"
#while True:
while run.lower() == "y":
    #todo = input(user_prompt)
    user_action = input("Type add, show, edit, complete or exit: ").strip()

    match user_action:
        case 'exit':
            run = 'n'
        case 'add':
            todo = input("Enter a todo (or press return when done): ").strip().title()
            while todo:
                myTodos.append(todo)
                todo = input("Enter a todo (or press return when done): ").strip().title()
            print(myTodos)
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
        case 'complete':
            number = int(input("Number of the todo to complete: "))
            myTodos.pop(number - 1)
        case _:  # the underscore is recognised as the default capture for unknown commands
            print("You've entered an unknown command.")
print()
print("Thanks for using this app.")