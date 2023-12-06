import functions
import PySimpleGUI as sg


label = sg.Text("Type in a To-do: ")
input_box = sg.InputText(tooltip="Enter To-do")
add_button = sg.Button("Add")

Window = sg.Window("My To-do App", layout=[[label, input_box], [add_button]])
Window.read()
Window.close()