# Todo app - add enumerate
name = input("What is your name? ").title()
print(f"{name}'s To Do List")
#user_prompt = "Enter a todo: (x to exit) "
myTodos = []
run = "y"
#while True:
while run.lower() == "y":
    #todo = input(user_prompt)
    user_action = input("Type add or show or exit: ").strip()

    match user_action:
        case 'exit':
            run = 'n'
        case 'add':
            todo = input("Enter a todo: ").strip().title()
            while todo:
                myTodos.append(todo)
                todo = input("Enter a todo: ").strip().title()
            print(myTodos)
        case 'show' | 'display':  # the pipe is used as an OR
            print(20 * '*')
            print(f"{name}'s To Do List:")
            for item, elem in enumerate(myTodos):
                print(f"{item + 1}: {elem}")
            print(20 * '*')
        case _:  # the underscore is recognised as the default capture for unknown commands
            print("You've entered an unknown command.")
print()
print("Thanks for using this app.")