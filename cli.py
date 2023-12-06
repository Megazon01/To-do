#from functions import get_todos, write_todos
import functions
import time

print("Welcome to your To-do list!")
print(time.strftime("%H:%M %b %d - %Y"))
while True:
    user_action = input("Type stop, add, amount remaining, complete, edit or show: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):

        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo + '\n')

        functions.write_todos(todos)

    elif user_action.startswith("show"):

        todos = functions.get_todos()

        new_todos=[item.strip('\n') for item in todos]

        for index, item in enumerate(new_todos):
            item=item.title()
            print(f"{index+1}. {item}")
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number-1

            todos = functions.get_todos()

            new = input('Enter new: ')
            todos[number] = new + '\n'

            functions.write_todos(todos)
        except ValueError:
            print("Invalid Command. Try inputting 'edit' followed by the number you want to edit.")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            number = number-1

            todos = functions.get_todos()

            rem_todo = todos[number].strip('\n')
            todos.pop(number)

            functions.write_todos(todos)

            print(f"{rem_todo.title()} was removed!")
        except IndexError:
            print("There's no to-do associated with that number!")
            continue

    elif user_action.startswith("amount remaining"):

        todos = functions.get_todos()
        print("To-do's remaining: ", len(todos))

    elif user_action.startswith("stop"):
        break

    else:
        print("Not a valid response.")

print('K Bye Now!')