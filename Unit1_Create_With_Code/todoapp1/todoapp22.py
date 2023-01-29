# Todo app
name = input("What is your name? ")
nums = 1
print(f"{name}'s To Do List")
user_prompt = "Enter a todo: (x to exit) "
myTodos = []
run = "y"
#while True:
while run.lower() == "y":
    todo = input(user_prompt)
    if todo == "x":
        run = "n"
    else:
        myTodos.append(todo)
        print(myTodos)
        '''
        print(20 * '*')
        print(f"{name}'s To Do List:")
        for item, elem in enumerate(myTodos):
            print(f"{item+1}: {elem}")
        print(20 * '*')
        '''
print("Thanks for using this app.")