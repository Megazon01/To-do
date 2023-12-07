import functions
import PySimpleGUI as sg


label = sg.Text("Type in a To-do: ")
input_box = sg.InputText(tooltip="Enter To-do", key="todo")
add_button = sg.Button("Add")
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
show_button = sg.Button("Show")
list_box = sg.Listbox(values=functions.get_todos(), key="todos",
                      enable_events=True, size=[45, 10])

Window = sg.Window("My To-do App",
                   layout=[[label, input_box],
                           [add_button, complete_button, show_button],
                           [list_box, edit_button]],
                   font=("Helvetica", 20))


while True:
    event, values = Window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            Window["todos"].update(values=todos)

        case "Edit":
            old_todo = values["todos"][0]
            new_todo = values["todo"] + "\n"
            todos = functions.get_todos()
            index = todos.index(old_todo)
            todos[index] = new_todo
            functions.write_todos(todos)
            Window["todos"].update(values=todos)

        case "todos":
            strip_todo = values["todos"][0].strip("\n")
            Window["todo"].update(value=strip_todo)


        case sg.WIN_CLOSED:
            break
Window.close()