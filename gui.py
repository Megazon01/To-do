import functions
import PySimpleGUI as sg


label = sg.Text("Type in a To-do: ")
input_box = sg.InputText(tooltip="Enter To-do", key="todo")
add_button = sg.Button("Add")
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
show_button = sg.Button("Show")

Window = sg.Window("My To-do App",
                   layout=[[label, input_box], [add_button, edit_button, complete_button, show_button]],
                   font=("Helvetica", 20))


while True:
    event, values = Window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)

        case sg.WIN_CLOSED:
            break
Window.close()