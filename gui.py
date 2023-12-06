import functions
import PySimpleGUI as sg


label = sg.Text("Type in a To-do")
input_box = sg.InputText(tooltip="Enter To-do")

Window = sg.Window("My To-do App", layout=[[label, input_box]])
Window.read()
Window.close()