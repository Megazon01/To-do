import functions
import PySimpleGUI as sg
import time


###THEMES###

sg.theme("DarkBrown4")
#sg.theme("DarkBlue7")
#sg.theme("DarkPurple1")
#sg.theme("LightBlue7")
#sg.theme("BrightColors")

###VARIABLES###
clock = sg.Text("", key="clock")
label = sg.Text("Type in a To-do: ")
input_box = sg.InputText(tooltip="Enter To-do", key="todo")
add_button = sg.Button("Add")
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")
#error_text = sg.Text("", key="error")

list_box = sg.Listbox(values=functions.get_todos(), key="todos",
                      enable_events=True, size=[45, 10])
layout = [[clock], [label], [input_box, add_button],
          [list_box, edit_button, complete_button],
          [exit_button]]

Window = sg.Window("My To-do App",
                   layout=layout, font=("Helvetica", 20))


while True:
    event, values = Window.read(timeout=200)
    Window["clock"].update(value=time.strftime("%H:%M %b %d - %Y"))
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            Window["todos"].update(values=todos)
            Window['todo'].update(value='')

        case "Edit":
            try:
                old_todo = values["todos"][0]
                new_todo = values["todo"] + "\n"
                todos = functions.get_todos()
                index = todos.index(old_todo)
                todos[index] = new_todo
                functions.write_todos(todos)
                Window["todos"].update(values=todos)
            except IndexError:
                #Window["error"].update("Select an item first!")
                sg.Popup("Select an item first!", font=("Helvetica", 15))

        case "Complete":
            try:
                completed_todo = values["todos"][0]
                todos = functions.get_todos()
                todos.remove(completed_todo)
                functions.write_todos(todos)
                Window["todos"].update(values=todos)
                Window['todo'].update(value='')
            except IndexError:
                sg.Popup("Select an item first!", font=("Helvetica", 15))

        case "todos":
            strip_todo = values["todos"][0].strip("\n")
            Window["todo"].update(value=strip_todo)

        case "Exit":
            break

        case sg.WIN_CLOSED:
            break
Window.close()